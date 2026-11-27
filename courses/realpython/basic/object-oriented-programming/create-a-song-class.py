"""
Create a Song class that represents a song with a title, an artist, and a duration.

Your Song class should have:

A class attribute called category set to "music"
An .__init__() method that accepts title, artist, and duration (an integer representing seconds)
Each argument stored as an instance attribute with the same name

Examples
song = Song("Imagine", "John Lennon", 187)
song.title => 'Imagine'
song.artist =>'John Lennon'
song.duration => 187
song.category => 'music'
Song.category =>'music'

Requirements
The class must be named Song
category must be a class attribute defined in the class body, not inside .__init__()
.__init__() must accept title, artist, and duration
All three arguments must be stored as instance attributes
"""

class Song:
    """Represents a song with a title, artist, and duration."""
    ...
    category = 'music'
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration