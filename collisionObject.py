#import abc	# abstract class stuff
import turtle
from gameObject import GameObject

# Sets so Turtle objects initialize facing north and positive rotation values are clockwise.
turtle.mode('logo')

# CollisionObject assumes your object is a rectangle.  Out of respect, please do not not be a rectangle.
class CollisionObject(GameObject, turtle.Turtle):
	
	def __init__(self, mainGameObject=None):
		super().__init__(mainGameObject)	# this only calls GameObject because of MRO (see: https://rhettinger.wordpress.com/2011/05/26/super-considered-super/ )
		self.shape('square')
		self.penup()

		# register self with game
		if self.mainGameObject is not None:
			self.mainGameObject.registerCollisionObject(self)
	

	def getSides(self):		
		# positions are relative to object center, not screen center
		mySubjectiveCorners = self.get_shapepoly()
		myLowerRightCorner = mySubjectiveCorners[0]
		#myUpperRightCorner = mySubjectiveCorners[1]
		myUpperLeftCorner = mySubjectiveCorners[2]
		#myLowerLeftCorner = mySubjectiveCorners[3]
		
		myAbsoluteCenter = self.position()

		myAbsoluteLeft = myUpperLeftCorner[0] + myAbsoluteCenter[0]
		myAbsoluteTop = myUpperLeftCorner[1] + myAbsoluteCenter[1]
		myAbsoluteRight = myLowerRightCorner[0] + myAbsoluteCenter[0]
		myAbsoluteBottom = myLowerRightCorner[1] + myAbsoluteCenter[1]
		
		return myAbsoluteLeft, myAbsoluteTop, myAbsoluteRight, myAbsoluteBottom
	

	def isCollidingWith(self, otherCollisionObject):
		# Reference: https://stackoverflow.com/questions/31022269/collision-detection-between-two-rectangles-in-java
		myLeft, myTop, myRight, myBottom= self.getSides()
		yourLeft, yourTop, yourRight, yourBottom= otherCollisionObject.getSides()

		# Check for conditions that would prove the rectangles are NOT overlapping...
		notOverlapping =  myLeft > yourRight or myRight < yourLeft 				\
						  or myTop < yourBottom or myBottom > yourTop

		# ...then flip the result
		return not notOverlapping
		
