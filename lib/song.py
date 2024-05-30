class Song:
    genres = set()
    artists = set()
    count = 0
    
    def __init__(self, name, artist , genre):   
    
      
      self.name = name
      self.artist = artist
      self.genre = genre
      Song.add_genre(genre)
      Song.add_artist(artist)
      Song.count +=1
      Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
      Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
    @classmethod
    def add_genre(cls, genre):
        cls.genres.add(genre)
    @classmethod
    def add_artist(cls, artist):
        cls.artists.add(artist)
   
