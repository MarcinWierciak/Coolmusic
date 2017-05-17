import csv
import sys
import random


def new_album():
    writer = open("music.csv", "a")
    writer.seek(0,2)
    new_artist = input("Artist: ")
    new_album = input("Album: ")
    new_year = input("Year of an album (YYYY): ")
    new_genre = input("Genre of music: ")
    new_length = input("Length of an album (MM:SS): ")
    writer.writelines((" | ").join([new_artist, new_album, new_year, new_genre, new_length + "\n"]))
    print("\nNew album has been added!")
    music_file = open("music.csv", "r+")
    return music_file

def albums_by_artist(name, artist):
    artist_input = input("Enter an artist: ")
    for text in name:
        if artist_input in artist:
            if artist_input in text:
                print("\n" + " - ".join(text))
        else:
            print("\nThere is no artist '" + artist_input + "', \ntry again.")
            break

def albums_by_year(name, year):
        year_input = input("Enter a year: ")
        year_info = list(zip(year, name))
        for text in year_info:
            try:
                if int(year_input) in year:
                    if int(year_input) in text:
                        print("\n" + " - ".join(text[1]))
                else:
                    print("\nThere are no albums from year '" + year_input + "', \ntry again.")
                    break
            except ValueError:
                print("\n E-E. Enter a year in format [YYYY], \n try again.")
                break

def artist_by_album(name, album):
    album_input = input("Enter an album: ")
    for text in name:
        if album_input in album:
            if album_input in text:
                print("\n" + text[1] + " - " + text[0])
        else:
            print("\nThere is no album '" + album_input + "', \ntry again.")
            break

def albums_by_letters(name, album):
    letters_input = input("Enter a/some letter(s), [size matters]: ")
    x = 0
    for text_1 in album:
        if letters_input in text_1:
            x = x + 1
            for text_2 in name:
               if text_1 in text_2:
                    print("\n" + " - ".join(text_2))
    if x == 0:
        print("\nThere are no albums with letter(s) '" + letters_input + "', \ntry again.")

def albums_by_genre(name, genre):
    genre_input = input("Enter a genre: ")
    genre_name = list(zip(genre, name))
    for text in genre_name:
        if genre_input in genre:
            if genre_input in text:
                print("\n" + " - ".join(text[1]))
        else:
            print("\nThere are no music with genre '" + genre_input + "', \ntry again.")
            break

def total_age(year):
    total_age = 2017*len(year) - sum(year)
    print("\nAll albums are " + str(total_age) + " years old.")

def random_album_by_genre(name, genre):
    genre_random_input = input("Enter a genre: ")
    genre_name = list(zip(genre, name))
    random_album = []
    if genre_random_input in genre:
        for text in genre_name:
            if genre_random_input in text:
                random_album.append(text)
        random_final = random.choice(random_album)
        print("\n" +" - ".join(random_final[1]))
    else:
        print("\nThere are no music with genre '" + genre_random_input + "', \ntry again.")

def amount_of_albums_by_artist(name):
    albums_by_artist_input = input("Enter an artist: ")
    amount = 0
    for text in name:
        if albums_by_artist_input in text:
            amount = amount + 1
    print("\nThere are " + str(amount) + " album(s) by " + albums_by_artist_input + ".")

def the_highest_length(length, album, name, artist):
    length_in_number = list(int(numb.replace(":","")) for numb in length)
    name_length = list(zip(length_in_number, album, artist, length))
    maximum = length_in_number[0]
    for time in length_in_number:
        if maximum < time:
            maximum = time
    for text in name_length:
        if maximum in text:
            print("\nThe longest-time album is:\n","".join(text[2]),"-","".join(text[1]),"(" + "".join(text[3]) + ")")

def main():
    with open("music.csv", "r") as music_file:
        artist = list(row.split(" | ")[0] for row in music_file)
    with open("music.csv", "r") as music_file:
        album = list(row.split(" | ")[1] for row in music_file)
    with open("music.csv", "r") as music_file:
        year = list(int(row.split(" | ")[2]) for row in music_file)
    with open("music.csv", "r") as music_file:
        genre = list(row.split(" | ")[3] for row in music_file)
    with open("music.csv", "r") as music_file:
        length = list(row.split(" | ")[4].replace("\n", "") for row in music_file)
    print("\nWelcome to CoolMusic!")
    while True:
        print("\n1) Add new album\n2) Find albums by artist\n3) Find albums by year\n4) Find musician by album\n5) Find albums by letter(s)")
        print("6) Find albums by genre\n7) Calculate the age of all albums\n8) Choose a random album by genre\n9) Show the amount of albums by an artist\n10) Find the longest-time album\n0) Exit")
        menu_key = input("\nEnter a menu key: ")
        menu_keys_list = ["1","2","3","4","5","6","7","8","9","0","10"]
        name = tuple(zip(artist,album))
        info = tuple(zip(year,genre,length))
        music = list(zip(name,info))
        if menu_key in menu_keys_list:
            if menu_key == "1":
                new_album()
                with open("music.csv", "r") as music_file:
                    artist = list(row.split(" | ")[0] for row in music_file)
                with open("music.csv", "r") as music_file:
                    album = list(row.split(" | ")[1] for row in music_file)
                with open("music.csv", "r") as music_file:
                    year = list(int(row.split(" | ")[2]) for row in music_file)
                with open("music.csv", "r") as music_file:
                    genre = list(row.split(" | ")[3] for row in music_file)
                with open("music.csv", "r") as music_file:
                    length = list(row.split(" | ")[4].replace("\n", "") for row in music_file)
            if menu_key == "2":
                albums_by_artist(name, artist)
            if menu_key == "3":
                albums_by_year(name, year)
            if menu_key == "4":
                artist_by_album(name, album)
            if menu_key == "5":
                albums_by_letters(name, album)
            if menu_key == "6":
                albums_by_genre(name, genre)
            if menu_key == "7":
                total_age(year)
            if menu_key == "8":
                random_album_by_genre(name, genre)
            if menu_key == "9":
                amount_of_albums_by_artist(name)
            if menu_key == "10":
                the_highest_length(length, album, name, artist)
            if menu_key == "0":
                print("\nBye-Bye.\n")
                sys.exit()
        else:
            print("\n E-E!\n Enter a NUMBER from 0 to 10, and press Enter.")


if __name__ == "__main__":
    main()
