from bs4 import BeautifulSoup

def main():
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
if __name__ == '__main__':
    main()
