from reports import *
from printing import *


def main():
    print("Hi Judy!")
    file_name = input("Enter the name of the file you want to use: ")
    f = open("answers.txt", "w")
    print_count_games(file_name)
    f.write("How many games are in the file?    {}\n".format(count_games(file_name)))
    year = int(input("Enter the year you are interested in: "))
    print_decide(file_name, year)
    f.write("Is there a game from the given year?    {}\n".format(decide(file_name, year)))
    print_get_latest(file_name)
    f.write("Which was the latest game?    {}\n".format(get_latest(file_name)))
    genre = str(input("Enter the genre you are interested in: "))
    print_count_by_genre(file_name, genre)
    f.write("How many games do we have by genre?    {}\n".format(count_by_genre(file_name, genre)))
    title = str(input("Enter the name of the game that you want to know the position of: "))
    print_get_line_number_by_title(file_name, title)
    f.write("What is the line number of the given game?    {}\n".format(get_line_number_by_title(file_name, title)))
    print_get_genres(file_name)
    f.write("What are the genres?    {}\n".format(get_genres(file_name)))
    print_when_was_top_sold_fps(file_name)
    f.write("What is the release date of the top sold 'FPS' game?    {}\n".format(when_was_top_sold_fps(file_name)))
    f.close()
    print("Your answers are ready in the 'answers.txt' file.\nBye Judy!")

if __name__ == '__main__':
    main()
