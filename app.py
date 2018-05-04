import json
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


with open('Movies.json') as json_data:
    d = json.load(json_data)
    list_of_movies = []
    for data in d['movies']:
    	list_of_movies.append(data)


@app.route('/', methods =['GET'])
def test():
	return render_template("index.html")

@app.route('/movies', methods =['GET'])
def test1():
	return render_template("index.html",list_data=list_of_movies)

@app.route('/movies/<string:idd>', methods =['GET'])
def test2(idd):
	g = [movie for movie in list_of_movies if movie['id'] == idd]
	return render_template("index.html",list_data=g)

if __name__ == '__main__':
	 app.run(debug=True, host='0.0.0.0')