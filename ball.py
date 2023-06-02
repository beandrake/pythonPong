from turtle import Turtle
from collisionObject import CollisionObject

class Ball(CollisionObject):
	
	def __init__(self, positionX=0, positionY=0, pixelsPerSecondX=15, pixelsPerSecondY=15, mainGameObject=None):
		super().__init__(mainGameObject)
		self.positionX = positionX
		self.positionY = positionY
		self.pixelsPerSecondX = pixelsPerSecondX
		self.pixelsPerSecondY = pixelsPerSecondY
		self.collisionObjectList = mainGameObject.collisionObjectList

		# initialize aesthetic
		self.shape('square')
		self.shapesize(stretch_wid=1, stretch_len=1)
		self.color('white')
		self.penup()
		self.resetLocation()


	def update(self, secondsSinceLastUpdate):
		self.move(secondsSinceLastUpdate)
		self.checkCollisionWithCollisionObjects()
		self.checkCollisionWithScreenEdges()


	def move(self, secondsSinceLastUpdate):
		newX = self.xcor() + (self.pixelsPerSecondX * secondsSinceLastUpdate)
		newY = self.ycor() + (self.pixelsPerSecondY * secondsSinceLastUpdate)
		self.goto(newX, newY)


	def checkCollisionWithCollisionObjects(self):
		for collisionObject in self.collisionObjectList:
			if collisionObject is not self and self.isCollidingWith(collisionObject):
				# Only bounce off something if you are moving in the direction of its center
				if (self.pixelsPerSecondX > 0 and self.xcor() < collisionObject.xcor())	\
				   or																	\
				   (self.pixelsPerSecondX < 0 and self.xcor() > collisionObject.xcor()):
					self.pixelsPerSecondX = -self.pixelsPerSecondX


	def checkCollisionWithScreenEdges(self):
		if (self.pixelsPerSecondX > 0 and self.xcor() > self.screen.canvwidth)		\
		   or 																		\
		   (self.pixelsPerSecondX < 0 and self.xcor() < -self.screen.canvwidth):
			self.pixelsPerSecondX = -self.pixelsPerSecondX
			# you could also put point logic here to keep score
		
		if (self.pixelsPerSecondY > 0 and self.ycor() > self.screen.canvheight)		\
		   or 																		\
		   (self.pixelsPerSecondY < 0 and self.ycor() < -self.screen.canvheight):
			self.pixelsPerSecondY = -self.pixelsPerSecondY


	def resetLocation(self):
		self.goto(self.positionX, self.positionY)
