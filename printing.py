
# Printing functions

import reports

# Print 1
def count_games_print(file_name):
    print("Number of games in the file: {}".format(reports.count_games(file_name)))

count_games_print("game_stat.txt")

# Print 2
def decide_print(file_name, year):
    answear=reports.decide(file_name, year)
    if answear==True:
        answear="Yes"
    else:
        answear="No"
    print("Is there a game from {0} year?: {1}".format(year, answear))

decide_print("game_stat.txt", 2311)

# Print 3

def get_latest_print(file_name):
    print("The latest game is: {}".format(reports.get_latest(file_name)))

get_latest_print("game_stat.txt")

# Print 4
def count_by_genre_print(file_name, genre):
    print("Number of games in {0} : {1}".format(genre, reports.count_by_genre(file_name, genre)))

count_by_genre_print("game_stat.txt", "First-person shooter")

# Print 5

def get_line_number_by_title_print(file_name,title):
    print("Line number of game {0} is: {1}".format(title, reports.get_line_number_by_title(file_name, title)))

get_line_number_by_title_print("game_stat.txt", "Diablo III")

# Print 6
def sort_abc_print(file_name):
    print("Alphabetical ordered list of titles: "+str(reports.sort_abc(file_name)))

sort_abc_print("game_stat.txt")


# Print 7

def get_genres_print(file_name):
    print("A list of the genres: {}".format(reports.get_genres(file_name)))

get_genres_print("game_stat.txt")

# Print 8
def when_was_top_sold_fps_print(file_name):
    print("The release date of the top sold First-person shooter game: {}".format(reports.when_was_top_sold_fps(file_name)))

when_was_top_sold_fps_print("game_stat.txt")
