from constants import *
from pieces import *

from pyglet import clock

class Board(object):
	def __init__(self):

		self.piece = generatePiece()

		self.storedSprites = []

		def zero():
			c = [1]
			for i in range(18):
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

		self.columns = [self.ctemp, self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9, self.ctemp, self.ctemp, self.ctemp]


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
			if self.pieceColumn(key, 0)[self.relativePiecePositionY(key)] != 0:
				return False
		return True

	def checkRight(self):
		for key in self.piece.shape:
			if self.pieceColumn(key, 2)[self.relativePiecePositionY(key)] != 0:
				return False
		return True

	def checkSuroundings(self):
		return self.checkBelow() and self.checkRight() and self.checkLeft()

	def fall(self, dt):
	    if self.checkBelow():
			self.piece.fall()
	    else:
			for key in self.piece.shape:
				self.pieceColumn(key)[self.relativePiecePositionY(key) + 1] = 1
				self.storedSprites.append(sprite.Sprite(blockImage, x=self.piece.shape[key].x, y=self.piece.shape[key].y, batch=gameBatch))

			self.piece = generatePiece()

	def movePieceLeft(self):
		if self.checkLeft():
			self.piece.shiftLeft()

	def movePieceRight(self):
		if self.checkRight():
			self.piece.shiftRight()

	def rotatePiece(self):
		if self.checkSuroundings():
			self.piece.rotatePiece()









