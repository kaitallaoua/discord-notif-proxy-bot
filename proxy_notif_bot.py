import json
from pathlib import Path
from time import sleep

import requests
from discord import RequestsWebhookAdapter, Webhook

MINS_30 = 1800
REPEAT_MSG_EVERY = 5

config = json.loads(Path("config.json").read_text())
WEBHOOK_URL = config["api_url"]
PROXY_URL = config["proxy_url"]


def main():
    webhook = Webhook.from_url(
        WEBHOOK_URL,
        adapter=RequestsWebhookAdapter(),
    )

    latch_message_count = 0

    while True:

        try:
            requests.get("http://google.com", proxies={"http": PROXY_URL})
            latch_message_count = 0
        except requests.exceptions.ConnectionError:
            if latch_message_count % REPEAT_MSG_EVERY == 0:
                webhook.send("Proxy Server Connection Failed")
            latch_message_count += 1
            # TODO: then re attempt with another config?
            # TODO: try to detect different failure modes like the current one, invalid credentials etc
        sleep(MINS_30)


if __name__ == "__main__":
    main()
