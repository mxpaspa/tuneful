import os.path
import json

from flask import request, Response, url_for, send_from_directory
from werkzeug.utils import secure_filename
from jsonschema import validate, ValidationError

from . import models
from . import decorators
from tuneful import app
from .database import session
from .utils import upload_path

song_schema ={
    "file": {
        "id": 7
    }
}

@app.route("/api/songs", methods=["GET"])
@decorators.accept("application/json")
def posts_get():
    """ Get a list of songs """
    

    # Get and filter the posts from the database
    songs = session.query(models.Song).all()
   
    # Convert the posts to JSON and return a response
    data = json.dumps([song.as_dictionary() for song in songs])
    return Response(data, 200, mimetype="application/json")

@app.route("/api/songs", methods=["POST"])
@decorators.accept("application/json")
@decorators.require("application/json")

def post_song():
    data = request.json
    
     # check that the JSON supplied is valid
    # if not return a 422 Unprocessable Entity
    
    try: 
        validate(data, song_schema)
    except ValidationError as error:
        data = {"message": error.message}
        return Response(json.dumps(data), 422, mimetype="application/json")
        
    #add the song to the database 
    song = models.Song(song_file_id=data["file"]["id"])
    session.add(song)
    session.commit()
        
    # return a 201 Created, containing the post as JSON and with the
    # location header set to the location of the post
    data = json.dumps(song.as_dictionary())
    headers = {"Location": url_for("get_songs", id=song.id)}
    return Response(json.dumps(data), 200, headers=headers, mimetype="application/json")
    
@app.route("/api/songs/<int:id>", methods=["PUT"])
@decorators.accept("application/json")
@decorators.require("application/json")

def edit_song():

 # check if the song exists, if not return a 404 with a helpful message
    song = session.query(models.Song).get(id)
    if not song:
        message = "Could not find song with id {}".format(id)
        data = json.dumps({"message": message})
        return Response(data, 404, mimetype="application/json")
        
    data = request.json

    # check that the JSON supplied is valid
    # if not, return a 422 Unprocessable Entity
    try:
        validate(data, song_schema)
    except ValidationError as error:
        data = {"message": error.message}
        return Response(json.dumps(data), 422, mimetype="application/json")
        
    song = data[""]
    session.commit()
    # return an OK 200, containing the song as JSON with the
    # location header set to the location of the post
    data = json.dumps(song.as_dictionary())
    headers = {"Location": url_for("post_get", id=song.id)}
    return Response(
        data, 200, headers=headers,
        mimetype="application/json"
    )
    
@app.route("/api/songs/<int:id>", methods=["DELETE"])
@decorators.accept("application/json")
def delete_song(id):
    """ Delete a single song """
    # check if the song exists, if not return a 404 with a helpful message
    song = session.query(models.Song).get(id)
    if not song:
        message = "Could not find song with id {}".format(id)
        data = json.dumps({"message": message})
        return Response(data, 404, mimetype="application/json")
        
        session.delete(song)
        session.commit
        
        message = "deleted song {}".format(id)
        data = json.dumps({"message": message})
        return Response(data, 404, mimetype="application/json")
    