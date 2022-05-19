# websearch
websearch is a Python library for searching DuckDuckGo, easily. websearch uses requests and BeautifulSoup4 to scrape DuckDuckGo. 

## Installation
To install, run the following command:
```bash
python3 -m pip install pyduckduckgosearch
```

## usage
To get results for a search term, simply use the search function in websearch. For example, to get results for "DuckDuckGo" in DuckDuckGo, just run the following program:
```python
from websearch import search
search("DuckDuckGo")
```

## Additional options
websearch supports a few additional options. By default, websearch returns 10 results. This can be changed. To get a 100 results on DuckDuckGo for example, run the following program.
```python
from websearch import search
search("DuckDuckGo", num_results=100)
```
In addition, you can change the language DuckDuckGo searches in. For example, to get results in French run the following program:
```python
from websearch import search
search("DuckDuckGo", lang="fr")
```
## websearch.search
```python
websearch.search(str: term, int: num_results=10, str: lang="en") -> list
```
