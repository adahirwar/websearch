#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:13:20 2022

@author: Arvind Ahirwar
"""
import csv
import json
import os
import re
import unicodedata
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from time import sleep

import click
import requests
from lxml import html

__version__ = "1.0.1"


session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"
}
session.headers.update(headers)


def _slugify(filename):
    """
    Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """

    filename = unicodedata.normalize("NFC", filename)
    filename = re.sub(r"[^\w\s-]", "", filename.lower())
    return re.sub(r"[-\s]+", "-", filename).strip("-_")


def _normalize(text):
    if text:
        body = html.fromstring(text)
        return html.tostring(body, method="text", encoding="unicode")
    
class SearchResult:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self):
        return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"


def search(
    keywords,
    region="wt-wt",
    safesearch="Moderate",
    time=None,
    max_results=5,
    output=None,
):
    """DuckDuckGo search
    Query parameters, link: https://duckduckgo.com/params:
    keywords: keywords for query;
    safesearch: On (kp = 1), Moderate (kp = -1), Off (kp = -2);
    region: country of results - wt-wt (Global), us-en, uk-en, ru-ru, etc.;
    time: 'd' (day), 'w' (week), 'm' (month), 'y' (year);
    max_results = 5 gives a number of results not less than 5,
                  maximum Duckduckgo gives out about 200 results,
    output: csv, json, print.
    """

    if not keywords:
        return None

    # get vqd
    payload = {
        "q": keywords,
    }
    res = session.post("https://duckduckgo.com", data=payload)
    tree = html.fromstring(res.text)
    vqd = (
        tree.xpath("//script[contains(text(), 'vqd=')]/text()")[0]
        .split("vqd='")[-1]
        .split("';")[0]
    )
    sleep(0.75)

    # search
    safesearch_base = {"On": 1, "Moderate": -1, "Off": -2}
    params = {
        "q": keywords,
        "l": region,
        "p": safesearch_base[safesearch],
        "s": 0,
        "df": time,
        "o": "json",
        "vqd": vqd,
    }
    results = []
    while len(results) < max_results and params["s"] < 200:
        resp = session.get("https://links.duckduckgo.com/d.js", params=params)
        try:
            data = resp.json()["results"]
        except:
            return results

        for r in data:
            try:
                s = r["n"].split("s=")[1].split("&")[0]
                params["s"] = int(s) - int(s) % 2
                break
            except:
                    title = _normalize(r["t"])
                    href = r["u"]
                    body = _normalize(r["a"])
                    if body:
                        sleep(0.75)
                        yield SearchResult(href, title, body)
                        
