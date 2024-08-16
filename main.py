from fastapi import FastAPI, HTTPException, Query
import requests
import cachetools
import logging
from fastapi.responses import HTMLResponse



app = FastAPI()

news_api = "https://hacker-news.firebaseio.com/v0"
cache_time = 600 
cache = cachetools.TTLCache(maxsize=100, ttl=cache_time)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

@app.get("/", response_class=HTMLResponse, tags=["Home Page"])
def read_root():
    return """
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <p>Visit this URL to access the API documentation: <a href="http://0.0.0.0:8000/docs">http://0.0.0.0:8000/docs</a></p>
        </body>
    </html>
    """

def fetch_top_news(count: int):
    cached_data = cache.get("top_news")
    if cached_data:
        logger.info(f"Returning {len(cached_data)} cached news.")
        return cached_data[:count]
    logger.info(f"Fetching top {count} news from Hacker News.")
    top_news_url = f"{news_api}/topstories.json"
    response = requests.get(top_news_url)

    if response.status_code != 200:
        logger.error(f"Failed to fetch top news: {response.status_code}")
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
            logger.info(f"Fetched News: {news_data.get('title')}")
        else:
            logger.error(f"Failed to fetch news with ID {news_id}: {news_response.status_code}")
            raise HTTPException(status_code=news_response.status_code, detail=f"Failed to fetch News with ID {news_id}.")
    cache["top_news"] = top_news
    logger.info("News cached successfully.")
    return top_news[:count]

@app.get("/top-news", tags=["Hacker News"])
def get_top_news(count: int = Query(10, ge=1, le=100)):
    logger.info(f"Received request for top {count} news.")
    try:
        return fetch_top_news(count)
    except Exception as ex:
        logger.error(f"An error occurred: {str(ex)}")
        raise HTTPException(status_code=500, detail=str(ex))
