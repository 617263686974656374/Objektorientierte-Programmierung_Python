import os
import json


class Album:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.songs = []

    def add_song(self, title, length):
        self.songs.append({'title': title, 'length': length})

    def remove_song(self, title):
        for i, song in enumerate(self.songs):
            if song['title'] == title:
                self.songs.pop(i)
                break

    def full_length(self):
        total = sum(int(song['length'].split(':')[0]) * 60 + int(song['length'].split(':')[1]) for song in self.songs)
        minutes = total // 60
        seconds = total % 60
        return f"{minutes}:{seconds:02d}"


class MusicLibrary:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.file_name = f"{self.name.lower().replace(' ', '_')}.json"

    def add_album(self, album):
        self.albums.append(album)

    def remove_album(self, album_name):
        for i, album in enumerate(self.albums):
            if album.name == album_name:
                self.albums.pop(i)
                break

    def display_albums(self):
        for i, album in enumerate(self.albums, 1):
            print(f"{i}. {album.name} by {album.artist} [{album.full_length()}]")

    def display_songs(self, album_name):
        album = next((a for a in self.albums if a.name == album_name), None)
        if album:
            print(f"\nSongs in {album.name}  [{album.full_length()}]:")
            for i, song in enumerate(album.songs, 1):
                print(f"{i}. {song['title']} ({song['length']})")
        else:
            print(f"Album '{album_name}' not found.")

    def save(self):
        data = [
            {
                'name': album.name,
                'artist': album.artist,
                'songs': album.songs
            } for album in self.albums
        ]
        with open(self.file_name, 'w') as f:
            json.dump(data, f)

    def load(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as f:
                # Nice!
                data = json.load(f)
            self.albums = [
                Album(album['name'], album['artist']) for album in data
            ]
            for i, album in enumerate(self.albums):
                album.songs = data[i]['songs']
        else:
            print(f"No saved data found for library '{self.name}'.")
