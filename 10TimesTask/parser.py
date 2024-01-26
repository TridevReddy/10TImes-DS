# parser.py
from tasks import process_rss_feed


if __name__ == '__main__':
    # Example RSS feed URL, replace with your actual feed URLs
    rss_feeds = [
        "http://rss.cnn.com/rss/cnn_topstories.rss",
        "http://qz.com/feed",
        "http://feeds.foxnews.com/foxnews/politics",
        "http://feeds.reuters.com/reuters/businessNews",
        "http://feeds.feedburner.com/NewshourWorld",
        "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
    ]

    for feed_url in rss_feeds:
        process_rss_feed.delay(feed_url)
