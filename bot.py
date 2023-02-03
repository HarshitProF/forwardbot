from telethon import TelegramClient , events
from telethon.sessions import StringSession
string=
import asyncio
api=26094266
phone=918318986538
hash="4e1b477203976969b56ef26477afe775"
client=TelegramClient(StringSession(string) , api, hash)
channels=[1496705628,1357275556,1433606813,1514109014,1687952246,1450755585,1348625748]
def number () :
	return phone
async def connect() :
	await client.connect() 
	if not await client.is_user_authorized() :
		try:
			await client.start(phone=number())
		except Exception as e :
			print(e) 
	async with client:
		await client.run_until_disconnected() 
#connect () 

def check(events) :
	"""
			return True
		else :
			return False
	except:
		return False"""
	
@client.on(events.NewMessage(incoming=True  )) 
async def messa(event) :
	try:
		if event.original_update.message.peer_id.channel_id in channels:
			print(event.original_update.message) 
			await client.forward_messages("Deals_01_bot",  event.original_update.message) 
	except:
		pass
	
def main() :
	asyncio.run(connect()) 
main() 

