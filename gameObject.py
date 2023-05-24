import abc	# abstract class stuff

class GameObject(abc.ABC):
	@abc.abstractmethod
	def update(self):
		pass