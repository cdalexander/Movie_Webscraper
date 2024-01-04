import requests

class IMDb_Scraper:
    def __init__(self):
        pass

    def get_media(self, title : str) -> str:
        """
        Args:
          title: the autocomplete title for a media (e.g. "game of thr")

        Returns: 
          str: the id for the selected media title

        Description: Gets the API id for the media title the user enters in order to query details from the API
        """
        url = "https://imdb8.p.rapidapi.com/auto-complete"
        querystring = {"q": title}
        headers = {
	        "X-RapidAPI-Key": "2d9d715c2fmshd7acab766d9cf86p10e08ajsn9ff19bc2402b",
	        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)

        title = (response.json()['d'][2]['l'])
        id = (response.json()['d'][2]['id'])

        return title, id


    # def get_media_details(self, media_details : dict) -> str:
    #     """
    #     Args: 
    #       id: the id for the media

    #     Returns:
    #       dict: a dictionary containing the media details

    #     Description: Gets the details for media using the API given a media id
    #     """
    #     title = (media_details['d'][2]['l'])
    #     id = (media_details['d'][2]['id'])

    #     print(one + "" + two)

    #     return 
    

# scraper = IMDb_Scraper()
# title, id = scraper.get_media("Game of Thrones")
# print(f"{title}\n{id}")
# scraper.get_media_details(myTitle)
