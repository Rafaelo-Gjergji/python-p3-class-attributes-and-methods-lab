class Song:                          # This line defines a class named 'Song'
    count = 0                        # Class attribute: 'Count' keeps track of the total number of songs created
    genres = []                      # Class attribute: 'Genres' is a list that will contain unique genre names
    artists = []                     # Class attribute: 'Artists' is a list that will contain unique artist names
    genre_count = {}                 # Class attribute: 'Genre_count' is a dictionary that will store the count of songs for each genre
    artist_count = {}                # Class attribute: 'Artist_count' is a dictionary that will store the count of songs for each artist

    def __init__(self, name, artist, genre):  # '__init__' method is called when a new instance of the 'Song' class is created. it initializes
                                              # the object with the provided 'name', 'artist', and 'genre'
        self.name = name             # 'name' attributes of the current 'Song' object to the values passed as arguments to the __init__ method
        self.artist = artist         # 'artist' attributes of the current 'Song' object to the values passed as arguments to the __init__ method
        self.genre = genre           # 'genre' attributes of the current 'Song' object to the values passed as arguments to the __init__ method
        Song.add_song_to_count()     # Increments the total count of songs.
        self.add_artist_to_list()    # Adds the artist of the current song to the list of artists
        self.add_genre_to_list()     # Adds the genre of the current song to the list of genres
        self.add_to_genre_count()    # Updates the count of songs for the genre of the current song
        self.add_to_artist_count()   # Updates the count of songs for the artist of the current song

    @classmethod                     # Class method named 'add_song_to_count'. It increments the 'count' attribute of the 'Song' class by 1
    def add_song_to_count(cls):
        cls.count += 1

    def add_genre_to_list(self):     # This method adds the genre of the current song to the 'genres' list if it's not already present
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_artist_to_list(self):    # This method adds the artist of the current song to the 'artists' list if it's not already present
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    @classmethod                     # This class method adds a new genre to the 'genres' list if it's not already present
    def add_to_genres(cls, new_genre):
        if new_genre not in cls.genres:
            cls.genres.append(new_genre)

    @classmethod                     # This class method adds a new artist to the 'artists' list if it's not already present.
    def add_to_artists(cls, new_artist):
        if new_artist not in cls.artists:
            cls.artists.append(new_artist)

    def add_to_genre_count(self):    # This updates the 'genre_count' histogram by incrementing the count for the genre of the current song
        if self.genre not in Song.genre_count:
            Song.genre_count[self.genre] = 1
        else:
            Song.genre_count[self.genre] += 1

    def add_to_artist_count(self):   # This updates the 'artist_count' histogram by incrementing the count for the artist of the current song
        if self.artist not in Song.artist_count:
            Song.artist_count[self.artist] = 1
        else:
            Song.artist_count[self.artist] += 1
