from bs4 import BeautifulSoup
import requests
import random

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


def get_top_movies():
    url = URL
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # If request fails
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None  # If request fails

    web_page = response.text
    soup = BeautifulSoup(web_page, "html.parser")

    movie_tags = soup.find_all(name="div", class_="article-title-description__text")

    if not movie_tags:
        print(
            "No movies found. The webpage has been restructured please leave an issue on the repo"
        )
    all_movies = [
        tag.find(name="h3").get_text(strip=True) for tag in movie_tags if tag.find("h3")
    ]

    return all_movies if all_movies else None


def get_random_movie():
    movies = get_top_movies()
    if movies:
        return random.choice(movies)
    return "no movies available."


if __name__ == "__main__":
    movie = get_random_movie()
    print(movie)
