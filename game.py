import abc	# abstract class stuff
#from gameObject import GameObject

class Game:
	def __init__(self):
		self.gameObjectList = []
		self.collisionObjectList = []
	
	def registerCollisionObject(self, newObject):
		self.collisionObjectList.append(newObject)
		self.registerGameObject(newObject)

	def registerGameObject(self, newObject):
		self.gameObjectList.append(newObject)
	