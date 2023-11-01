# Requisito 1
import time
import requests
import parsel
from tech_news.database import create_news


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )

        if response.status_code != 200:
            return None
        return response.text

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = parsel.Selector(text=html_content)
    url = selector.css(".entry-preview .entry-title a::attr(href)").getall()

    return url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(text=html_content)
    page_next = selector.css(".nav-links .next::attr(href)").get()

    return page_next


# Requisito 4
def scrape_news(html_content):
    news_dict = {}
    selector = parsel.Selector(text=html_content)

    news_dict["url"] = selector.css(
        "head link[rel=canonical]::attr(href)"
    ).get()

    news_dict["title"] = (
        selector.css(".entry-title::text").get().strip(" \xa0")
    )
    news_dict["timestamp"] = selector.css(".meta-date::text").get()
    news_dict["writer"] = selector.css(".author a::text").get()

    news_dict["reading_time"] = int(
        selector.css(".meta-reading-time::text").re_first(r"\d+")
    )

    paragraph = selector.xpath("(//p)[1]//text()").getall()
    news_dict["summary"] = "".join(paragraph).strip(" \xa0")
    news_dict["category"] = selector.css(".meta-category .label::text").get()

    return news_dict


# Requisito 5
def get_tech_news(amount):
    response = fetch("https://blog.betrybe.com/")
    news_page = scrape_updates(response)
    all_pagesnews = []

    while len(all_pagesnews) < amount:
        for n in news_page:
            if len(all_pagesnews) < amount:
                response_news = fetch(n)
                data = scrape_news(response_news)
                all_pagesnews.append(data)

        response = fetch(scrape_next_page_link(response))
        news_page = scrape_updates(response)

    create_news(all_pagesnews)

    return all_pagesnews
