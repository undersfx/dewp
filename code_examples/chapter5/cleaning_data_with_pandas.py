import pandas as pd


df = pd.read_csv('scooter.csv')


# Normalize case in columns titles
# df.rename(columns={'DURATION':'duration'},inplace=True)
df.columns = [title.lower() for title in df.columns]
print(df.columns)


# Droping rows that have bad data (zero duration trips)
bad_data = df[(df['duration']=='0:00:00')]
df.drop(index=bad_data.index,inplace=True)


# Drop column not useful (all values are the same)
df.drop(columns=['region_id'], inplace=True)


# Droping rows that have null 'DURATION'
df.dropna(subset=['duration'], inplace=True)


# Fill null values for 'start_location_name' and 'end_location_name'
df['start_location_name'].fillna('Start St.', inplace=True)
df['end_location_name'].fillna('Start St.', inplace=True)


# String methods can be called in Series with Series.str
df['month']=df['month'].str.upper()


# Create dedicated fields for time and date
# Creates a 'new' df with columns splited 
# (expand makes the colums be each of the split list indexes)
# e.g. 5/21/2019 18:33 -> 0: 5/21/2019 1: 18:33 -> date: 5/21/2019, time: 18:33
new = df['started_at'].str.split(expand=True)
df['date']=new[0]
df['time']=new[1]


# Correct datetime dtype in field 'started_at'
df['started_at'] = pd.to_datetime(df['started_at'],format='%m/%d/%Y %H:%M')
df['date'] = pd.to_datetime(df['date'],format='%m/%d/%Y')


print(df)
