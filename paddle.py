from turtle import Turtle
from gameObject import GameObject

class Paddle(Turtle, GameObject):
		
	Y_MAX = 200
	Y_MIN = -200
	
	def __init__(self, xPosition, upKey, downKey):
		super().__init__()

		self.xPosition = xPosition
		self.upKey = upKey
		self.downKey = downKey
		self.upKeyPressed = False
		self.downKeyPressed = False
		self.movementDistance = 1

		# initialize aesthetic
		self.shape('square')
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.color('white')
		self.penup()
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
	
	def update(self):
		if self.upKeyPressed != self.downKeyPressed:
			if self.upKeyPressed:
				self.moveUp()
			else:
				self.moveDown()


	def moveUp(self):
		if self.ycor() < Paddle.Y_MAX:
			newY = self.ycor() + self.movementDistance
			self.goto(self.xcor(), newY)

	def moveDown(self):
		if self.ycor() > Paddle.Y_MIN:
			newY = self.ycor() - self.movementDistance
			self.goto(self.xcor(), newY)

	def resetLocation(self):
		self.goto(self.xPosition, 0)