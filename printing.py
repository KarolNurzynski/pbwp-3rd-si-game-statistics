
# Printing functions

import reports

# Print 1


def count_games_print():
    file_name = input("Enter file name: ")
    print("Number of games in the file: {}".format(
        reports.count_games(file_name)))

# Print 2


def decide_print():
    file_name = input("Enter file name: ")
    year = input("Enter year: ")
    answear = reports.decide(file_name, year)
    if answear:
        answear = "Yes"
    else:
        answear = "No"
    print("Is there a game from {0} year?: {1}".format(year, answear))

# Print 3


def get_latest_print():
    file_name = input("Enter file name: ")
    print("The latest game is: {}".format(reports.get_latest(file_name)))


# Print 4
def count_by_genre_print():
    file_name = input("Enter file name: ")
    genre = input("Enter genre: ")
    print(
        "Number of games in {0} : {1}".format(
            genre,
            reports.count_by_genre(
                file_name,
                genre)))

# Print 5


def get_line_number_by_title_print():
    file_name = input("Enter file name: ")
    title = input("Enter title: ")
    print(
        "Line number of game {0} is: {1}".format(
            title,
            reports.get_line_number_by_title(
                file_name,
                title)))

# Print 6


def sort_abc_print():
    file_name = input("Enter file name: ")
    print("Alphabetical ordered list of titles: " +
          str(reports.sort_abc(file_name)))

# Print 7


def get_genres_print():
    file_name = input("Enter file name: ")
    print("A list of the genres: {}".format(reports.get_genres(file_name)))

# Print 8


def when_was_top_sold_fps_print():
    file_name = input("Enter file name: ")
    print("The release date of the top sold First-person shooter game: {}".format(
        reports.when_was_top_sold_fps(file_name)))
