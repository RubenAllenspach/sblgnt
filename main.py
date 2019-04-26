import time
import pymysql
from os import listdir, walk
from os.path import isfile, join, dirname

mypath = join(dirname(__file__), 'books/')

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

db = pymysql.connect("localhost", "root", "pswd1234", "allensp6_greek")
cursor = db.cursor()

time_start = time.time()

for file in onlyfiles:
    with open(mypath + file, encoding="utf8") as f:
        for line in f:
            path, part_of_speech, parsing_code, text, word, normalized_word, lemma = line.strip().split()
            print(path, part_of_speech, parsing_code, text, word, normalized_word, lemma)

            try:
                cursor.execute(
                    "INSERT INTO lwt_greek_morphgnt (\
                        path,\
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
                        '%s'\
                    )" % \
                    (path, part_of_speech, parsing_code, text, word, normalized_word, lemma)
                )
                # commit changes to db
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

db.close()

print('starting time: ' + str(time_start))
print('ending time: ' + str(time.time()))



# import pymysql
# import pprint
# import os.path

# Open database connection
# db = pymysql.connect("localhost", "root", "pswd1234", "allensp6_greek")

# prepare a cursor object using cursor() method
# cursor = db.cursor()

# i = 0

# with open(os.path.join(os.path.dirname(__file__), "gnt_data/tokens.txt"), encoding="utf8") as f:
    # for line in f:
        # i += 1

        # token_id, token_text, token_text_normalized, part_of_speech, morphological_tag_old, morphological_tag_new, lemma = line.strip().split()

        # print(token_id, token_text, token_text_normalized, part_of_speech, morphological_tag_old, morphological_tag_new, lemma)

        # if i > 10:
        #     break

        # try:
        #     cursor.execute(
        #         "INSERT INTO lwt_greek_tokens (\
        #             token_id,\
        #             token_text,\
        #             token_text_normalized,\
        #             part_of_speech,\
        #             morphological_tag_old,\
        #             morphological_tag_new,\
        #             lemma\
        #         ) VALUES (\
        #             '%d',\
        #             '%s',\
        #             '%s',\
        #             '%s',\
        #             '%s',\
        #             '%s',\
        #             '%s'\
        #         )" % \
        #         (int(token_id), token_text, token_text_normalized, part_of_speech, morphological_tag_old, morphological_tag_new, lemma)
        #     )
            # commit changes to db
            # db.commit()
        # except:
            # Rollback in case there is any error
            # db.rollback()

# Fetch a single row using fetchone() method.
# data = cursor.fetchall()

# ugly print
# print(data)

# pretty print
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(data)

# disconnect from server
# db.close()
