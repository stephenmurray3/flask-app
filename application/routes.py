# Creation of a route
from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacter

def format_character(character):
    return {
        "id": character.id,
        "name": character.name,
        "age": character.age,
        "catch_phrase": character.catch_phrase
    }

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# POST route
@app.route("/characters", methods=['POST'])
def create_character():
    # retrieve the body - req.body
    data = request.json
    # data -> {name: , age: , etc.}
    character = FriendsCharacter(data['name'], data['age'], data['catch_phrase'])
    # add the character -> add character in a temporary queue
    db.session.add(character)
    # commit -> send the character to the database
    db.session.commit()
    # send back a JSON response
    # jsonify -> turns JSON output into a Response object
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

# GET route to retrieve all the characters
@app.route("/characters")
def get_characters():
    characters = FriendsCharacter.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))
    return {'characters': character_list}

# GET route to retrieve character by id
@app.route("/characters/<id>")
def get_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

# DELETE route to delete character by id
@app.route("/characters/<id>", methods=["DELETE"])
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return "Character Deleted"

# PATCH method to update character by id
@app.route("/characters/<id>", methods=["PATCH"])
def update_character(id):
    character = FriendsCharacter.query.filter_by(id=id)
    data = request.json
    character.update(dict(name=data['name'], age=data['age'], catch_phrase=data['catch_phrase']))
    # Commit the change to the database
    db.session.commit()
    # Retrieve the specific character from the filtering
    updatedCharacter = character.first()
    # Return a JSON object of the updated character
    return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)
