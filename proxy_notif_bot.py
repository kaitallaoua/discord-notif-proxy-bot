import asyncio
import json
from pathlib import Path

import requests
from aiohttp import ClientSession
from discord import Webhook

SLEEP_TIME_SEC = 1800  # 30 mins
REPEAT_MSG_EVERY = 5

config = json.loads(Path("config.json").read_text())
WEBHOOK_URL = config["webhook_url"]
PROXY_URL = config["proxy_url"]


#TODO: investigate spam
async def main():
    async with ClientSession() as session:
        webhook = Webhook.from_url(WEBHOOK_URL, session=session)

        latch_message_count = 0

        while True:

            try:
                # TODO: use async here
                requests.get("http://google.com", proxies={"http": PROXY_URL})
                latch_message_count = 0
            except requests.exceptions.ConnectionError:
                if latch_message_count % REPEAT_MSG_EVERY == 0:
                    await webhook.send("Proxy Server Connection Failed")
                latch_message_count += 1
                # TODO: then re attempt with another config?
                # TODO: try to detect different failure modes like the current one, invalid credentials etc
            await asyncio.sleep(SLEEP_TIME_SEC)


if __name__ == "__main__":
    asyncio.run(main())
