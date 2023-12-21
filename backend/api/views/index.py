#!/usr/bin/python3
""" Index """
from models.user import User
from models.post import Post
from models import storage
from api.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [User, Post]
    names = ["users", "posts"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)


@app_views.route('/', strict_slashes=False)
def top_arts():
    return jsonify(
        [
            {
                "name": "Tobi Oyekanmi",
                "caption": "Baddest art",
                "likes": 100,
                "media_link": "https://google.com",
                "art_page": "tbh"
            },
            {
                "name": "Tobi Oyekanmi",
                "caption": "Baddest art",
                "likes": 100,
                "media_link": "https://google.com",
                "art_page": "tbh"
            },
            {
                "name": "Tobi Oyekanmi",
                "caption": "Baddest art",
                "likes": 100,
                "media_link": "https://google.com",
                "art_page": "tbh"
            },
            {
                "name": "Tobi Oyekanmi",
                "caption": "Baddest art",
                "likes": 100,
                "media_link": "https://google.com",
                "art_page": "tbh"
            },
            {
                "name": "Tobi Oyekanmi",
                "caption": "Baddest art",
                "likes": 100,
                "media_link": "https://google.com",
                "art_page": "tbh"
            },
            {
                "name": "Tobi Oyekanmi",
                "caption": "Baddest art",
                "likes": 100,
                "media_link": "https://google.com",
                "art_page": "tbh"
            },
            {
                "name": "Tobi Oyekanmi",
                "caption": "Baddest art",
                "likes": 100,
                "media_link": "https://google.com",
                "art_page": "tbh"
            }
        ]
    )
