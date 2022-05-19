# websearch
websearch is a Python library for searching DuckDuckGo, easily. websearch uses requests and BeautifulSoup4 to scrape DuckDuckGo. 

## Installation
To install, run the following command:
```bash
python3 -m pip install pyduckduckgosearch
```

## Usage
To get results for a search term, simply use the search function in websearch. For example, to get results for "DuckDuckGo" in DuckDuckGo, just run the following program:
```python
from websearch import search
keywords = 'what is machine learning'
results = search(keywords, region='wt-wt', safesearch='Moderate', time='y', max_results=2)
print(results.__next__().__dict__)
```
