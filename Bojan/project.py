import asyncio
import json

import aiohttp

from understat import Understat

forward = [["shots", "goals", "xG", "assists", "xGChain", "key_passes"]]

async def main(league, year, name, team):
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
                foward_stat.append(int(player_stat[i][1]))
            if player_stat[i][0] == "xG":
                foward_stat.append(round(float(player_stat[i][1]),2))
            if player_stat[i][0] == "assists":
                foward_stat.append(int(player_stat[i][1]))
            if player_stat[i][0] == "shots":
                foward_stat.append(int(player_stat[i][1]))
            if player_stat[i][0] == "key_passes":
                foward_stat.append(int(player_stat[i][1]))
            if player_stat[i][0] == "xGChain":
                foward_stat.append(round(float(player_stat[i][1]),2))
            

        foward_per.append([foward_stat])  # Enclose foward_stat in a list
        forward.append(tuple(foward_per))


loop = asyncio.get_event_loop()
# 크롤링해서 가져올 부분
loop.run_until_complete(main("epl", 2022, "Erling Haaland", "Manchester City"))
loop.run_until_complete(main("La liga", 2022, "Vinícius Júnior", "Real Madrid"))
loop.run_until_complete(main("Bundesliga", 2022, "Jamal Musiala", "Bayern Munich"))
print(forward)
sdata = forward
