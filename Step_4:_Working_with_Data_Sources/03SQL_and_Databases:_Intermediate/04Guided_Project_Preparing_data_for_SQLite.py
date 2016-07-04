
# coding: utf-8

# In[34]:

import pandas as pd
df = pd.read_csv("academy_awards.csv",encoding="ISO-8859-1")
df.head(2)


# In[35]:

df["Unnamed: 10"].value_counts()


# In[36]:

df["Year"] = df["Year"].str[0:4]
df["Year"] = df["Year"].astype("int64")
later_than_2000 = df[df["Year"] > 2000]
award_categories = ["Actor -- Leading Role","Actor -- Supporting Role","Actress -- Leading Role",
                    "Actress -- Supporting Role"]
nominations = later_than_2000[later_than_2000["Category"].isin(award_categories)]


# In[37]:

replacements = {"NO":0,"YES":1}
nominations["Won?"] = nominations["Won?"].map(replacements)
nominations["Won"] = nominations["Won?"]
drop_cols = ["Won?","Unnamed: 5", "Unnamed: 6","Unnamed: 7", "Unnamed: 8", "Unnamed: 9", "Unnamed: 10"]
final_nominations = nominations.drop(drop_cols,axis=1)


# In[38]:

additional_info_one = final_nominations["Additional Info"].str.rstrip("'}")
additional_info_two = additional_info_one.str.split("{'")
movie_names = additional_info_two.str[0]
characters = additional_info_two.str[1]
final_nominations["Movie"] = movie_names
final_nominations["Character"] = characters
final_nominations = final_nominations.drop("Additional Info",axis=1)


# In[39]:

final_nominations


# In[40]:

import sqlite3
conn = sqlite3.connect("noiminations.db")
final_nominations.to_sql("nominations",conn,index=False)


# In[41]:

query = "pragma table_info(nominations);"
print(conn.execute(query).fetchall())


# In[42]:

query = "select * from nominations limit 10;"
print(conn.execute(query).fetchall())


# In[44]:

conn.close()


# In[ ]:



