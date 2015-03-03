from constants import *

from pyglet import graphics
from pyglet import image
from pyglet import sprite

gameBatch = graphics.Batch()

y = HEIGHT #this is top of screen
x = WIDTH / 2 #this is center of screen

class piece:
	def __init__(self, x, y):
		self.blockImage = image.load('block.png')
		self.blockSprite = sprite.Sprite(self.blockImage, x=WIDTH/2, y=HEIGHT, batch=gameBatch)
		self.block = {'A':self.blockSprite}
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

piece = piece(x, y)

def fall(dt):
    piece.fall()

def movePieceLeft():
	piece.movePieceLeft()

def movePieceRight():
	piece.movePieceRight()

def rotatePiece():
	piece.rotatePiece()