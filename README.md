# soccerdb

I investigated the soccer database from kaggle
The database can be found in kaggle's website at
I used jupyter notebooks to perform my analysis I divided the dataset into three joined tables play, team and game.
Game includes league, country and match table, team icludes team and team_attributes tables lastly play table which was table of my primary interest includes player and player attributes tables.
I used sqlite3 to connect to the database and then I used panda's .read_sql_query function to query the database.