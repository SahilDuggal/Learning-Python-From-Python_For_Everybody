# Using the SQLite Browser 

# Command to create a Table in database
# CREATE TABLE Users(
# name VARCHAR(127),
# email VARCHAR(127)
# )

# Command to insert data into the table
# INSERT INTO Users (name, email) VALUES ('Sahil', 'duggalsahil1909@gmail.com')

# Command to delete data from the table
# DELETE FROM Users WHERE email='duggalsahil1909@gmail.com' // All the emails with the email address is same the emails will be deleted.

# Command to update data in the table
# UPDATE Users SET name='Sahil', email='duggalsahil1909@gmail.com' WHERE name='Pranav'

# Command to read data of the table
# SELECT * FROM Users // To select all the data 
# SELECT * FROM Users WHERE name='Sahil' // To select data with particular attribute
# SELECT name FROM Users 
# SELECT * FROM Users ORDER BY name // To select all the data in a order alphabatically.

# Track (Table)
# ID    album_ID    Genre_ID    Title           Len     Rating  Count
# 1	    2	        1	        Black Dog	    297	    5	    0
# 2	    2	        1	        Stairway	    482	    5	    0
# 3	    1	        2	        About to Rock	313	    5	    0
# 4	    1	        2	        Who Made Who	207	    5	    0

# Artist (Table)
# ID    Name
# 1	    Led Zepplin
# 2	    AC/DC

# Album (Table)
# ID    Artist_ID   Track
# 1	    2	        Who Made Who
# 2	    1	        IV

# Genre (Table)
# ID    Name
# 1	    Rock
# 2	    Metal

# Command to join2 or more tables
# Select Album.title, Album.artist_id, Artist.id, Artist.name from Album JOIN Artist on Album.artist_id = Artist.id 

# SELECT * FROM Track JOIN Album JOIN Artist JOIN Genre ON Track.album_id = Album.id and Track.genre_id = Genre.id and Album.artist_id = Artist.id

# Track.title, Artist.name, Album.title, Genre.name