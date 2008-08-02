from kol.database import ItemDatabase
from kol.database import SkillDatabase
from kol.util import Report

import socket
import threading
import time

_bots = []
_haltEvent = None

def init(params=None):
	global _haltEvent
	
	# Create the event which can be used to halt all bots.
	_haltEvent = threading.Event()
	
	# Initialize the databases.
	ItemDatabase.init()
	SkillDatabase.init()
	
	# Force HTTP requests to timeout after 5 minutes.
	socket.setdefaulttimeout(300)

def registerBot(bot):
	_bots.append(bot)

def runBots():
	if len(_bots) > 1:
		Report.includeThreadName = True
	
	for bot in _bots:
		bot.start()
	
	try:
		while _haltEvent.isSet() == False:
			time.sleep(15)
	except KeyboardInterrupt:
		_haltEvent.set()
	
	Report.info("bot", "Shutting down.")
		
	for bot in _bots:
		bot.join()
