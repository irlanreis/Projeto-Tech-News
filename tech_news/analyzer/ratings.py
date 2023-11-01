from tech_news.database import db


# Requisito 10
def top_5_categories():
    categorys = db.news.find({}, {"category": True})
    categories_all = {}

    for category in categorys:
        if categories_all.get(category["category"]):
            categories_all[category["category"]] += 1
        else:
            categories_all[category["category"]] = 1

    categories_sorted = list(
        dict(
            sorted(
                categories_all.items(), key=lambda item: (-item[1], item[0])
            )
        ).keys()
    )

    return categories_sorted[:5]
