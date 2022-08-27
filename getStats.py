import requests
import datetime
isMonday = datetime.date.today().isoweekday() == 1

if True == True:
    r = requests.get('https://api.mcchampionship.com/v1/participants/RED')
    with open("db/participants-red.json", "w") as red:
        red.write(r.text)