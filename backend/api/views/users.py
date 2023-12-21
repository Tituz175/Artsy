#!/usr/bin/python3
""" User """
from models.user import User
from models.post import Post
from models import storage
from api.views import app_views
from flask import jsonify, request, make_response, abort
from hashlib import md5


def serialize_to_json(obj):
    """
    Serializes the given object to a JSON-compatible dictionary representation.

    Args:
        obj: The object to be serialized.

    Returns:
        dict: A dictionary representing the object in a JSON-compatible format.
             Returns a 404 error response if the object is not found.
    """
    return obj.to_dict() if obj else abort(404)

@app_views.route('/signup', methods=['POST'], strict_slashes=False)
def signup():
    """Returns Successful status"""
    data = request.get_json()
    if data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    all_users = [user.to_dict() for user in storage.all(User).values()]
    for user in all_users:
        if data['email'] == user['email']:
            return jsonify({"message": "Existing account, signin pls"}), 200
    if 'first_name' not in data:
        return make_response(jsonify({"error": "Missing first name"}), 400)
    if 'last_name' not in data:
        return make_response(jsonify({"error": "Missing last name"}), 400)
    if 'email' not in data:
        return make_response(jsonify({"error": "Missing email"}), 400)
    if 'occupation' not in data:
        return make_response(jsonify({"error": "Missing occupation"}), 400)
    if 'password' not in data:
        return make_response(jsonify({"error": "Missing password"}), 400)
    if len(data['password']) < 8:
        return make_response(jsonify({"error": "Password less than 8"}), 400)
    new_user = User(**data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route("/signin", strict_slashes=False, methods=["POST"])
def signin_view():
    """Returns Successful status"""
    data = request.get_json()
    print(data)
    if data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'email' not in data:
        return make_response(jsonify({"error": "Missing email"}), 400)
    if 'password' not in data:
        return make_response(jsonify({"error": "Missing password"}), 400)
    all_users = [user.to_dict("signin") for user in storage.all(User).values()]
    if all_users is None:
        return jsonify({"user": None})
        abort(404)
    for user in all_users:
        if data['email'] == user['email'] and md5(data['password'].encode()).hexdigest() == user['password']:
            return jsonify(
                {
                    "first_name": user['first_name'],
                    "last_name": user['last_name'],
                    "email": user['email'],
                    "id": user['id']
                }
            ), 200
    return jsonify({"message": "No record"}), 200

@app_views.route("/users/<string:user_id>", strict_slashes=False, methods=["GET"])
def get_user(user_id):
    """
    Retrieves a specific user by ID and returns a JSON response.

    Args:
        user_id (string): The ID of the user to retrieve.

    Returns:
        Response: A JSON response containing the details of the specified user.
    """
    return jsonify(serialize_to_json(storage.get(User, user_id)))


