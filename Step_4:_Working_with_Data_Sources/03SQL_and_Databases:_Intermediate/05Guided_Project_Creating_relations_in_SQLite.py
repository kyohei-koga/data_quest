
# coding: utf-8

# In[14]:

import sqlite3
conn = sqlite3.connect("nominations.db")
query = "pragma table_info(nominations);"
schema = conn.execute(query).fetchall()
query = "select * from nominations limit 10;"
first_ten = conn.execute(query).fetchall()

for r in schema:
    print (r)
    
for r in first_ten:
    print(r)


# In[15]:
# we'll focus on creating the ceremonies table and inserting the data we need.
# The Python sqlite3 library comes with an executemany method that let's us easily mass insert records into a table. The executemany method requires the records we want to insert to be represented as a list of tuples. 
years_hosts = [(2010, "Steve Martin"),
               (2009, "Hugh Jackman"),
               (2008, "Jon Stewart"),
               (2007, "Ellen DeGeneres"),
               (2006, "Jon Stewart"),
               (2005, "Chris Rock"),
               (2004, "Billy Crystal"),
               (2003, "Steve Martin"),
               (2002, "Whoopi Goldberg"),
               (2001, "Steve Martin"),
               (2000, "Billy Crystal"),
            ]
create_ceremonies = "create table ceremonies (id integer primary key,year integer, host text);"
conn.execute(create_ceremonies)
insert_query = "insert into ceremonies (Year, Host) values (?,?);"
conn.executemany(insert_query,years_hosts)

print(conn.execute("select * from ceremonies limit 10;").fetchall())
print(conn.execute("pragma table_info(ceremonies);").fetchall())


# In[16]:

conn.execute("PRAGMA foreign_keys = ON;")


# In[22]:

create_nominations_two = '''create table nominations_two 
(id integer primary key, 
category text, 
nominee text, 
movie text, 
character text, 
won text,
ceremony_id integer,
foreign key(ceremony_id) references ceremonies(id));
'''

nom_query = '''
select ceremonies.id as ceremony_id, nominations.category as category, 
nominations.nominee as nominee, nominations.movie as movie, 
nominations.character as character, nominations.won as won
from nominations
inner join ceremonies 
on nominations.year == ceremonies.year
;
'''
joined_nominations = conn.execute(nom_query).fetchall()

#conn.execute(create_nominations_two)

insert_nominations_two = '''insert into nominations_two (ceremony_id, category, nominee, movie, character, won) 
values (?,?,?,?,?,?);
'''

conn.executemany(insert_nominations_two, joined_nominations)
print(conn.execute("select * from nominations_two limit 5;").fetchall())


# In[23]:
#We can use the DROP TABLE statement to drop the original nominations table.
#we can use the ALTER TABLE statement to rename nominations_two to nominations.
drop_nominations = "drop table nominations;"
conn.execute(drop_nominations)

rename_nominations_two = "alter table nominations_two rename to nominations;"
conn.execute(rename_nominations_two)


# In[25]:

create_movies = "create table movies (id integer primary key,movie text);"
create_actors = "create table actors (id integer primary key,actor text);"
create_movies_actors = '''create table movies_actors (id INTEGER PRIMARY KEY,
movie_id INTEGER references movies(id), actor_id INTEGER references actors(id));
'''
conn.execute(create_movies)
conn.execute(create_actors)
conn.execute(create_movies_actors)


# In[26]:

insert_movies = "insert into movies (movie) select distinct movie from nominations;"
insert_actors = "insert into actors (actor) select distinct nominee from nominations;"
conn.execute(insert_movies)
conn.execute(insert_actors)

print(conn.execute("select * from movies limit 5;").fetchall())
print(conn.execute("select * from actors limit 5;").fetchall())


# In[27]:

pairs_query = "select movie,nominee from nominations;"
movie_actor_pairs = conn.execute(pairs_query).fetchall()

join_table_insert = "insert into movies_actors (movie_id, actor_id) values ((select id from movies where movie == ?),(select id from actors where actor == ?));"
conn.executemany(join_table_insert,movie_actor_pairs)

print(conn.execute("select * from movies_actors limit 5;").fetchall())




