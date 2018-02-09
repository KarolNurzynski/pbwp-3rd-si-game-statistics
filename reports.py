# Report functions

# Function 1

def count_games(file_name):
    with open(file_name, "r") as f:
        return len(f.readlines())

# Function 2

def decide(file_name, year):
    with open(file_name, "r") as f:
        a=f.readlines()
        string=" ".join(a)
        if string.find(str(year))==-1:
            return False
        else:
            return True

# Function 3

def get_latest(file_name):
    table=[]
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    table.sort(key=lambda x:x[2], reverse=True)
    return table[0][0]

# Function 4

def count_by_genre(file_name, genre):
    table=[]
    number=0
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    for row in table:
        if row[3]==genre:
            number+=1
    return number

# Function 5

def get_line_number_by_title(file_name, title):
    table=[]
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    for row in table:
        if title in row:
            return table.index(row)+1
    raise ValueError("There is no game {} in the list".format(title))

# Function 6

def sort_abc(file_name):
    table=[]
    titles=[]
    sorted_titles = []
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    for row in table:
        titles.append(row[0])
    while titles:
        minimum = titles[0]  # arbitrary number in list
        for element in titles:
            if element < minimum:
                minimum = element
        sorted_titles.append(minimum)
        titles.remove(minimum)
    return sorted_titles

# Function 7

def get_genres(file_name):
    table=[]
    genres=[]
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    for row in table:
        genres.append(row[3])
    return sorted(set(genres))

# Function 8

def when_was_top_sold_fps(file_name):
    table=[]
    fps=[]
    with open(file_name, "r") as f:
        for row in f:
            table.append(row.split("\t"))
    for row in table:
        if row[3]=="First-person shooter":
            fps.append([float(row[1]),row[0], int(row[2])])
    fps.sort(key=lambda x:x[0], reverse=True)
    if len(fps)==0:
        raise ValueError
    return fps[0][2]
