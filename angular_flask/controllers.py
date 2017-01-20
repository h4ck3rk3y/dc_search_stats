import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort
from flask import jsonify

from angular_flask import app

from db_connection import searches

from random import randint

# routing for API endpoints, generated from the models designated as API_MODELS
from angular_flask.core import api_manager

# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/about')
@app.route('/blog')
@app.route('/search')
@app.route('/user')
@app.route('/user/<user_name>')
@app.route('/userslist')
@app.route('/random')
def basic_pages(**kwargs):
    return make_response(open('angular_flask/templates/index.html').read())

@app.route('/api/search/random')
def search_random():
    count = searches.count()
    random_number = randint(0, count-1)
    search = searches.find().limit(-1).skip(random_number).next()
    search = {'user': search['user'], 'created_on': search['on'], 'query': search['query'], 'status': 'success'}
    return jsonify(**search)

@app.route('/api/search')
def search():
    search = searches.find().sort([("_id", -1)])[0]
    search = {'user': search['user'], 'created_on': search['on'], 'query': search['query'], 'status': 'success'}
    return jsonify(**search)

@app.route('/api/search/<user_name>')
@app.route('/api/search/<user_name>/<limit>')
def user_search(user_name, limit=10):
    user_searches = searches.find({'user': user_name}).sort([("_id", -1)]).limit(limit)
    result = {'searches': []}
    result['user']= user_name
    for search in user_searches:
        result['searches'].append({'query': search['query'], 'created_on': search['on']})

    result['count'] = len(result['searches'])
    result['status'] = 'success'
    return jsonify(**result)

@app.route('/api/users')
@app.route('/api/users/<limit>')
def user_list(limit=False):
    user_list = searches.distinct("user")
    if limit:
        try:
            user_list = user_list[:int(limit)]
        except:
            pass
    result = {}
    result['users'] = sorted(user_list, reverse=True)
    result['count'] = len(result['users'])
    result['status'] = 'success'
    return jsonify(**result)

# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
