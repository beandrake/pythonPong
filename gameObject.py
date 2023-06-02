import abc	# abstract class stuff

class GameObject(abc.ABC):
	def __init__(self, mainGameObject=None):
		super().__init__()
		self.mainGameObject = mainGameObject

		# register self with game
		if self.mainGameObject is not None:
			self.mainGameObject.registerGameObject(self)
	
	
	@abc.abstractmethod
	def update(self, secondsSinceLastUpdate):
		pass