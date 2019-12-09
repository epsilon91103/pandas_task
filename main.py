import pandas as pd

# read
df = pd.read_csv('keywords.csv', sep=';', quotechar="'")

# 1 
df['Keyword'] = df['Keyword'].str.replace(r'(?:-[a-zA-Zа-яА-Я]+)', '')

# 2
df['Keyword'] = df['Keyword'].str.replace(r'[\[\]]', '')

# 3
df_ext = df[['Keyword', 'AdGroupId']].assign(key=1).merge(
    df[['Keyword', 'AdGroupId']].assign(key=1), 
    on="key"
).drop('key', axis=1)

df_ext = df_ext[df_ext.AdGroupId_x != df_ext.AdGroupId_y].copy()

df_ext['crossed'] = df_ext.apply(
    lambda x: ', '.join(set(x.Keyword_x.split()) & set(x.Keyword_y.split())),
    axis=1
)

# write
df_ext.to_csv('keywords_ext.csv', sep=';', quotechar="'")
