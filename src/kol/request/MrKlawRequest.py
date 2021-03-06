from kol.request.GenericRequest import GenericRequest
from kol.request import ParseResponseUtils

class MrKlawRequest(GenericRequest):
	"Uses Mr. Klaw in the rumpus room"
	def __init__(self, session):
		super(MrKlawRequest, self).__init__(session)
		self.url = session.serverURL + 'clan_rumpus.php?action=click&spot=3&furni=3'

	def parseResponse(self):
		response = ParseResponseUtils.parseItemsReceived(self.session, self.responseText)
			
		self.responseData = response
