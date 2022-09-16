"""Forms for playlist app."""

from turtle import title
from unicodedata import name
from wtforms import SelectField, StringField
from wtforms.validators import InputRequired, Optional
from flask_wtf import FlaskForm



class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Playlist Name", validators=[InputRequired()])
    description = StringField("Playlist Description", validators=[Optional()])


    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField("Song Title", validators=[InputRequired()])
    artist = StringField("Song Artist", validators=[InputRequired()])

    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
    
