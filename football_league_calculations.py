import pandas as pd

df = pd.read_csv('./data/Fullmetadata.csv')

# Sum all values of a column
df_all_goals = df['goals'].sum()
print('\nDataframe all goals:\n', df_all_goals)

# Mean of all goals
df_goals_mean = df['goals'].mean()
print('\nDataframe goals mean:\n', df_goals_mean)

# Max value of a column
max_score = df['goals'].max()
max_scorer_cols = ['player_name', 'goals']
df_goals_subset = df[ df.goals == max_score ][max_scorer_cols]
print('\nMax scorer:\n', df_goals_subset)

# Min value of a column
min_games = df['games'].min()
dusty_player_cols = ['player_name', 'games']
most_dusty_players = df[ df.games == min_games ][dusty_player_cols]
print('\nMost dusty player:\n', most_dusty_players)

# Count the different values inside a column (usefull to count categories)
teams_count = df['team_name'].value_counts(sort=True)
red_cards_amount = df['red_cards'].value_counts() # By default 'sort' parameter is 'True'

danger_player_cols = ['player_name', 'red_cards']
most_danger_player = df[ df.red_cards == df['red_cards'].max() ][danger_player_cols]
print('\nMost danger player:\n', most_danger_player)

print('\nCount of teams:\n', teams_count)
print('\nCount of red cards:\n', red_cards_amount)

