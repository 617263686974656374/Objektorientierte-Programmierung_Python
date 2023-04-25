from KMS_1_03_LE_01_04_Code import *

library = MusicLibrary("My Music Library")
library.load()
while True:
    # Choice 1: New Album or existing Album or show all
    # Choice 2: Add Song, Delete Song, Show Details, Delete Album
    print("\nMain Menu\n"
          "--------------\n"
          "1. Display Albums\n"
          "2. View or edit Album\n"
          "3. Add new Album\n"
          "4. Save and Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"\nAlbums in {library.name}")
        library.display_albums()
    elif choice == 2:
        album_name = input("Enter album name: ")
        album = next((a for a in library.albums if a.name == album_name), None)
        if album:
            while True:
                try:
                    album_choice = int(input(f"\n{album_name}\n"
                                             f"---------------\n"
                                             f"1. Display Songs\n"
                                             f"2. Add Song\n"
                                             f"3. Remove Song\n"
                                             f"4. Remove Album from {library.name}\n"
                                             f"5. Return to Main Menu\n"
                                             f"Enter your choice: "))
                    if album_choice == 1:
                        library.display_songs(album_name)
                    elif album_choice == 2:
                        title = input("Enter song title: ")
                        while True:
                            length = input("Enter song length (mm:ss): ")
                            try:
                                lst_len = length.split(":")
                                if 0 <= int(lst_len[0]) < 60 and 0 <= int(lst_len[1]) < 60 or len(lst_len) != 2:
                                    break
                                else:
                                    print("\nInvalid input.\n")
                            except:
                                print("\nInvalid input.\n")
                        album.add_song(title, length)
                    elif album_choice == 3:
                        title = input("Enter song title: ")
                        album.remove_song(title)
                    elif album_choice == 4:
                        library.remove_album(album_name)
                    elif album_choice == 5:
                        break
                except:
                    print("Invalid choice.")
        else:
            print(f"Album '{album_name}' not found.")
    elif choice == 3:
        album_name = input("Enter album name: ")
        artist = input("Enter artist name: ")
        library.add_album(Album(album_name, artist))
    elif choice == 4:
        album01 = Album("Thriller", "Michael Jackson")
        library.save()
        break
    else:
        print("\nInvalid choice.")
library.save()
