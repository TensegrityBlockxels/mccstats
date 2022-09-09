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

if True == True:
    rundown = requests.get("https://api.mcchampionship.com/v1/rundown")
    with open("static/db/individualScores.json", "w") as individualScores:
        individualScores.write(rundown.text)


    # downloadGameStats("MG_ROCKET_SPLEEF")
    # downloadGameStats("MG_SURVIVAL_GAMES")
    # downloadGameStats("PARKOUR_WARRIOR")
    # downloadGameStats("MG_ACE_RACE")
    # downloadGameStats("MG_TGTTOSAWAF")
    # downloadGameStats("MG_SKYBATTLE")
    # downloadGameStats("MG_HOLE_IN_THE_WALL")
    # downloadGameStats("MG_BATTLE_BOX")
    # downloadGameStats("MG_BUILD_MART")
    # downloadGameStats("MG_SANDS_OF_TIME")
    # downloadGameStats("MG_DODGEBOLT")
    # downloadGameStats("MG_PARKOUR_TAG")
    # downloadGameStats("MG_GRID_RUNNERS")
    # downloadGameStats("MG_MELTDOWN")

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