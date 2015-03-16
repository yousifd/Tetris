from constants import *
from pieces import *

class Board(object):
	def __init__(self):
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


		self.columns = [self.ctemp, self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9, self.ctemp]

	def relativePiecePositionX(self, piece):
		return piece.position('row') / BLOCKLENGTH

	def relativePiecePositionY(slef, piece):
		return piece.position('column') / BLOCKLENGTH

	def pieceColumn(self, piece, block=1):
		if self.relativePiecePositionX(piece) == 0:
			return self.columns[0 + block]
		elif self.relativePiecePositionX(piece) == 1:
			return self.columns[1 + block]
		elif self.relativePiecePositionX(piece) == 2:
			return self.columns[2 + block]
		elif self.relativePiecePositionX(piece) == 3:
			return self.columns[3 + block]
		elif self.relativePiecePositionX(piece) == 4:
			return self.columns[4 + block]
		elif self.relativePiecePositionX(piece) == 5:
			return self.columns[5 + block]
		elif self.relativePiecePositionX(piece) == 6:
			return self.columns[6 + block]
		elif self.relativePiecePositionX(piece) == 7:
			return self.columns[7 + block]
		elif self.relativePiecePositionX(piece) == 8:
			return self.columns[8 + block]
		elif self.relativePiecePositionX(piece) == 9:
			return self.columns[9 + block]
		else:
			print 'Something is really wrong with us!'

	def checkBelow(self, piece):
		# Check index below
		if self.pieceColumn(piece)[self.relativePiecePositionY(piece)] == 0:
			return True
		else:
			return False

	def checkLeft(self, piece):
		if self.pieceColumn(piece, 0)[self.relativePiecePositionY(piece)] == 0:
			return True
		else:
			return False

	def checkRight(self, piece):
		if self.pieceColumn(piece, 2)[self.relativePiecePositionY(piece)] == 0:
			return True
		else:
			return False

board = Board()

def fall(dt, piece):
    if board.checkBelow(piece):
    	piece.fall()
    else:
    	board.pieceColumn(piece)[board.relativePiecePositionY(piece)] = 1

def movePieceLeft(piece):
	if board.checkLeft(piece):
		piece.shiftLeft()

def movePieceRight(piece):
	if board.checkRight(piece):
		piece.shiftRight()

def rotatePiece(piece):
	piece.rotatePiece()