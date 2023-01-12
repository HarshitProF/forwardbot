from telethon import TelegramClient , events
import asyncio
api=26094266
phone=918318986538
hash="4e1b477203976969b56ef26477afe775"
client=TelegramClient('Harshit', api, hash)
channels=[1496705628,1357275556,1433606813,1514109014,1687952246,1450755585,1348625748]
def number () :
	return phone
def connect() :
	if not client.is_user_authorized() :
		try:
			client.start(phone=number())
		except Exception as e :
			print(e) 
	client.connect() 
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
	
if __name__=="__main__" :
	connect() 
	#client.connect() 
	with client:
		client.run_until_disconnected() 

