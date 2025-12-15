import requests
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

def main():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find_all(name="h3", class_="title")

    # To reverse the movies use the slice [::-1] or the reverse() object as list(reversed(movies))
    movies = [ row.getText().strip() for row in rows ]
    movies = movies[::-1] # Reverse with slicing

    # Take each movie and write it to the file
    with open("./movies.txt", "w", encoding="utf-8") as file:
        for movie in movies:
            file.write(movie + "\n")

    with open("./top10.txt", "w", encoding="utf-8") as file:
        for movie in movies[:10]:
            file.write(movie + "\n")

    print(len(movies))

if __name__ == "__main__":
    main()