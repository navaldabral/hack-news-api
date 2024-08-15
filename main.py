from fastapi import FastAPI, HTTPException, Query
import requests
import cachetools



app = FastAPI()

news_api = "https://hacker-news.firebaseio.com/v0"
cache_time = 600 
cache = cachetools.TTLCache(maxsize=100, ttl=cache_time)


def fetch_top_news(count: int):
    cached_data = cache.get("top_news")
    if cached_data:
        return cached_data[:count]
    top_news_url = f"{news_api}/topstories.json"
    response = requests.get(top_news_url)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch top News.")
    top_news_ids = response.json()[:count]
    top_news = []
    for news_id in top_news_ids:
        news_url = f"{news_api}/item/{news_id}.json"
        news_response = requests.get(news_url)
        if news_response.status_code == 200:
            news_data = news_response.json()
            top_news.append({
                "Title": news_data.get("title"),
                "By": news_data.get("by"),
                "URL": news_data.get("url")
            })
        else:
            raise HTTPException(status_code=news_response.status_code, detail=f"Failed to fetch News with ID {news_id}.")
    cache["top_news"] = top_news
    return top_news[:count]

@app.get("/top-news", tags=["Hacker News"])
def get_top_news(count: int = Query(10, ge=1, le=100)):
    try:
        return fetch_top_news(count)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
