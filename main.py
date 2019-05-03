import time
import pymysql
from os import listdir
from os.path import isfile, join, dirname

my_path = join(dirname(__file__), 'books/')

only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

db = pymysql.connect("localhost", "root", "pswd1234", "allensp6_greek")
cursor = db.cursor()

time_start = time.time()

for file in only_files:
    with open(my_path + file, encoding="utf8") as f:
        for line in f:
            path, part_of_speech, parsing_code, text, word, normalized_word, lemma = line.strip().split()
            print(path[0:2], path[2:4], path[4:6], part_of_speech, parsing_code, text, word, normalized_word, lemma)

            try:
                cursor.execute(
                    "INSERT INTO lwt_greek_morphgnt (\
                        book,\
                        chapter,\
                        verse,\
                        part_of_speech,\
                        parsing_code,\
                        text,\
                        word,\
                        normalized_word,\
                        lemma\
                    ) VALUES (\
                        '%s',\
                        '%s',\
                        '%s',\
                        '%s',\
                        '%s',\
                        '%s',\
                        '%s',\
                        '%s',\
                        '%s'\
                    )" %
                    (path[0:2], path[2:4], path[4:6], part_of_speech, parsing_code, text, word, normalized_word, lemma)
                )
                # commit changes to db
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

db.close()

print('starting time: ' + str(time_start))
print('ending time: ' + str(time.time()))
