from turtle import Turtle
from collisionObject import CollisionObject

class Paddle(CollisionObject):
		
	Y_MAX = 200
	Y_MIN = -200
	
	def __init__(self, xPosition, upKey, downKey, pixelsPerSecond = 10, mainGameObject=None):
		super().__init__(mainGameObject)

		self.xPosition = xPosition
		self.upKey = upKey
		self.downKey = downKey
		self.upKeyPressed = False
		self.downKeyPressed = False
		self.pixelsPerSecond = pixelsPerSecond

		# initialize aesthetic
		self.shapesize(stretch_wid=1, stretch_len=5)
		self.color('white')
		self.resetLocation()

		# initialize listeners
		self.screen.onkeypress(self.setUpKeyPressed, self.upKey)
		self.screen.onkeyrelease(self.setUpKeyReleased, self.upKey)
		self.screen.onkeypress(self.setDownKeyPressed, self.downKey)
		self.screen.onkeyrelease(self.setDownKeyReleased, self.downKey)


	def setUpKeyPressed(self):
		self.upKeyPressed = True

	def setUpKeyReleased(self):
		self.upKeyPressed = False
	def setDownKeyPressed(self):
		self.downKeyPressed = True

	def setDownKeyReleased(self):
		self.downKeyPressed = False
	
	def update(self, secondsSinceLastUpdate):
		if self.upKeyPressed != self.downKeyPressed:
			if self.upKeyPressed:
				self.moveUp(secondsSinceLastUpdate)
			else:
				self.moveDown(secondsSinceLastUpdate)


	def moveUp(self, secondsSinceLastUpdate):
		if self.ycor() < Paddle.Y_MAX:
			newY = self.ycor() + (self.pixelsPerSecond * secondsSinceLastUpdate)
			self.goto(self.xcor(), newY)

	def moveDown(self, secondsSinceLastUpdate):
		if self.ycor() > Paddle.Y_MIN:
			newY = self.ycor() - (self.pixelsPerSecond * secondsSinceLastUpdate)
			self.goto(self.xcor(), newY)

	def resetLocation(self):
		self.goto(self.xPosition, 0)