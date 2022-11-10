import requests, json
import datetime, sys
isMonday = datetime.date.today().isoweekday() == 1
def downloadGameStats(gameName):
    req = requests.get(f"https://api.mcchampionship.com/v1/halloffame/{gameName}")
    with open(f"static/db/team/{gameName}.json", "w") as stat:
        stat.write(req.text)

def downloadParticipantStats(teamName):
    team = requests.get(f'https://api.mcchampionship.com/v1/participants/{teamName}')
    with open(f"static/db/participants{teamName}.json", "w") as teamw:
        teamw.write(team.text)


def downloadSetup():
    if isMonday == True or sys.argv[1] == "download" or sys.argv[1] == "cache":
        TEAMS = ["RED","ORANGE","YELLOW","GREEN","LIME","AQUA","CYAN","BLUE","PURPLE","PINK"]

        if sys.arv[1] == "download":
            rundown = requests.get("https://api.mcchampionship.com/v1/rundown")
            with open("static/db/individualScores.json", "w") as individualScores:
                individualScores.write(rundown.text)
            for team in TEAMS:
                downloadParticipantStats(f"{team}")

        with open("static/db/individualScores.json", "r") as scoreReader:
            content = json.loads(scoreReader.read())
            scores = content["data"]["individualScores"]

        participantList = []
        for team in TEAMS:
            with open(f"static/db/participants{team}.json", "r") as participantReader:
                participants = json.loads(participantReader.read())
                participants = participants["data"]       
                for participant in range(len(participants)):
                    participantList.append(participants[participant]["username"])


    diff_names = list(set(participantList) - set(scores))

    diff_name_dict = {diff: "0000" for diff in diff_names}
    content_dict = content["data"]["individualScores"]
    content_dict.update(diff_name_dict)
    

    content["data"]["individualScores"] = content_dict

    # print(content)

    with open("static/db/individualScores.json", "w") as scoreFixer:
        scoreFixer.write(content)

if sys.argv[1] == "download":
    downloadSetup()