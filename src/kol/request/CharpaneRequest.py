from GenericRequest import GenericRequest
from kol.manager import PatternManager

class CharpaneRequest(GenericRequest):
	"Requests the user's character pane."
	
	def __init__(self, session):
		super(CharpaneRequest, self).__init__(session)
		self.url = session.serverURL + 'charpane.php'

	def parseResponse(self):
		characterLevelPattern = PatternManager.getOrCompilePattern('characterLevel')		
		match = characterLevelPattern.search(self.responseText)
		if match:
			self.responseData["level"] = int(match.group(1))
		
		characterHPPattern = PatternManager.getOrCompilePattern('characterHP')
		match = characterHPPattern.search(self.responseText)
		if match:
			self.responseData["currentHP"] = int(match.group(1))
			self.responseData["maxHP"] = int(match.group(2))
		
		characterMPPattern = PatternManager.getOrCompilePattern('characterMP')
		match = characterMPPattern.search(self.responseText)
		if match:
			self.responseData["currentMP"] = int(match.group(1))
			self.responseData["maxMP"] = int(match.group(2))
		
		characterMeatPattern = PatternManager.getOrCompilePattern('characterMeat')
		match = characterMeatPattern.search(self.responseText)
		if match:
			self.responseData["meat"] = int(match.group(1).replace(',', ''))
		
		characterAdventuresPattern = PatternManager.getOrCompilePattern('characterAdventures')
		match = characterAdventuresPattern.search(self.responseText)
		if match:
			self.responseData["adventures"] = int(match.group(1))
		
		