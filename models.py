"""Models for Playlist app."""

from turtle import title
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Playlist(db.Model):
  """Playlist."""

  __tablename__ = 'playlists'

  id = db.Column(
      db.Integer, 
      nullable=False,
      primary_key=True,
      autoincrement=True
  )

  name = db.Column(
    db.String, 
    nullable=False
  )

  description = db.Column(
      db.String, 
      nullable=False
  )

  def __init__(self, name, description):
    self.name = name
    self.description = description

  assignments = db.relationship('PlaylistSong',
                                backref='playlists')

    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
  """Song."""

  __tablename__ = 'songs'
  id = db.Column(
      db.Integer, 
      nullable=False,
      primary_key=True,
      autoincrement=True
  )
  title = db.Column(
      db.String, 
      nullable=False
  )

  artist = db.Column(
      db.String, 
      nullable=False
  )

  def __init__(self, title, artist):
    self.title = title
    self.artist = artist
  
  
  assignments = db.relationship('PlaylistSong',
                                backref='songs')

  playlists = db.relationship('Playlist',
                             secondary='playlists_songs',
                             backref='songs')
                    
    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
  """Mapping of a playlist to a song."""
  __tablename__ = 'playlists_songs'

  id = db.Column(
      db.Integer, 
      nullable=False, 
      primary_key=True, 
      autoincrement=True
  )

  playlist_id = db.Column(
      db.Integer, 
      db.ForeignKey("playlists.id"), 
      primary_key=True
  )

  song_id = db.Column(
      db.Integer, 
      db.ForeignKey("songs.id"), 
      primary_key=True
  )

  def __init__(self, playlist_id, song_id):
    self.playlist_id = playlist_id
    self.song_id = song_id

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
  """Connect to database."""

  db.app = app
  db.init_app(app)
