import asyncio
import json

import aiohttp

from understat import Understat


async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        player = await understat.get_league_players(
            "epl",
            2022
        )
        print(json.dumps(player))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())