#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN\
                states ON cities.state_id=states.id ORDER BY\
                cities.id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
