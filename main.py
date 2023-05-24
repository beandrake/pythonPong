from turtle import Screen
import math
from queue import Queue
from paddle import Paddle
from ball import Ball
import time

class Pong:
	def __init__(self):
		self.gameActive = True
		# Screen
		self.screen = Screen()
		self.screen.bgcolor("black")
		self.screen.setup(width=800, height=600)
		self.screen.title("Pong")
		self.screen.tracer(0)	# turn off automatic drawing updates (we'll call them manually)
		self.timeAtBeginningOfMostRecentGameObjectUpdate = time.time()

		# initialize paddles
		self.leftPaddle = Paddle(-350, 'a', 'z')
		self.rightPaddle = Paddle(350, 'Up', 'Down')

		# initialize ball
		self.ball = Ball()
		
		self.gameObjectList = [self.leftPaddle, self.rightPaddle, self.ball]

		# After game pieces are initialized
		self.screen.onkeypress(self.quitProgram, 'q')
		self.screen.listen()
		self.newGame()


	def gameLoop(self):
		timeAtLoopStart = time.time()
		totalNumLoops = 0
		numberOfFrameTimes = 100
		mostRecentFrameTimes = Queue(maxsize=numberOfFrameTimes)

		# let's try to update movement 30 times a second to normalize the experience
		self.currentlyUpdatingGameObjects = False
		self.millisecondsPerFrame = math.floor(1000/30)
		#self.screen.ontimer(self.updateGameObjects, 1000)

		while self.gameActive:
			timeCapture = time.time()
			timeSincePreviousLoopStarted = timeCapture - timeAtLoopStart
			timeAtLoopStart = timeCapture
		
			# stuff to calculate frames per second
			if mostRecentFrameTimes.full():
				oldestFrameTime = mostRecentFrameTimes.get()
				timeSinceOldestFrame = timeAtLoopStart - oldestFrameTime
				if timeSinceOldestFrame != 0:
					framesPerSecond = numberOfFrameTimes / timeSinceOldestFrame
				else:
					framesPerSecond = "Infinite"
			mostRecentFrameTimes.put(timeAtLoopStart)

			self.updateGameObjects()
			self.screen.update()
			
			totalNumLoops += 1



	def newGame(self):
		#screen.tracer(0)
		self.leftPaddle.resetLocation()
		self.rightPaddle.resetLocation()
		self.ball.resetLocation()
		#screen.tracer(1)

	def updateGameObjects(self):
		# Don't overlap updates (may not be necessary anymore)
		if self.currentlyUpdatingGameObjects:
			return

		# Update only X times per second
		secondsSinceLastUpdate = time.time() - self.timeAtBeginningOfMostRecentGameObjectUpdate
		if  secondsSinceLastUpdate*1000 < self.millisecondsPerFrame:
			return

		self.timeAtBeginningOfMostRecentGameObjectUpdate = time.time()
		self.currentlyUpdatingGameObjects = True

		for gameObject in self.gameObjectList:
			gameObject.update()

		#if self.gameActive:
		#	self.screen.ontimer(self.updateGameObjects, self.millisecondsPerFrame)
			
		self.currentlyUpdatingGameObjects = False


	def quitProgram(self ):		
		self.gameActive = False


if __name__ == '__main__':
	pongGame = Pong()
	pongGame.gameLoop()










