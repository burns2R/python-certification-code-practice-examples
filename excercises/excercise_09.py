import pandas as pd

d = {'Berlin_time': ['2014-08-01 09:00:00+02:00',
     '2014-08-01 10:00:00+02:00',
     '2014-08-01 11:00:00+02:00'],
     'Data': [1.0, 2.0, 3.0]
     }
df = pd.DataFrame(data=d)
df['Berlin_time'] = pd.to_datetime(df['Berlin_time'])
df = df.set_index('Berlin_time') #Since the index is now in datetime format, it will create a 'DatetimeIndex' object

# Correct! tz_convert() is the proper method of a 'DatetimeIndex' object to change timezones.
# FYI: pandas.Series.dt is an interface on a pandas series that gives you convenient access 
# to operations on data stored as a pandas datetime. 
# FYI: pandas.Series.dt.tz_convert Convert tz-aware Datetime Array/Index from one time zone to another.
df['USCentral_time'] = df.index.tz_convert('Europe/London')
print(df)