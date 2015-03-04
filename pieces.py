#A B C D
#E F G H

# make blocks
# make function that randomly chooses blocks
# Size of play area 10x18 blocks

from constants import *

from pyglet import graphics
from pyglet import image
from pyglet import sprite

gameBatch = graphics.Batch()

blockImage = image.load('block.png')

class piece(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def generatePiece(self, dic):
		for key in dic:
			if key == 'A':
				dic[key] = sprite.Sprite(blockImage, x=CENTER, y=TOP, batch=gameBatch)
			elif key == 'B':
				dic[key] = sprite.Sprite(blockImage, x=CENTER + BLOCKLENGTH, y=TOP, batch=gameBatch)
			elif key == 'C':
				dic[key] = sprite.Sprite(blockImage, x=CENTER + BLOCKLENGTH*2, y=TOP, batch=gameBatch)
			elif key == 'D':
				dic[key] = sprite.Sprite(blockImage, x=CENTER + BLOCKLENGTH*3, y=TOP, batch=gameBatch)
			elif key == 'E':
				dic[key] = sprite.Sprite(blockImage, x=CENTER, y=(TOP - BLOCKLENGTH), batch=gameBatch)
			elif key == 'F':
				dic[key] = sprite.Sprite(blockImage, x=CENTER + BLOCKLENGTH, y=(TOP - BLOCKLENGTH), batch=gameBatch)
			elif key == 'G':
				dic[key] = sprite.Sprite(blockImage, x=CENTER + BLOCKLENGTH*2, y=(TOP - BLOCKLENGTH), batch=gameBatch)
			elif key == 'H':
				dic[key] = sprite.Sprite(blockImage, x=CENTER + BLOCKLENGTH*3, y=(TOP - BLOCKLENGTH), batch=gameBatch)
			else:
				print "Invalid Piece Key!"

	def fall(self):
		return False

	def movePieceLeft(self):
		return False

	def movePieceRight(self):
		return False

	def rotatePiece(self):
		print 'Rotate'
		return False

class twoxtwo(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.twoxtwo= {'C':0, 'D':0, 'G':0, 'H':0}
		piece.generatePiece(self, self.twoxtwo)

	def fall(self):
		if self.y > BOTTOM + BLOCKLENGTH:
			self.y -= MOVMENT_CONSTANT
			self.twoxtwo['C'].set_position(x=self.twoxtwo['C'].x, y=self.y)
			self.twoxtwo['D'].set_position(x=self.twoxtwo['D'].x, y=self.y)
			self.twoxtwo['G'].set_position(x=self.twoxtwo['G'].x, y=(self.y - BLOCKLENGTH))
			self.twoxtwo['H'].set_position(x=self.twoxtwo['H'].x, y=(self.y - BLOCKLENGTH))

	def movePieceLeft(self):
		if self.x > 0 - 2*BLOCKLENGTH:
			self.x -= MOVMENT_CONSTANT
			self.twoxtwo['C'].set_position(x=self.x + BLOCKLENGTH*2, y=self.twoxtwo['C'].y)
			self.twoxtwo['D'].set_position(x=self.x + BLOCKLENGTH*3, y=self.twoxtwo['D'].y)
			self.twoxtwo['G'].set_position(x=self.x + BLOCKLENGTH*2, y=self.twoxtwo['G'].y)
			self.twoxtwo['H'].set_position(x=self.x + BLOCKLENGTH*3, y=self.twoxtwo['H'].y)

	def movePieceRight(self):
		if self.x < CENTER + BLOCKLENGTH:
			self.x += MOVMENT_CONSTANT
			self.twoxtwo['C'].set_position(x=self.x + BLOCKLENGTH*2, y=self.twoxtwo['C'].y)
			self.twoxtwo['D'].set_position(x=self.x + BLOCKLENGTH*3, y=self.twoxtwo['D'].y)
			self.twoxtwo['G'].set_position(x=self.x + BLOCKLENGTH*2, y=self.twoxtwo['G'].y)
			self.twoxtwo['H'].set_position(x=self.x + BLOCKLENGTH*3, y=self.twoxtwo['H'].y)

piece = twoxtwo(CENTER, TOP)

def fall(dt):
    piece.fall()

def movePieceLeft():
	piece.movePieceLeft()

def movePieceRight():
	piece.movePieceRight()

def rotatePiece():
	piece.rotatePiece()