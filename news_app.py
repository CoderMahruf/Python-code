import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-10-14&sortBy=publishedAt&apiKey=7831074bfff64db9849d71672075e1d0"
r = requests.get(url)
news = json.loads(r.text)

if news.get("status") == "ok":
    for article in news.get("articles", []):
        print(article["title"])
        print(article["description"])
        print("--------------------------------------")
else:
    print("Error fetching news:", news.get("message", "Unknown error occurred"))
