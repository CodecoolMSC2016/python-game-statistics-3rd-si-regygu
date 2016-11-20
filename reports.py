def count_games(file_name):
    f = open(file_name, "r")
    counter = 0
    for line in f:
        counter += 1
    f.close()
    return counter


def decide(file_name, year):
    f = open(file_name, "r")
    cont = f.read()
    f.close()
    year = str(year)
    if year in cont:
        return True
    else:
        return False


def get_latest(file_name):
    f = open(file_name, "r")
    cont = f.readlines()
    names_and_dates = {}
    latest_date = 0
    for line in reversed(cont):
        elements_of_a_line = line.split('\t')
        names_and_dates[int(elements_of_a_line[2])] = elements_of_a_line[0]
        if int(elements_of_a_line[2]) > latest_date:
            latest_date = int(elements_of_a_line[2])
    f.close()
    return names_and_dates.get(latest_date)


def count_by_genre(file_name, genre):
    f = open(file_name, "r")
    cont = f.readlines()
    counter = 0
    for line in cont:
        if genre in line:
            counter += 1
    f.close()
    return counter


def get_line_number_by_title(file_name, title):
    f = open(file_name, "r")
    cont = f.readlines()
    line_number = 1
    max_number_of_lines = len(cont)
    for line in cont:
        elements_of_this_line = line.split('\t')
        if title != elements_of_this_line[0]:
            line_number += 1
        else:
            break
    f.close()
    if line_number > max_number_of_lines:
        raise ValueError
    return line_number


def get_genres(file_name):
    f = open(file_name, "r")
    cont = f.readlines()
    f.close()
    genres = []
    for line in cont:
        if (line.split('\t')[3]) not in genres:
            genres.append(line.split('\t')[3])
    return sorted(genres, key=str.lower)


def when_was_top_sold_fps(file_name):
    f = open(file_name, "r")
    cont = f.readlines()
    f.close()
    top_fps = [0, 0]
    for line in cont:
        if (line.split('\t')[3]) == "First-person shooter":
            if float(line.split('\t')[1]) > top_fps[0]:
                top_fps[0] = float(line.split('\t')[1])
                top_fps[1] = int(line.split('\t')[2])
    return top_fps[1]
