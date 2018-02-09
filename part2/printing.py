
# Printing functions

import reports

# Print 1


def get_most_played():
    file_name = input("Enter file name: ")
    print("Most played game is: {}".format(reports.get_most_played(file_name)))

# Print 2


def sum_sold():
    file_name = input("Enter file name: ")
    print("Total sold copies: {}".format(reports.sum_sold(file_name)))

# Print 3


def get_selling_avg():
    file_name = input("Enter file name: ")
    print("Selling average: {}".format(reports.get_selling_avg(file_name)))

# Print 4


def count_longest_title():
    file_name = input("Enter file name: ")
    print("Number of chars of the longest title: {}".format(
        reports.count_longest_title(file_name)))

# Print 5


def get_date_avg():
    file_name = input("Enter file name: ")
    print("Average release year: {}".format(reports.get_date_avg(file_name)))

# Print 6


def get_game():
    file_name = input("Enter file name: ")
    title = input("Enter title: ")
    print("Game properties: {}".format(reports.get_game(file_name, titles)))

# Print 7


def count_grouped_by_genre():
    file_name = input("Enter file name: ")
    print("Dict by genre: {}".format(reports.count_grouped_by_genre(file_name)))

# Print 8


def get_date_ordered():
    file_name = input("Enter file name: ")
    print("Games ordered by date: {}".format(
        reports.get_date_ordered(file_name)))
