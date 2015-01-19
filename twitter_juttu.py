import json
from pprint import pprint
import datetime
import sys

laskuri = {}

a1 = "Vaalit"
a2 = "miten"
a3 = "Suomen"

b1 = "lol"
b2 = "miten"
b3 = "Suomen"

c1 = "Vaalit"
c2 = "miten"
c3 = "moi"

teema1 = 0
teema2 = 0
teema3 = 0

for tiedosto in sys.argv[1:]:

    with open(tiedosto) as json_data:
        d = json.load(json_data)
        json_data.close()

        for tweet in d:
            aika = datetime.datetime.fromtimestamp(
                    int(tweet['time'])
                ).strftime('%Y-%m-%d')

            if aika not in laskuri:
                laskuri[aika] = 0

            laskuri[aika] += 1

            teema_lista = tweet['text']

            if a1 in teema_lista or a2 in teema_lista or a3 in teema_lista:
                teema1 = teema1 + 1

            if b1 in teema_lista or b2 in teema_lista or b3 in teema_lista:
                teema2 = teema2 + 1
            
            if c1 in teema_lista or c2 in teema_lista or c3 in teema_lista:
                teema3 = teema3 + 1

        ##print teema_lista
print teema1
print teema2
print teema3
for paiva in sorted( laskuri.keys() ):
    print paiva , "," , laskuri[ paiva ], "," , teema1, ",", teema2, ",", teema3





