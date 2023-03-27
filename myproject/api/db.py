import psycopg2 

def initBro():
    try:
        conn = psycopg2.connect("dbname='ecom_db' user='mdalmominmostafa' host='localhost'")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()
    cur.execute("""SELECT * from person""")