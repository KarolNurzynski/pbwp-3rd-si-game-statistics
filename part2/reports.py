
# Report functions


# Function 1

def get_most_played(file_name):
    table = []
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    table.sort(key=lambda x: float(x[1]), reverse=True)
    return table[0][0]

# Function 2


def sum_sold(file_name):
    table = []
    total_sold = 0
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    for element in table:
        total_sold += float(element[1])
    return total_sold

# Function 3


def get_selling_avg(file_name):
    table = []
    total_sold = 0
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    for element in table:
        total_sold += float(element[1])
        avg = total_sold / len(table)
    return avg

# Function 4


def count_longest_title(file_name):
    table = []
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    titles = [x[0] for x in table]
    return len(max(titles, key=len))

# Function 5


def get_date_avg(file_name):
    table = []
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    years = [int(x[2]) for x in table]
    avg = sum(years) / len(years)
    return round(avg)

# Funcion 6


def get_game(file_name, title):
    table = []
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    titles = [x[0] for x in table]
    index = titles.index(title)
    p = table[index]
    properties = [p[0], float(p[1]), int(p[2]), p[3], p[4].strip()]
    return properties

# Funcion 7


def count_grouped_by_genre(file_name):
    table = []
    genres_dict = {}
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    genres = [x[3] for x in table]
    genres_set = set(genres)
    for element in genres_set:
        genres_dict.update({element: genres.count(element)})
    return genres_dict

# Funcion 8


def get_date_ordered(file_name):
    table = []
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    table.sort(key=lambda x: (-int(x[2]), x[0]))
    sorted_titles = [x[0] for x in table]
    return sorted_titles
