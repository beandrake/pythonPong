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

		# Should the framerate be capped?  Early experiments show that this looks icky.
		self.capFrameRate = False
		self.cappedFramesPerSecond = 60
		self.cappedSecondsPerFrame = 1 / self.cappedFramesPerSecond
		self.timeAtBeginningOfMostRecentScreenDraw = time.time()

		# initialize paddles
		paddleSpeed = (self.screen.canvheight*2) / 2	# should take a bit less than 2 seconds to move from top to bottom (note: canvheight is only half the height)
		self.leftPaddle = Paddle(-350, 'a', 'z', paddleSpeed)
		self.rightPaddle = Paddle(350, 'Up', 'Down', paddleSpeed)

		# initialize ball
		ballSpeed = paddleSpeed * 1.5	# let's make the ball faster than paddles
		self.ball = Ball(pixelsPerSecondX = ballSpeed, pixelsPerSecondY = ballSpeed)
		
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

		while self.gameActive:
			timeCapture = time.time()
			timeSincePreviousLoopStarted = timeCapture - timeAtLoopStart
			timeAtLoopStart = timeCapture
		
			# stuff to calculate average frames per second over 100 frames
			if mostRecentFrameTimes.full():
				oldestFrameTime = mostRecentFrameTimes.get()
				timeSinceOldestFrame = timeAtLoopStart - oldestFrameTime
				if timeSinceOldestFrame != 0:
					framesPerSecond = numberOfFrameTimes / timeSinceOldestFrame
				else:
					framesPerSecond = "Infinite"
			mostRecentFrameTimes.put(timeAtLoopStart)

			self.updateGameObjects()
			
			totalNumLoops += 1


	def newGame(self):
		self.leftPaddle.resetLocation()
		self.rightPaddle.resetLocation()
		self.ball.resetLocation()


	def updateGameObjects(self):
		# We want objects to move at constant rates per unit of time regardless of framerate, 
		# so we detect the time delta since the previous frame so that objects can update proportionally.
		secondsSinceLastUpdate = time.time() - self.timeAtBeginningOfMostRecentGameObjectUpdate
		self.timeAtBeginningOfMostRecentGameObjectUpdate = time.time()

		for gameObject in self.gameObjectList:
			gameObject.update(secondsSinceLastUpdate)

		if not self.capFrameRate:
			self.screen.update()
		else:
			secondsSinceLastScreenDraw = time.time() - self.timeAtBeginningOfMostRecentScreenDraw
			if secondsSinceLastScreenDraw >= self.cappedSecondsPerFrame:
				self.timeAtBeginningOfMostRecentScreenDraw = time.time()
				self.screen.update()


	def quitProgram(self ):		
		self.gameActive = False


if __name__ == '__main__':
	pongGame = Pong()
	pongGame.gameLoop()










