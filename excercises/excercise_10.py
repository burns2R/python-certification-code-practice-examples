import pandas as pd

df = pd.DataFrame({'index': ['Team A', 'Team B', 'Team C'],
                   'win_prob': [0.430473, -0.520513, 0.816822]
                   })

#correct!!
df_filtered = df[df['win_prob'] > 0.2].round(3)
print(df_filtered)