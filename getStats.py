import requests
import datetime
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
    if True == True:
        rundown = requests.get("https://api.mcchampionship.com/v1/rundown")
        with open("static/db/individualScores.json", "w") as individualScores:
            individualScores.write(rundown.text)

        downloadParticipantStats("RED")
        downloadParticipantStats("ORANGE")
        downloadParticipantStats("YELLOW")
        downloadParticipantStats("GREEN")
        downloadParticipantStats("LIME")
        downloadParticipantStats("AQUA")
        downloadParticipantStats("CYAN")
        downloadParticipantStats("BLUE")
        downloadParticipantStats("PURPLE")
        downloadParticipantStats("PINK")