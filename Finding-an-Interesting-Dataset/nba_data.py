import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

# data spans from ABA and NBA (1948 to current)
nba_players_data = pandas.read_csv("NBA_players_clean.csv")

print(nba_players_data)