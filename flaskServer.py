from tmdbAPI import MovieData
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

movie_data = MovieData()
    
@app.route('/get_movie_info', methods=['POST'])
def get_movie_info():
    print("Request received.")
    data = request.get_json()
    title = data.get('title', '')
    

    movie_id = movie_data.getMovie(title)
    movie_budget = movie_data.getMovieBudget(movie_id)

    response =  jsonify({'title' : title, 'budget': movie_budget})
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')
    return response



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
