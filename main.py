from player import storage
from player.playlist_manager import PlaylistManager
from player.music_player import MusicPlayer


def print_menu():
    print("\n=== MUSIC PLAYER MENU ===")
    print("1. Add Song")
    print("2. Remove Song")
    print("3. Search Songs")
    print("4. List All Songs")
    print("5. Play Song")
    print("6. Pause")
    print("7. Stop")
    print("8. Exit")


def main():
    manager = PlaylistManager(storage)
    player = MusicPlayer(manager)

    while True:
        print_menu()
        choice = input("Choose option: ")

        if choice == "1":
            title = input("Song title: ")
            artist = input("Artist: ")
            duration = int(input("Duration (seconds): "))

            try:
                result = manager.add_song(title, artist, duration)
                print("Song added:", result)
            except Exception as e:
                print("Error:", str(e))

        elif choice == "2":
            song_id = int(input("Enter song ID to remove: "))
            if manager.remove_song(song_id):
                print("Song removed.")
            else:
                print("Song not found.")

        elif choice == "3":
            query = input("Search: ")
            results = manager.search(query)
            for s in results:
                print(s)

        elif choice == "4":
            for s in manager.list_songs():
                print(s)

        elif choice == "5":
            sid = int(input("Song ID to play: "))
            print(player.play(sid))

        elif choice == "6":
            print(player.pause())

        elif choice == "7":
            print(player.stop())

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()


