from turtle import Turtle
from gameObject import GameObject

class Ball(Turtle, GameObject):
	
	def __init__(self, positionX=0, positionY=0, velocityX=1, velocityY=1):
		super().__init__()
		self.positionX = positionX
		self.positionY = positionY
		self.velocityX = velocityX
		self.velocityY = velocityY

		# initialize aesthetic
		self.shape('square')
		self.shapesize(stretch_wid=1, stretch_len=1)
		self.color('white')
		self.penup()
		self.resetLocation()

	def update(self):
		self.move()


	def move(self):
		newX = self.xcor() + self.velocityX
		newY = self.ycor() + self.velocityY
		self.goto(newX, newY)

		if newX > self.screen.canvwidth or newX < -self.screen.canvwidth:
			self.velocityX = - self.velocityX

		if newY > self.screen.canvheight or newY < -self.screen.canvheight:
			self.velocityY = - self.velocityY

	def resetLocation(self):
		self.goto(self.positionX, self.positionY)
