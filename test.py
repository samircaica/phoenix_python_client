import phoenixdb
import phoenixdb.cursor
import sys
import random
import logging
import gssapi
import requests
from requests_gssapi import HTTPSPNEGOAuth


if __name__ == '__main__':
    pqs_host = sys.argv[1]
    pqs_port = sys.argv[2]
    database_url = (str(pqs_host) + ':' + str(pqs_port) + '/')
    
    #loggin level
    #logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)


    print("CREATING PQS CONNECTION")
    
    spnego = gssapi.OID.from_int_seq("1.3.6.1.5.5.2")
    authobj = HTTPSPNEGOAuth(opportunistic_auth=True,mech=spnego)
    conn = phoenixdb.connect(database_url, autocommit=True, auth=authobj)
    

    cursor = conn.cursor()

    try:
        print("DROP TABLE IF EXISTS EMP4")
        cursor.execute("DROP TABLE IF EXISTS EMP4")
    except Exception as e:
        print("Problem drop table", e)
        raise

    try:
        cursor.execute("CREATE TABLE EMP4 (id INTEGER PRIMARY KEY, username VARCHAR)")
    except Exception as e:
        print("Problem creating table", e)
        raise

    depts = ["SALES", "SUPPORT", "DEVELOPMENT", "MANAGEMENT"]
    try:
        for x in range(0, 10):
            dept = random.choice(depts)
            print("INSERTING VALUES ID DEPT ", (x+1, dept))
            cursor.execute("UPSERT INTO EMP4 VALUES (?, ?)", (x+1, dept))
    except Exception as e:
        print("Problem inserting into table", e)
        raise

    cursor.execute("SELECT * FROM EMP4")
    print("RESULTS")
    print(cursor.fetchall())



