import pandas as pd

# The 'dataframe' is the most common data structure used in Pandas,
# is like a spreadsheet.

# Creating a DataFrame from a dictionary of lists (column by column): ¿less keyword redundant but less legibility?
football_dict_a = {
    'player': ['Lionel Messi', 'Cristiano Ronaldo'],
    'year': [2016, 2016],
    'goals': [37, 25]
}
football_dataframe_a = pd.DataFrame(football_dict_a)
print(f'\nFootball dictionary of lists (column by column):\n{football_dict_a}')
print(f'\nFootball dataframe:\n{football_dataframe_a}')

# Creating a DataFrame from a dictionary of lists (row by row): ¿more keyword redundant but more legibility?
football_dict_b = [
    {'player': 'Lionel Messi', 'year': 2016, 'goals': 37},
    {'player': 'Cristiano Ronaldo', 'year': 2016, 'goals': 25}
]
football_dataframe_b = pd.DataFrame(football_dict_a)
print(f'\nFootball dictionary of lists (row by row):\n{football_dict_b}')
print(f'\nFootball dataframe:\n{football_dataframe_b}')

# Creating dataframe from CSV file
df_a = pd.read_csv('./data/testing.csv')
print(f'\nRead from CSV file:\n{df_a}')

# Changing the default numeric indexation of rows
df_b = pd.read_csv(filepath_or_buffer='./data/testing.csv', index_col='player')
print(f'\nDataframe with player name indexation:\n{df_b}')
