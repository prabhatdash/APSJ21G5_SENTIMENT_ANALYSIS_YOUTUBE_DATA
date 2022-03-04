import connector as con
def auth_user(email):
    count=0
    query = "select * from reg_users;"
    con.cursor.execute(query)
    for i in con.cursor:
        if i[0]==email:
            count=1
    return count
