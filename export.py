# Export functions

import reports

answears=[
reports.count_games("game_stat.txt"),
reports.decide("game_stat.txt", 2311),
reports.get_latest("game_stat.txt"),
reports.count_by_genre("game_stat.txt", "First-person shooter"),
reports.get_line_number_by_title("game_stat.txt", "Diablo III"),
reports.sort_abc("game_stat.txt"),
reports.get_genres("game_stat.txt"),
reports.when_was_top_sold_fps("game_stat.txt"),
]

with open("answears.txt","w") as f:
    for element in answears:
        f.write(str(element)+"\n")
