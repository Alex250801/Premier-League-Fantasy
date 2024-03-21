import requests
from bs4 import BeautifulSoup

urls = {
    ### General
    "GOALS" : " /goals",
    "ASSISTS" : "/goal_assist",

    ## Attack
    "SHOTS" : "/total_scoring_att",
    "SHOTS ON TARGET" : "/ontarget_scoring_att",
    "BIG CHANCES MISSED" : "/big_chance_missed",
    "THROUGH BALLS" : "/total_through_ball",

    ## Defence
    "INTERCEPTIONS" : "/interception",
    "BLOCKS" : "/outfielder_block",
    "TACKLES" : "/total_tackle",
    "ERRORS LEADING TO GOAL" : "/error_lead_to_goal",

    ## Goalkeeper
    "CLEAN SHEETS" : "/clean_sheet",
    "GOALS CONCEDED" : "/goals_conceded?po=GOALKEEPER",
    "SAVES" : "/saves?po=GOALKEEPER",
    "PENALTY SAVES" : "/penalty_save?po=GOALKEEPER"
}

URL_GOALS = "https://www.premierleague.com/stats/top/players/goals?se=578"
page = requests.get(URL_GOALS)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find('table')
player_stats = results.find_all('tr', class_ = 'table__row')
data = []
for player_stat in player_stats:
    player_RANK = player_stat.find('td', class_ = 'stats-table__rank')
    player_NAME = player_stat.find('a', class_ = 'playerName')
    player_CLUB = player_stat.find('a', class_ = 'stats-table__cell-icon-align')
    player_NATIONALITY = player_stat.find('span', class_ = 'stats__player-country')
    player_ATTRIBUTE = player_stat.find('td', class_ = 'stats-table__main-stat')
    data.append(player_RANK.text.strip())
    data.append(player_NAME.text.strip())
    data.append(player_CLUB.text.strip())
    data.append(player_NATIONALITY.text.strip())
    data.append(player_ATTRIBUTE.text.strip())
    data.append("NEXT PLAYER")
    print(player_RANK.text.strip())
    print(player_NAME.text.strip())
    print(player_CLUB.text.strip())
    print(player_NATIONALITY.text.strip())
    print(player_ATTRIBUTE.text.strip())
    print(" ")

print(data)
print(urls["ASSISTS"])


