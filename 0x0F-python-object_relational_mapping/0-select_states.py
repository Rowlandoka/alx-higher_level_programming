#!/usr/bin/python3
# Get all states via python


def main(args):
    # Get states
    if len(args) != 4:
        raise Exception('Needs 3 arguments')
    db = MySQLdb.connect(
        host='localhost', user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states  ORDER BY id ASC')
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
