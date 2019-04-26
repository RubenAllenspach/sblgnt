import pymysql

db = pymysql.connect("localhost", "root", "pswd1234", "allensp6_greek")
cursor = db.cursor()

try:
    cursor.execute(
        "SELECT *\
        FROM lwt_greek_morphgnt\
        WHERE `text` LIKE '%%%s%'" % \
        (ord(chr(11778).encode()))
    )
    # commit changes to db
    print(cursor.fetchall())
except:
    # Rollback in case there is any error
    db.rollback()

db.close()
