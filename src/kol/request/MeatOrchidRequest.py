from kol.request.GenericRequest import GenericRequest
from kol.request import ParseResponseUtils

"""
Note that we do not parse for messages indicating you've already used the orchid.  If no meat is retrieved, it will return just an empty dictionary.
"""

class MeatOrchidRequest(GenericRequest):
	"Visits the hanging meat orchid in the clan rumpus room"
	def __init__(self, session):
		super(MeatOrchidRequest, self).__init__(session)
		self.url = session.serverURL + 'clan_rumpus.php?action=click&spot=1&furni=4'

	def parseResponse(self):
		response = {}
		response["meat"] = ParseResponseUtils.parseMeatReceived(self.responseText)
		
		self.responseData = response
