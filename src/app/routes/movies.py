import os

from flask import Blueprint
from flask.json import jsonify
from flask import request
import json
import requests

movies = Blueprint('movies', __name__)  # pylint: disable=C0103
API_KEY = os.environ['API_KEY']

IMG_URL_PATH = "http://image.tmdb.org/t/p/w500"

@movies.route('search', methods=['GET'])
def get_movies():
    genre = {}
    query_parameters = dict(request.args)
    query_parameters['api_key'] = API_KEY
    response = requests.get('https://api.themoviedb.org/3/genre/movie/list', params=query_parameters)
    json_response = response.json()
    for items in json_response.get("genres"):
        genre[items['id']] = items['name']
    sort_by = query_parameters['sort_by']
    if "," in sort_by:
        sort_by = query_parameters['sort_by'].split(",")
    isreverse= True if query_parameters['reverse'].lower() == 'true' else False
    response = requests.get('https://api.themoviedb.org/3/search/movie', params=query_parameters)
    json_response = response.json()
    for index, items in enumerate(json_response["results"]):
        genre_list = list()
        for genre_id in items.get("genre_ids"):
            genre_list.append(genre.get(genre_id))
        items['genre_names'] = genre_list
        del items['genre_ids']
        json_response['results'][index] = items
        if items.get("backdrop_path"):
            items['backdrop_path'] = IMG_URL_PATH + items['backdrop_path']
        if items.get("poster_path"):
            items['poster_path'] = IMG_URL_PATH + items['poster_path']

    if isinstance(sort_by, list):
        json_response['results'] = sorted(json_response['results'],key=lambda i: (i[sort_by[0]],i[sort_by[1]]), reverse=isreverse)
    else:
        json_response['results'] = sorted(json_response['results'], key=lambda i: i[sort_by],
                                              reverse=isreverse)
    return json_response

@movies.route('<string:movie_id>/details', methods=['GET'])
def get_movie(movie_id):
    query_parameters = dict(request.args)
    query_parameters['api_key'] = API_KEY
    response = requests.get('https://api.themoviedb.org/3/movie/{}'.format(movie_id), params=query_parameters)
    json_response = response.json()
    json_response['belongs_to_collection']['poster_path']= IMG_URL_PATH + json_response["poster_path"]
    json_response['belongs_to_collection']['backdrop_path'] = IMG_URL_PATH + json_response["backdrop_path"]
    if json_response.get("poster_path"):
        json_response["poster_path"] = IMG_URL_PATH + json_response["poster_path"]
    return jsonify(json_response)


@movies.route('<string:movie_id>/ratings/', methods=['POST'])
def rate_movie(movie_id):
    query_parameters = dict(request.args)
    query_parameters['api_key'] = API_KEY
    if not request.data:
        return {"Failure": {"message": "Rating is not available! Please provide Rating."},"Status": 400}
    try:
        body = json.loads(request.data.decode('utf-8'))
    except Exception as ex:
        return {'Failure': {"message":str(ex)}, "status": 400}

    if not query_parameters.get("guest_session_id"):
        response = requests.get('https://api.themoviedb.org/3/authentication/guest_session/new', params=query_parameters)
        json_response = response.json()
        query_parameters["guest_session_id"] = json_response.get("guest_session_id")
    result = requests.post(f'https://api.themoviedb.org/3/movie/{movie_id}/rating', params=query_parameters, data=body)
    return result.json()

