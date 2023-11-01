# Requisito 7
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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
