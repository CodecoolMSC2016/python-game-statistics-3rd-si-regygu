def print_count_games(file_name):
    from reports import count_games
    print("The number of games in the file is {}.\n".format(count_games(file_name)))


def print_decide(file_name, year):
    from reports import decide
    print("Is there a game from the given year? {}\n".format(decide(file_name, year)))


def print_get_latest(file_name):
    from reports import get_latest
    print("The latest game is {}.\n".format(get_latest(file_name)))


def print_count_by_genre(file_name, genre):
    from reports import count_by_genre
    print("The number of games in the given genre is {}.\n".format(count_by_genre(file_name, genre)))


def print_get_line_number_by_title(file_name, title):
    from reports import get_line_number_by_title
    print("The line number of the given game is {}.\n".format(get_line_number_by_title(file_name, title)))


def print_get_genres(file_name):
    from reports import get_genres
    print("The list of the genres: {}\n".format(get_genres(file_name)))


def print_when_was_top_sold_fps(file_name):
    from reports import when_was_top_sold_fps
    print("The release date of the top-sold fps game is {}.\n".format(when_was_top_sold_fps(file_name)))
    

