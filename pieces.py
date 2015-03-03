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

blockSpriteA = sprite.Sprite(blockImage, x=WIDTH/2, y=HEIGHT)
blockSpriteB = sprite.Sprite(blockImage, x=(WIDTH/2) + 36, y=HEIGHT)
blockSpriteC = sprite.Sprite(blockImage, x=(WIDTH/2) + 36*2, y=HEIGHT)
blockSpriteD = sprite.Sprite(blockImage, x=(WIDTH/2) + 36*3, y=HEIGHT)
blockSpriteE = sprite.Sprite(blockImage, x=WIDTH/2, y=(HEIGHT - 36))
blockSpriteF = sprite.Sprite(blockImage, x=(WIDTH/2) + 36, y=(HEIGHT - 36))
blockSpriteG = sprite.Sprite(blockImage, x=(WIDTH/2) + 36*2, y=(HEIGHT - 36))
blockSpriteH = sprite.Sprite(blockImage, x=(WIDTH/2) + 36*3, y=(HEIGHT - 36))

y = HEIGHT #this is top of screen
x = WIDTH / 2 #this is center of screen

class piece(object):
	def __init__(self, x, y):
		self.block = {'A':blockSpriteA}
		self.x = x
		self.y = y

	def fall(self):
		if self.y > BOTTOM:
			self.y -= MOVMENT_CONSTANT
			self.block['A'].set_position(x=self.x, y=self.y)
		else:
			self.y = HEIGHT
		print 'Y:', self.y
		return False

	def movePieceLeft(self):
		if self.x > 0:
			self.x -= MOVMENT_CONSTANT
			self.block['A'].set_position(x=self.x, y=self.y)
		print 'X:', self.x
		return False

	def movePieceRight(self):
		if self.x < WIDTH - MOVMENT_CONSTANT:
			self.x += MOVMENT_CONSTANT
			self.block['A'].set_position(x=self.x, y=self.y)
		print 'X:', self.x
		return False

	def rotatePiece(self):
		print 'Rotate'
		return False

class twoxtwo(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.block = {'C':blockSpriteC, 'D':blockSpriteD, 'G':blockSpriteG, 'H':blockSpriteH}
		gameBatch.add

	def fall(self):
		if self.y > BOTTOM:
			self.y -= MOVMENT_CONSTANT
			self.block['C'].set_position(x=self.block['C'].x, y=self.y)
			self.block['D'].set_position(x=self.block['D'].x, y=self.y)
			self.block['G'].set_position(x=self.block['G'].x, y=(self.y - 36))
			self.block['H'].set_position(x=self.block['H'].x, y=(self.y - 36))
		else:
			self.y = HEIGHT

	def movePieceLeft(self):
		if self.x > 0:
			self.x -= MOVMENT_CONSTANT
			self.block['C'].set_position(x=self.x + 36*2, y=self.block['C'].y)
			self.block['D'].set_position(x=self.x + 36*3, y=self.block['D'].y)
			self.block['G'].set_position(x=self.x + 36*2, y=self.block['G'].y)
			self.block['H'].set_position(x=self.x + 36*3, y=self.block['H'].y)

	def movePieceRight(self):
		if self.x < WIDTH - MOVMENT_CONSTANT:
			self.x += MOVMENT_CONSTANT
			self.block['C'].set_position(x=self.x + 36*2, y=self.block['C'].y)
			self.block['D'].set_position(x=self.x + 36*3, y=self.block['D'].y)
			self.block['G'].set_position(x=self.x + 36*2, y=self.block['G'].y)
			self.block['H'].set_position(x=self.x + 36*3, y=self.block['H'].y)

piece = twoxtwo(x, y)

def fall(dt):
    piece.fall()

def movePieceLeft():
	piece.movePieceLeft()

def movePieceRight():
	piece.movePieceRight()

def rotatePiece():
	piece.rotatePiece()