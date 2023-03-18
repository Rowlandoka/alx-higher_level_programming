#!/usr/bin/python3
# gets all states via python


def main(args):
    # gets all state
    if len(args) != 4:
        raise Exception("need 3 arguments!")
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=args[1],
                         passwd=args[2],
                         db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
