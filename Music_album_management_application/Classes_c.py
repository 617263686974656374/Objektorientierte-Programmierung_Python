from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QPlainTextEdit,QLabel,QHBoxLayout,QVBoxLayout, QDialog, QMainWindow, QStackedLayout, QComboBox, QMessageBox, QInputDialog
import json

class Album:
    def __init__(self, title, artist=None):
        self.title = title
        self.artist = artist
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def get_duration(self):
        total_duration = sum(song.duration for song in self.songs)
        total_duration = total_duration % (24 * 3600)
        hour = total_duration // 3600
        total_duration %= 3600
        minutes = total_duration // 60
        total_duration %= 60
        return "%d:%02d:%02d" % (hour, minutes, total_duration)


class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def get_duration(self):
        return f"{self.duration // 60}:{self.duration % 60:02}"


class MusicLibrary:
    def __init__(self):
        self.albums = []
        self.current_album = Album('')

    @staticmethod
    def save_albums_to_file(library):
        data = {"albums": []}

        for album in library.albums:
            songs = []
            for song in album.songs:
                songs.append({"title": song.title, "duration": song.duration})

            data["albums"].append({
                "title": album.title,
                "artist": album.artist,
                "songs": songs
            })

        with open("albums.json", "w") as file:
            json.dump(data, file)

    @staticmethod
    def load_albums_from_file():
        try:
            with open("albums.json", "r") as file:
                data = json.load(file)

            library = MusicLibrary()
            for album_data in data["albums"]:
                album = Album(album_data["title"], album_data["artist"])
                for song_data in album_data["songs"]:
                    song = Song(song_data["title"], song_data["duration"])
                    album.add_song(song)
                library.add_album(album)
            return library

        except FileNotFoundError:
            return MusicLibrary()

    def add_album(self, album):
        self.albums.append(album)

    def get_albums(self):
        return [album.title for album in self.albums]

    def get_one_album(self, album_name):
        for album in self.albums:
            if album.title == album_name:
                return album
        return False

    def set_current_album(self, album):
        self.current_album = album

    def add_song_to_current_album(self, song):
        if self.current_album:
            self.current_album.add_song(song)
        else:
            print("No album selected.")

    def display_one_album(self):
        print("Albums:")
        for album in self.albums:
            print(f"\t{album.title}")

    def display_album(self):
        print("Albums:")
        for i, album in enumerate(self.albums, start=1):
            print(f"{i}:  {album.title} ")

    def get_index(self, album_name):
        for i, album in enumerate(self.albums, start=0):
            if album.title == album_name:
                return i

    def remove_album(self, album_title):
        for album in self.albums:
            if album.title == album_title:
                self.albums.remove(album)
                print(f"Album '{album_title}'was deleted.")
                return
        print("Album not found.")

    def remove_song_from_album(self, album_title, song_title):
        for album in self.albums:
            if album.title == album_title:
                for song in album.songs:
                    if song.title == song_title:
                        album.remove_song(song)
                        print(f"Song '{song_title}' was deleted from the album '{album_title}'.")
                        return
                    else:
                        print("Song not found")
            else:
                print("Album not found.")
