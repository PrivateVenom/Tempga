import asyncio
import random

from telethon import TelegramClient
from telethon import functions, types
import questionary

api_id = int(questionary.password('Api ID:').ask())
api_hash = questionary.password('Api hash:').ask()



client = TelegramClient('session_new', api_id, api_hash)
client.start()

print('∧,,,∧   ~ ┏━━━━━━━━┓
     (  ̳• · • ̳)   ~ @Fucker_VeNoM 𝙏𝙚𝙘𝙝_𝘿𝙞𝙜𝙞𝙩𝙖𝙡
    /       づ  ~ ┗━━━━━━━━┛')


async def main():
    telegram_list = open('telegram_db', 'r').readlines()
    for (i,telegram_channel) in enumerate(telegram_list):
        if "https://" in telegram_channel:
            telegram_channel = telegram_channel.split('/')[-1]
        elif '@' in telegram_channel:
            telegram_channel = telegram_channel[1:]
        print(telegram_channel)
        try:
            result = await client(functions.account.ReportPeerRequest(
                peer=telegram_channel,
                reason=types.InputReportReasonSpam(),
                message='RUSSIAN PROPAGANDA AGAINST UKRAINE DURING RUSSIAN INVASION IN UKRAINE PLEASE TAKE DOWN IT' + str(random.random())
            ))
            print(result)
        except ValueError:
            print("Channel Error")
        await asyncio.sleep(3 + 2 * random.random())
with client:

    client.loop.run_until_complete(main())
