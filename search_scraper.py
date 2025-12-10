import requests
from bs4 import BeautifulSoup

def duckduckgo_search(query):
    url = "https://duckduckgo.com/html/"
    params = {"q": query}

    response = requests.post(url, data=params)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for item in soup.select(".result"):
        title = item.select_one(".result__a")
        snippet = item.select_one(".result__snippet")
        link = item.select_one(".result__a")

        results.append({
            "title": title.get_text(strip=True) if title else "",
            "link": link["href"] if link else "",
            "snippet": snippet.get_text(strip=True) if snippet else "",
        })

        if len(results) >= 5:
            break

    return results
