from urllib.parse import urlparse, parse_qs, urlencode

import re

url = ["https://example.com/shop?category=books&sort=desc#reviews",
       "http://news.site.com/resources?articles?page=5&category=tech",
       "https://blog.example.org/?author=alice&year=2024"]

for i in url:
    parsed_url = urlparse(i)
    print(f"Domain: {parsed_url.netloc}")
    print(f"Path: {parsed_url.path}")
    print(f"Query: {parsed_url.query}")

    parsed_url = urlparse(i)
    query_params = parse_qs(parsed_url.query)
    print(f"Query Params: {query_params}")
    print("===========================")


with open("text.txt") as file:
    for line in file:
        urls = re.findall('https?://(?:[ -\w.]|(?:%[\da-fA-F]{2}))+', line)
        print(urls)