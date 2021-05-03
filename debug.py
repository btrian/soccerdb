import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cnt = sqlite3.connect('database.sqlite')
country =pd.read_sql_query('select * from country', cnt)
query = """
SELECT cy.id, cy.name, lg.name , lg.id, mt.season, mt.stage, mt.date, mt.match_api_id, mt.home_team_api_id, 
mt.away_team_api_id,mt.home_team_goal, py.player_api_id, py.player_name, py.player_fifa_api_id, py.birthday, 
py.height, py.weight, py_at.date, py_at.overall_rating,py_at.potential, py_at.preffered_foot, py_at.attacking_work_rate,
py_at.defensive_work_rate, py_at.crossing, py_at.finishing, py_at.heading_accuracy, py_at.short_passing, py_at.volleys,
py_at.dribbling, py_at.curves,py_at.free_kick_accuracy, py_at.long_passing, py_at.ball_control, py_at.acceleration, 
py_at.sprint_speed, py_at.agility,py_at.reactions, py_at.balance, py_at.shot_power, py_at.jumping, py_at.stamina, 
py_at.strength, py_at.long_shot, py_at.aggression, py_at.interceptions, py_at.postioning, py_at.vision, py_at.penalties,
py_at.marking, py_at.standing_tackle, py_at.sliding_tackle, tm.team_api_id, tm.team_fifa_api_id, tm.team_long_name,
tm.team_short_name, tm_at.buildUpPlaySpeed, tm_at.buildUpPlaySpeedClass, tm_at.buildUpPlayDribbling, 
tm_at.buildUpPlayDribblingClass, tm_at.buildUpPlayPassing, tm_at.buildUpPlayPassingClass 
FROM country cy
JOIN league lg ON cy.id =lg.id JOIN match mt ON mt.id = lg.id 
JOIN player py ON lg.id =py.id JOIN player_Attributes py_at ON py.id = py_at.id 
JOIN team tm ON tm.id = py_at.id JOIN team_Attributes tm_at ON tm.id = tm_at.id
"""


df = pd.read_sql_query(query, cnt)

df.head()