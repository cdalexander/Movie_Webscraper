import requests

url = "https://imdb8.p.rapidapi.com/title/get-details"

querystring = {"tconst":"tt0944947"}

headers = {
	"X-RapidAPI-Key": "2d9d715c2fmshd7acab766d9cf86p10e08ajsn9ff19bc2402b",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

