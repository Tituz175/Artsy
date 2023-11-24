#!/usr/bin/python3
""" Post """
from models.user import User
from models.post import Post
from models import storage
from api.v1.views import app_views
from flask import jsonify, request, make_response, abort

@app_views.route('/posts', methods=["GET"], strict_slashes=False)
def get_posts():
    all_posts = [post.to_dict() for post in storage.all(Post).values()]
    return jsonify(all_posts)

@app_views.route('/posts', methods=["POST"], strict_slashes=False)
def create_post():
    data = request.get_json()
    if data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'user_id' not in data:
        return make_response(jsonify({"error": "Missing user id"}), 400)
    user = storage.get(User, data.get("user_id"))
    if not user:
        abort(404)
    if 'title' not in data:
        return make_response(jsonify({"error": "Missing title"}), 400)
    if 'description' not in data:
        return make_response(jsonify({"error": "Missing description"}), 400)
    if 'media_link' not in data:
        return make_response(jsonify({"error": "Missing media link"}), 400)
    new_post = Post(**data)
    new_post.save()
    return jsonify(new_post.to_dict()), 201
