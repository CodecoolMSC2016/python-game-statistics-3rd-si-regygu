def get_most_played(file_name):
    f = open(file_name, "r")
    cont = f.readlines()
    f.close()
    most_played = [0, ""]
    for line in cont:
        if float(line.split('\t')[1]) > most_played[0]:
            most_played[0] = float(line.split('\t')[1])
            most_played[1] = (line.split('\t')[0])
    return most_played[1]


def sum_sold(file_name):
    f = open(file_name, "r")
    cont = f.readlines()
    f.close()
    total = 0
    for line in cont:
        total += float(line.split('\t')[1])
    return total


def get_selling_avg(file_name):
    f = open(file_name, "r")
    cont = f.readlines()
    f.close()
    total = 0
    number_of_games = 0
    for line in cont:
        total += float(line.split('\t')[1])
        number_of_games += 1
    return total/number_of_games


def count_longest_title(file_name):
    f = open(file_name, "r")
    cont = f.readlines()
    f.close()
    titles = []
    for line in cont:
        titles.append(line.split('\t')[0])
    return len(max(titles, key=len))


def get_date_avg(file_name):
    import math
    f = open(file_name, "r")
    cont = f.readlines()
    f.close()
    total = 0
    number_of_games = 0
    for line in cont:
        total += int(line.split('\t')[2])
        number_of_games += 1
    return math.ceil(total/number_of_games)


def get_game(file_name, title):
    f = open(file_name, "r")
    cont = f.readlines()
    f.close()
    properties = []
    for line in cont:
        if line.split('\t')[0] == title:
            properties.append(line.split('\t')[0])
            properties.append(float(line.split('\t')[1]))
            properties.append(int(line.split('\t')[2]))
            properties.append(line.split('\t')[3])
            properties.append((line.split('\t')[4]).rstrip('\n'))
    return properties


def count_grouped_by_genre(file_name):
    f = open(file_name, "r")
    cont = f.readlines()
    f.close()
    genre_values = {}
    for line in cont:
        if line.split('\t')[3] in genre_values:
            genre_values[line.split('\t')[3]] += 1
        else:
            genre_values[line.split('\t')[3]] = 1
    return genre_values


def get_date_ordered(file_name):
    f = open(file_name, "r")
    cont = f.readlines()
    f.close()
    sorted_titles = []
    temp_list = []
    for date in range(2100, 1950, -1):
        for line in cont:
            if int(line.split('\t')[2]) == date:
                temp_list.append(line.split('\t')[0])
        for title in sorted(temp_list):
            sorted_titles.append(title)
        temp_list = []
    return sorted_titles

