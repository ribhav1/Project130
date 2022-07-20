import pandas as pd

df = pd.read_csv('E:/ClassProjects/Normal/Project130/venv/total_stars.csv')

column_headers = list(df.columns)

# Deleting obsolete column
del df['star']

df.to_csv('stars.csv', index = False, line_terminator = '\n')