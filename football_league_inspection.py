import pandas as pd

# Dataframe sorting
df_sort = pd.read_csv(filepath_or_buffer='./data/Fullmetadata.csv', index_col='player_name')
best_5_scorers = df_sort.sort_values(by='goals', ascending=False).head()
# print(f'\nBest 5 scorers:\n{best_5_scorers}')

# Dataframe subsetting
whole_df = pd.read_csv('./data/Fullmetadata.csv')

df_one_columns = whole_df['player_name']
df_two_columns = whole_df[['player_name', 'goals']]
print(f'\n1 column subset:\n{df_one_columns}')
print(f'\n2 column subset:\n{df_two_columns}')

# Dataframe filtering
print('\nFilter by name (dot notation):\n', whole_df[ whole_df.player_name == 'Lionel Messi']) # Dot notation
print('\nFilter by name (brackets notation):\n', whole_df[ whole_df['player_name'] == 'Lionel Messi' ]) # Brackets notation

# Filter with a list
filter_list = ['Lionel Messi', 'Cristiano Ronaldo']
print('\nFilter by name (using a list):\n', whole_df[ whole_df.player_name.isin(filter_list) ].sort_values(by='player_name'))

# Alternative way to filter the dataframe
print('\nAlternative filter:\n', whole_df.query('player_name == "Lionel Messi"'))
goals_parameter = 30
print('\nMore than 40 goals:\n', whole_df.query('goals > @goals_parameter')) # Inserting a variable in the bool expression
print('\nMora than 40 goals in 2015:\n', whole_df[ (whole_df.year==2015) & (whole_df.goals > goals_parameter) ]) # Multiple conditions with '&' operator

# Dataframe indexing manipulation
df_red_card_indexation = whole_df.set_index('red_cards')
print('\nRed card indexing:\n', df_red_card_indexation.head())
print('\nRed card indexing (sorted):\n', df_red_card_indexation.sort_index(ascending=False).head())
print('\nRestarting to default indexing:\n', df_red_card_indexation.reset_index().head())

