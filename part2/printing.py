def print_get_most_played(file_name):
    from reports import get_most_played
    print("The most played game is {}.\n".format(get_most_played(file_name)))


def print_sum_sold(file_name):
    from reports import sum_sold
    print("The total number of copies sold is {}m.\n".format(sum_sold(file_name)))


def print_get_selling_avg(file_name):
    from reports import get_selling_avg
    print("The average of copies sold is {}m.\n".format(get_selling_avg(file_name)))


def print_count_longest_title(file_name):
    from reports import count_longest_title
    print("The lenght of the longest title is {} characters.\n".format(count_longest_title(file_name)))


def print_get_date_avg(file_name):
    from reports import get_date_avg
    print("The average of release dates is {}.\n".format(get_date_avg(file_name)))


def print_get_game(file_name, title):
    from reports import get_game
    print("The properties of this game are the following: {}.\n".format(get_game(file_name, title)))


def print_count_grouped_by_genre(file_name):
    from reports import count_grouped_by_genre
    print("The genres by counts are the following: {}.\n".format(count_grouped_by_genre(file_name)))


def print_get_date_ordered(file_name):
    from reports import get_date_ordered
    print("The games ordered by release date: {}.\n".format(get_date_ordered(file_name)))
