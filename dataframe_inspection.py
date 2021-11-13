import pandas as pd

# Return the first 5 rows by default or
# 'n' rows of the dataframe, when 'n' is a integer passed.
df = pd.read_csv('./data/Fullmetadata.csv')
df_first_5_rows = df.head()
n = 12
df_first_n_rows = df.head(n)
print(f'\nFirst 5 rows of dataframe:\n{df_first_5_rows}')
print(f'\nFirst {n} rows of the dataframe:\n{df_first_n_rows}')

# Return the last 5 rows by default or
# 'n' rows of the dataframe, when 'n' is a integer passed.
df_last_5_rows = df.tail()
df_last_n_rows = df.tail(n)
print(f'\nLast 5 rows of the dataframe:\n{df_last_5_rows}')
print(f'\nLast {n} rows of the dataframe:\n{df_last_n_rows}')

# Return a random sample of 'n' from the dataframe
# when 'n' is a mandatory integer value.
df_random_sample = df.sample(3)
print(f'\nRandom sample of 3:\n{df_random_sample}')

# Return a tuple of the dataframe rows and columns.
df_dimensionality = df.shape
print(f'\nDataframe dimensionality:\n{df_dimensionality}')

# Multiply rows and columns to return the total data of the dataframe
df_total_data = df.size
print(f'\nDataframe total data:\n{df_total_data}')

# Display non-null columns, his data types and memory usage
df.info()
