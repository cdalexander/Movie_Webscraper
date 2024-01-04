from webScraper import IMDb_Scraper
from flask import Flask, request, jsonify

# scraper = IMDb_Scraper()
# media = input("Please enter a movie or TV show: ")
# title, id = scraper.get_media(media)
# print(f"{title}\n{id}")

app = Flask(__name__)
imdb_scraper = IMDb_Scraper()
from flask_cors import CORS

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:8080"}})
    
@app.route('/get_movie_info', methods=['POST'])
def get_movie_info():
    print("Request received.")
    data = request.get_json()
    title = data.get('title', '')
    movie_title, movie_id = imdb_scraper.get_media(title)
    

    if title:
        return jsonify({'title': movie_title, 'id': movie_id})
    else:
        return jsonify({'error': 'Title not provided'}), 400

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
