def make_album(musician_name, album_name, music_num=0-1):
    album = {}
    album['musician_name'] = musician_name
    album['album_name'] = album_name
    if music_num != -1:
        album['music_num'] = music_num
    return album

def main():
    album1 = make_album('Aimer Neige', 'No Title', 0)
    print(album1)
    album2 = make_album('Monika', 'Your reality')
    print(album2)

if __name__ == '__main__':
    main()