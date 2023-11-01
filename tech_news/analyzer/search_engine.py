# Requisito 7
from datetime import datetime
from tech_news.database import db


def search_by_title(title):
    title = db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
        {"title": True, "url": True},
    )

    news_return = []
    for n in title:
        news_return.append((n["title"], n["url"]))

    return news_return


# Requisito 8
def search_by_date(date):
    try:
        format_date = datetime.strptime(date, "%Y-%m-%d")
        news_date = db.news.find(
            {"timestamp": datetime.strftime(format_date, "%d/%m/%Y")},
            {"title": True, "url": True},
        )

        news_return = []
        for n in news_date:
            news_return.append((n["title"], n["url"]))

        return news_return
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    news_category = db.news.find(
        {"category": {"$regex": category, "$options": "i"}},
        {"title": True, "url": True},
    )

    news_return = []
    for n in news_category:
        news_return.append((n["title"], n["url"]))

    return news_return
