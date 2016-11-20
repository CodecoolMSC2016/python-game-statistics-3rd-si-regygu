from reports import *
from printing import *


def main():
    print("Hi Judy!")
    file_name = input("Enter the name of the file you want to use: ")
    f = open("answers.txt", "w")
    print_get_most_played(file_name)
    f.write("What is the title of the most played game?    {}\n".format(get_most_played(file_name)))
    print_sum_sold(file_name)
    f.write("How many copies have been sold total?    {}\n".format(sum_sold(file_name)))
    print_get_selling_avg(file_name)
    f.write("What is the average selling?    {}\n".format(get_selling_avg(file_name)))
    print_count_longest_title(file_name)
    f.write("How many characters long is the longest title?    {}\n".format(count_longest_title(file_name)))
    print_get_date_avg(file_name)
    f.write("What is the average of the release dates?    {}\n".format(get_date_avg(file_name)))
    title = str(input("Enter the name of the game that you want to know the properties of: "))
    print_get_game(file_name, title)
    f.write("What are the properties of the game?    {}\n".format(get_game(file_name, title)))
    print_count_grouped_by_genre(file_name)
    f.write("How many games are there grouped by genre?    {}\n".format(count_grouped_by_genre(file_name)))
    print_get_date_ordered(file_name)
    f.write("What is the date ordered list of the games?    {}\n".format(get_date_ordered(file_name)))
    f.close()
    print("Your answers are ready in the 'answers.txt' file.\nNow take your puppy eyes to somewhere else...\nBye!!!")

if __name__ == '__main__':
    main()
