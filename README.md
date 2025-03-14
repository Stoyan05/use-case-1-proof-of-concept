Hello, This is my project for the amusement park database. 

The way this works is:
1. In the SQL folder, you need to run the SQL file in the snowflake environment to create the DB and it's tables
2. Going into script folder, you need to run the python file, which creates a new insert_data SQL file on your computer, which you go into, and copy it's content, and pase it into the snowflake environment, it is just a bunch of randomly generated INSERT statements.
3. In the server folder, you can find the db.py script which initializes the connection to the snowflake database, and has methods to query and insert into the db, and the app.py, which starts up the flask server, and contains data for the endpoints of the server.
4. You can check out the doc folder which includes an ER diagram of the database and a word file to explain what each table is for.
