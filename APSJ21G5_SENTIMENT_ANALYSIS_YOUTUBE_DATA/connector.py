import mysql.connector as mc
dbc = mc.connect(host="localhost",user="root",passwd="root",database="twitter_data")
cursor=dbc.cursor()