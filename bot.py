from telethon import TelegramClient , events
from telethon.sessions import StringSession
string="1BVtsOKUBu6Widi8nNVr797UWZZF6B5XQqJkQMC528iYoNazEIyBB9rSMfbd3pt7dDbZl8Vei070CL0KM4KYnIu_SlzYXauWcDh-ibkWtcRfDG1ti3GuofAlGXsAUWpXEawtO32wv01vBNJOsQxnLQs6Msi3j1xoVp_2_x2UXGz_l93RUIvflDyTn_d8A8kiEnA1sj5MCeMVheBwVivK0JiMmiNfNBM_5EwBecJnQkH_KYXI2BMZvqO6Fjts1RULtLsWPCGr_W2HqgQcfGbYLMN0gwUvdWT8Eifup5CcejNNXSCCinYx7TFrB_7Ty19j4Qk01Wpv7HHDmKDybznv-FfULszSMDec="
import asyncio
api=26094266
phone=918318986538
hash="4e1b477203976969b56ef26477afe775"
client=TelegramClient(StringSession(string) , api, hash)
channels=[1496705628,1357275556,1433606813,1514109014,1687952246,1450755585,1348625748]
def number () :
	return phone
def connect() :
	client.connect() 
	if not await client.is_user_authorized() :
		try:
			client.start(phone=number())
		except Exception as e :
			print(e) 
	with client:
		client.run_until_disconnected() 
#connect () 

def check(events) :
	"""
			return True
		else :
			return False
	except:
		return False"""
	
@client.on(events.NewMessage(incoming=True  )) 
def messa(event) :
	try:
		if event.original_update.message.peer_id.channel_id in channels:
			print(event.original_update.message) 
			client.forward_messages("Deals_01_bot",  event.original_update.message) 
	except:
		pass
	
#connect() 
if __name__=="__main__":
    connect() 
