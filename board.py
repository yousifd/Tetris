from constants import *
from pieces import *

import time

from pyglet import clock

# COMPLETED:

# Clear completed lines<Ebrahim>
# Score system<Ebrahim>
# Finish game<Ebrahim>
# Fix wait time until block is allowed to not move<Yousif>
# Pause game<Yousif>
# Enable hold on down button<Yousif>

# TODO:

# Implement Game UI
# Implement Switching the current piece with the next one
# Add Background
# Add instant falling
# Make options menu
# Audio
# Add more controls: Example?
# Speed option
# Increase Speed after completeting a set number of lines
# Animation 

class Board(object):
	def __init__(self):

		self.piece = generatePiece()

		self.storedSprites = []
		# WTF?
		# self.grayBlock = image.load('Gray.png')

		self.oldTime = time.time()

		self.i = 0

		self.completedLines = 0
		self.score = 0 

		self.gameStop = True

		self.removeLines = []
		self.deleteRows = [] 

		def zero():
			c = [1]
			for i in range(20):
				c.append(0)
			return c

		self.ctemp = zero()

		self.c0 = zero()
		self.c1 = zero()
		self.c2 = zero()
		self.c3 = zero()
		self.c4 = zero()
		self.c5 = zero()
		self.c6 = zero()
		self.c7 = zero()
		self.c8 = zero()
		self.c9 = zero()

		self.columns = [self.ctemp, self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9, self.c0, self.ctemp, self.ctemp, self.ctemp]

	def timeSinceLastMovement(self, time):
		return time - self.oldTime > 0.01

	def checkSteps(self):
		return self.i >= 1

	def relativePiecePositionX(self, key):
		return self.piece.shape[key].x / BLOCKLENGTH

	def relativePiecePositionY(self, key):
		return self.piece.shape[key].y / BLOCKLENGTH

	def pieceColumn(self, key, block=1):
		if self.relativePiecePositionX(key) == 0:
			return self.columns[0 + block]
		elif self.relativePiecePositionX(key) == 1:
			return self.columns[1 + block]
		elif self.relativePiecePositionX(key) == 2:
			return self.columns[2 + block]
		elif self.relativePiecePositionX(key) == 3:
			return self.columns[3 + block]
		elif self.relativePiecePositionX(key) == 4:
			return self.columns[4 + block]
		elif self.relativePiecePositionX(key) == 5:
			return self.columns[5 + block]
		elif self.relativePiecePositionX(key) == 6:
			return self.columns[6 + block]
		elif self.relativePiecePositionX(key) == 7:
			return self.columns[7 + block]
		elif self.relativePiecePositionX(key) == 8:
			return self.columns[8 + block]
		elif self.relativePiecePositionX(key) == 9:
			return self.columns[9 + block]
		else:
			 return self.ctemp

	def checkBelow(self):
		for key in self.piece.shape:
			if self.pieceColumn(key)[self.relativePiecePositionY(key)] != 0:
				return False
		return True

	def checkLeft(self):
		for key in self.piece.shape:
			if self.pieceColumn(key, 0)[self.relativePiecePositionY(key) + 1] != 0:
				return False
		return True

	def checkRight(self):
		for key in self.piece.shape:
			if self.pieceColumn(key, 2)[self.relativePiecePositionY(key) + 1] != 0:
				return False
		return True

	def checkSuroundings(self):
		return self.checkBelow() and self.checkRight() and self.checkLeft()

	def checkLine(self, row):
		isLineFull = True
		for column in self.columns[1:11]:
			columnTemp = column[1:]
			if columnTemp[row] == 0:
				isLineFull = False
		print 'isLineFull in this row:', row, '?', isLineFull, '\n'
		return isLineFull

	def linesToBeRemoved(self):
		self.completedLines = 0
		self.removeLines = []

		for key in self.piece.shape:
			print 'self.relativePiecePositionY(key): ', self.relativePiecePositionY(key)
			if self.checkLine(self.relativePiecePositionY(key)):
				if self.relativePiecePositionY(key) not in self.removeLines:
					self.removeLines.append(self.relativePiecePositionY(key))

					self.completedLines += 1

		for i in self.removeLines:
			print 'removeLine: ', i

	def removeLine(self):
		for row in reversed(sorted(self.removeLines)):
			for column in self.columns[1:11]:
				del column[row + 1]
				column.append(0)

	def removeBlcoks(self):
		if self.removeLines:
			# Turn block color gray before deleting them
			# for Y in reversed(sorted(self.removeLines)):
			# 	for s in self.storedSprites:
			# 		if s.y == (Y * 36):
			# 			self.storedSprites[self.storedSprites.index(s)] = sprite.Sprite(self.grayBlock, x=s.x, y=s.y, batch=gameBatch)

			for i in range(5):
				for Y in reversed(sorted(self.removeLines)):
					for s in self.storedSprites:
						if float(s.y) == float(Y * BLOCKLENGTH):
							del self.storedSprites[self.storedSprites.index(s)]

			for Y in reversed(sorted(self.removeLines)):
				for s in self.storedSprites:
					if float(s.y) > float(Y * BLOCKLENGTH):
						s.y -= BLOCKLENGTH	

	def scoring(self):
		if self.completedLines == 1:
			self.score += 40 
		elif self.completedLines == 2:
			self.score += 100
		elif self.completedLines == 3:
			self.score += 300
		elif self.completedLines == 4:
			self.score += 1200

	def isGameOver(self):
		game = True
		for column in self.columns[1:11]:
			if column[18] == 1:
				game = False

		if not game:
			self.gameStop = True
			print 'Game Over! Your score is', self.score

	def fall(self, dt):
		self.isGameOver()

		if self.checkBelow():
			self.piece.fall()
			self.oldTime = time.time()
		elif self.timeSinceLastMovement(time.time()) or self.checkSteps():
			self.i = 0

			for key in self.piece.shape:
				self.pieceColumn(key)[self.relativePiecePositionY(key) + 1] = 1
				self.storedSprites.append(sprite.Sprite(self.piece.block, x=self.piece.shape[key].x, y=self.piece.shape[key].y, batch=gameBatch))
			
			self.linesToBeRemoved()
			self.removeLine()
			self.removeBlcoks()

			self.scoring()
			# print 'score: ', self.score

			for i in self.columns[1:11]:
				print i
						
			self.piece = generatePiece()

	def fallFaster(self, dt):
		self.fall(dt)

	def movePieceLeft(self):
		if self.checkLeft():
			self.piece.shiftLeft()
			self.oldTime = time.time()
			self.i += 1

	def movePieceRight(self):
		if self.checkRight():
			self.piece.shiftRight()
			self.oldTime = time.time()
			self.i += 1

	def rotatePiece(self, dt):
		if self.checkSuroundings():
			self.piece.rotatePiece()
			self.oldTime = time.time()









