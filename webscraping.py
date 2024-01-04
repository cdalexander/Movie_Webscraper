# from flask import Flask, request, jsonify
# from bs4 import BeautifulSoup
# import requests
# import json
# import requests

# app = Flask(__name__)

# @app.route("/scrape", methods=["POST"])

# def scrape_movie():
#     data = request.get_json()
#     title = data["title"]

#     url = "https://imdb8.p.rapidapi.com/title/get-details"

#     querystring = {"tconst":"tt0944947"}

#     headers = {
#         "X-RapidAPI-Key": "2d9d715c2fmshd7acab766d9cf86p10e08ajsn9ff19bc2402b",
#         "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     movie_details = response.json()

#     return jsonify(movie_details)

# if __name__ == "__main__":
#     app.run(dubug = True)





from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
CORS(app, resources={r"/get_movie_details": {"origins": "http://127.0.0.1:8080"}})

@app.route('/get_movie_details', methods=['GET'])
def get_movie_details():
    try:
        title = request.args.get('title')
        url = "https://imdb8.p.rapidapi.com/title/get-details"
        querystring = {"tconst": "tt0944947"}

        headers = {
            "X-RapidAPI-Key": "2d9d715c2fmshd7acab766d9cf86p10e08ajsn9ff19bc2402b",
            "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        #HTTPErro for bad responses
        response.raise_for_status() 


        print("RapidAPI Response:", response.text)
        print("RapidAPI Response Length:", len(response.text))
        print("RapidAPI Response Status Code:", response.status_code)
        print("RapidAPI Response Content-Type:", response.headers.get('Content-Type'))
        print("RapidAPI Response Decoded:", response.content.decode('utf-8'))
        
        if response.status_code == 204:
            return jsonify({"message": "No content available"}), 204

        try: 
            return jsonify(response.json())
        except ValueError as ve:
            print(f"Error parsing JSON: {ve}")
            return jsonify({"error": "Invalid JSON in response"}), 500


    except Exception as e:
        # print or log the exception traceback during development
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
