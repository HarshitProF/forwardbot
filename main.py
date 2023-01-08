from telethon import TelegramClient as Client,events
import asyncio
num=918318986538
bot=Client(f'sessions/{num}',api_id='26094266',api_hash='4e1b477203976969b56ef26477afe775')
channels=[1496705628,1357275556,1433606813,1514109014,1687952246,1450755585,1348625748]
async def connect():
    if not bot.is_user_authorized():
        try:
            await bot.start(phone=num)
        except Exception as e:
            print(e)
    await bot.connect()
    async with bot:
        await bot.run_until_disconnected()
@bot.on(events.NewMessage(incoming=True))
async def forward(event):
    try:
        if event.original_update.message.peer_id.channel_id in channels:
            print(event.original_update.message)
            await bot.forward_messages("Deals_01_bot",event.original_update.message)
    except:
        pass
if __name__=='__main__':
    asyncio.run(connect())
