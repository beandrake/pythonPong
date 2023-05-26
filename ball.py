from turtle import Turtle
from gameObject import GameObject

class Ball(Turtle, GameObject):
	
	def __init__(self, positionX=0, positionY=0, pixelsPerSecondX=15, pixelsPerSecondY=15):
		super().__init__()
		self.positionX = positionX
		self.positionY = positionY
		self.pixelsPerSecondX = pixelsPerSecondX
		self.pixelsPerSecondY = pixelsPerSecondY

		# initialize aesthetic
		self.shape('square')
		self.shapesize(stretch_wid=1, stretch_len=1)
		self.color('white')
		self.penup()
		self.resetLocation()

	def update(self, secondsSinceLastUpdate):
		self.move(secondsSinceLastUpdate)


	def move(self, secondsSinceLastUpdate):
		newX = self.xcor() + (self.pixelsPerSecondX * secondsSinceLastUpdate)
		newY = self.ycor() + (self.pixelsPerSecondY * secondsSinceLastUpdate)
		self.goto(newX, newY)

		if self.pixelsPerSecondX > 0 and newX > self.screen.canvwidth		\
		   or 																\
		   self.pixelsPerSecondX < 0 and newX < -self.screen.canvwidth:
			self.pixelsPerSecondX = -self.pixelsPerSecondX
		
		if self.pixelsPerSecondY > 0 and newY > self.screen.canvheight		\
		   or 																\
		   self.pixelsPerSecondY < 0 and newY < -self.screen.canvheight:
			self.pixelsPerSecondY = -self.pixelsPerSecondY


	def resetLocation(self):
		self.goto(self.positionX, self.positionY)
