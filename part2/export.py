
# Export functions

import reports

answears = [
    reports.get_most_played("game_stat.txt"),
    reports.sum_sold("game_stat.txt"),
    reports.get_selling_avg("game_stat.txt"),
    reports.count_longest_title("game_stat.txt"),
    reports.get_date_avg("game_stat.txt"),
    reports.get_game("game_stat.txt", "Minecraft"),
    reports.count_grouped_by_genre("game_stat.txt"),
    reports.get_date_ordered("game_stat.txt")
]

with open("answears.txt", "w") as f:
    for element in answears:
        f.write(str(element) + "\n")
