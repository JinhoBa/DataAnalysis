import asyncio
import json

import aiohttp

from understat import Understat

forward = [["shots", "goals", "xG", "assists", "xGChain", "key_passes"]]
score_list = []
async def main(league, year, name, team):
    sum1=0
    goal=0
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        player = await understat.get_league_players(
            league, year,
            player_name=name,
            team_title=team
        )
        player_json1 = json.dumps(player)
        player_json1 = player_json1[2:-2].replace('"', "")
        player_json2 = player_json1.split(",")
        player_stat = []

        for item in player_json2:
            key, value = item.split(":")
            player_stat.append((key.strip(), value.strip()))

        foward_stat = []
        foward_per = []
        foward_per.append(player_stat[1][1])

        for i in range(len(player_stat)):
            if player_stat[i][0] == "goals":
                sum1 += (int(player_stat[i][1]))*8
                goal = (int(player_stat[i][1]))
            if player_stat[i][0] == "xG":
                xg= (float(player_stat[i][1]))
                sum1 += (goal-xg)*5
            if player_stat[i][0] == "assists":
                sum1 += (int(player_stat[i][1]))*5
            if player_stat[i][0] == "shots":
                sum1 += (int(player_stat[i][1]))*0.01
            if player_stat[i][0] == "key_passes":
                sum1 += (int(player_stat[i][1]))*0.5
            if player_stat[i][0] == "xGChain":
                sum1 += (float(player_stat[i][1]))*0.5

        foward_per.append([foward_stat])  # Enclose foward_stat in a list
        forward.append(tuple(foward_per))
        score_list.append(round(sum1,2))
        


loop = asyncio.get_event_loop()
# 크롤링해서 가져올 부분
loop.run_until_complete(main("epl", 2022, "Erling Haaland", "Manchester City"))
loop.run_until_complete(main("La liga", 2022, "Vinícius Júnior", "Real Madrid"))
loop.run_until_complete(main("epl", 2022, "Bukayo Saka", "Arsenal"))
loop.run_until_complete(main("epl", 2022, "Phil Foden", "Manchester City"))

