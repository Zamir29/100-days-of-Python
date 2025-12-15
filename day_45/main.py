from bs4 import BeautifulSoup
import requests

def soup_training():
    with open("./website.html", "r", encoding="utf-8") as html:
        contents = html.read()
    soup = BeautifulSoup(contents, "html.parser")
    # print(soup.prettify())
    all_anchor_tags = soup.find_all(name="a")
    # print(all_anchor_tags)
    for anchor in all_anchor_tags:
        print(anchor.getText())
        print(anchor.get("href"))

    heading = soup.find(name="h1", id="name")
    print(heading)
    print(heading.getText())

    section_heading = soup.find(name="h3", class_="heading")
    print(section_heading)
    print(section_heading.getText())
    print(section_heading.get("class"))

    # Use CSS selector to target specific elements
    company_url = soup.select_one(selector="p a")
    print(company_url)

    headings = soup.select(".heading")
    print(headings)

def main_old():
    response = requests.get("https://news.ycombinator.com/news")
    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, "html.parser")
    page_title = soup.title.getText()
    # print(page_title)

    get_article = soup.find(name="span", class_="titleline")
    # print(get_article)
    article = get_article.select_one(selector=".titleline a")
    article_title = article.getText()
    article_link = article.get("href")

    get_article_score = soup.find(name="span", class_="score")
    article_score = get_article_score.getText()
    # print(article_score)

def get_score(soup,row) -> int:
    """ Safely extracts article score from ycombinator website or 0 if missing """
    try:
        row_id = row.get("id")
        # Assuming soup is available, not handling errors for soup here, out of scope
        article_score = soup.find(name="span", id=f"score_{row_id}")
        return int(article_score.getText().split()[0])
    except AttributeError:
        return 0

def main():
    response = requests.get("https://news.ycombinator.com/news")
    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, "html.parser")

    # Target specific rows
    get_rows = soup.find_all(name="tr", class_="athing submission")

    # # Create a list of dict with the articles scraped, but without list comprehension
    # all_articles = []
    # for row in get_rows:
    #     # Retrieving the article, link and the id
    #     row_article = row.select_one(".titleline a")
    #     article_title = row_article.getText()
    #     article_link = row_article.get("href")
    #
    #     # Not all id has a score, handling the AttributeError
    #     row_id = row.get("id")
    #     try:
    #         row_score = soup.find(name="span", id=f"score_{row_id}")
    #         article_score = int(row_score.getText().split()[0])
    #     except AttributeError:
    #         article_score = 0
    #
    #     # Populating the list of dict
    #     all_articles.append({"title": article_title, "link": article_link, "score": article_score})

    # This list comprehension is used with the get_score() function, hopefully it works
    all_articles = [
        {
            "title": row.select_one(".titleline a").getText(),
            "link": row.select_one(".titleline a").get("href"),
            "score": get_score(soup,row)}
        for row in get_rows
    ]

    # # First solution, not using dictionary comprehension
    # highest_score = {"index": 0, "score": 0}
    # for i in range(len(all_articles)):
    #     if all_articles[i]["score"] > highest_score["score"]:
    #         highest_score["score"] = all_articles[i]["score"]
    #         highest_score["index"] = i


    # print(highest_score)
    # print(all_articles[highest_score["index"]])

    index, article = max(enumerate(all_articles), key=lambda x: x[1]["score"])

    # print(index, article["score"])
    print(f"The article '{article['title']}' has the highest score of {article['score']} votes")

if __name__ == '__main__':
    main()
