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

	def fallBlock(self, sprite, y):
		sprite.set_position(x=sprite.x, y=y)

	def shiftBlock(self, sprite, x):
		sprite.set_position(x=x, y=sprite.y)
		print x

	def fall(self):
		return False

	def shiftLeft(self):
		return False

	def shiftRight(self):
		return False

	def rotatePiece(self):
		print 'Rotate'
		return False

class twoxtwo(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.twoxtwo = {'C':0, 'D':0, 'G':0, 'H':0}
		piece.generatePiece(self, self.twoxtwo)

	def fall(self):
		if self.y > BOTTOM + BLOCKLENGTH:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.twoxtwo['C'], self.y)
			self.fallBlock(self.twoxtwo['D'], self.y)
			self.fallBlock(self.twoxtwo['G'], self.y - BLOCKLENGTH)
			self.fallBlock(self.twoxtwo['H'], self.y - BLOCKLENGTH)

	def shiftLeft(self):
		if self.x > 0 - 2*BLOCKLENGTH:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.twoxtwo['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.twoxtwo['D'], self.x + BLOCKLENGTH*3)
			self.shiftBlock(self.twoxtwo['G'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.twoxtwo['H'], self.x + BLOCKLENGTH*3)

	def shiftRight(self):
		if self.x < WIDTH - BLOCKLENGTH*4:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.twoxtwo['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.twoxtwo['D'], self.x + BLOCKLENGTH*3)
			self.shiftBlock(self.twoxtwo['G'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.twoxtwo['H'], self.x + BLOCKLENGTH*3)

class onexfour(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.onexfour = {'A':0, 'B':0, 'C':0, 'D':0}
		piece.generatePiece(self, self.onexfour)

	def fall(self):
		if self.y > BOTTOM:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.onexfour['A'], self.y)
			self.fallBlock(self.onexfour['B'], self.y)
			self.fallBlock(self.onexfour['C'], self.y)
			self.fallBlock(self.onexfour['D'], self.y)

	def shiftLeft(self):
		if self.x > 0:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.onexfour['A'], self.x)
			self.shiftBlock(self.onexfour['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.onexfour['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.onexfour['D'], self.x + BLOCKLENGTH*3)

	def shiftRight(self):
		if self.x < WIDTH - BLOCKLENGTH*4:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.onexfour['A'], self.x)
			self.shiftBlock(self.onexfour['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.onexfour['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.onexfour['D'], self.x + BLOCKLENGTH*3)


piece = twoxtwo(CENTER, TOP)

def fall(dt):
    piece.fall()

def movePieceLeft():
	piece.shiftLeft()

def movePieceRight():
	piece.shiftRight()

def rotatePiece():
	piece.rotatePiece()