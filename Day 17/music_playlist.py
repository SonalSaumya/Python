

# def add():
#     names = input("Enter names of songs : ")
#     list((names.split(",")))
#
# add()
# print(songs)


song_titles = []
def add_songs():
    songs = input("Enter song_titles: ")
    song_titles.extend([songs.strip() for songs in songs.split(",")])
    print(f"Songs added: {songs}")

def remove_song():
    song = input("Enter the song title to remove: ")
    if song in song_titles:
        song_titles.remove(song)

    print (f"Song {song} not found in the song_titles.")

def view_songs():
    if song_titles:
        print("Song_titles:", ",".join(song_titles))
    else:
        print("The song_titles is empty.")

def slice_playlist():
    start = int(input("Enter the start index: "))
    end = int(input("Enter the end index: "))
    if 0<= start < len(song_titles) and 0 <= end <= len(song_titles):
        print("Sliced playlist: ", song_titles[start:end])
    else:
        print("Invalid Indices. ")

while True:
    print("\nOptions: \n1. Add Songs \n2. Remove Song \n3. View All Songs \n4. Slice Playlist \n5 Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_songs()
    elif choice == '2':
        remove_song()
    elif choice == '3':
        view_songs()
    elif choice== '4':
        slice_playlist()
    elif choice== '5':
        print("Existing.")
        break
    else:
        print ("Invalid option, try again.")