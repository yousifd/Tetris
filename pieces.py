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
#----------------------------------------------------------------------
class O_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.O_shape = {'C':0, 'D':0, 'G':0, 'H':0}
		piece.generatePiece(self, self.O_shape)

	def fall(self):
		if self.y > BOTTOM + BLOCKLENGTH:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.O_shape['C'], self.y)
			self.fallBlock(self.O_shape['D'], self.y)
			self.fallBlock(self.O_shape['G'], self.y - BLOCKLENGTH)
			self.fallBlock(self.O_shape['H'], self.y - BLOCKLENGTH)

	def shiftLeft(self):
		if self.x > 0 - 2*BLOCKLENGTH:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.O_shape['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.O_shape['D'], self.x + BLOCKLENGTH*3)
			self.shiftBlock(self.O_shape['G'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.O_shape['H'], self.x + BLOCKLENGTH*3)

	def shiftRight(self):
		if self.x < WIDTH - BLOCKLENGTH*4:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.O_shape['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.O_shape['D'], self.x + BLOCKLENGTH*3)
			self.shiftBlock(self.O_shape['G'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.O_shape['H'], self.x + BLOCKLENGTH*3)
#---------------------------------------------------------------------
class I_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.I_shape = {'A':0, 'B':0, 'C':0, 'D':0}
		piece.generatePiece(self, self.I_shape)

	def fall(self):
		if self.y > BOTTOM:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.I_shape['A'], self.y)
			self.fallBlock(self.I_shape['B'], self.y)
			self.fallBlock(self.I_shape['C'], self.y)
			self.fallBlock(self.I_shape['D'], self.y)

	def shiftLeft(self):
		if self.x > 0:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.I_shape['A'], self.x)
			self.shiftBlock(self.I_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.I_shape['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.I_shape['D'], self.x + BLOCKLENGTH*3)

	def shiftRight(self):
		if self.x < WIDTH - BLOCKLENGTH*4:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.I_shape['A'], self.x)
			self.shiftBlock(self.I_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.I_shape['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.I_shape['D'], self.x + BLOCKLENGTH*3)
#----------------------------------------------------------------------			
class L_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.L_shape = {'A':0, 'B':0, 'C':0, 'E':0}
		piece.generatePiece(self, self.L_shape)

	def fall(self):
		if self.y > BOTTOM + BLOCKLENGTH:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.L_shape['A'], self.y)
			self.fallBlock(self.L_shape['B'], self.y)
			self.fallBlock(self.L_shape['C'], self.y)
			self.fallBlock(self.L_shape['E'], self.y - BLOCKLENGTH)

	def shiftLeft(self):
		if self.x > 0:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.L_shape['A'], self.x)
			self.shiftBlock(self.L_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.L_shape['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.L_shape['E'], self.x)

	def shiftRight(self):
		if self.x < WIDTH - BLOCKLENGTH*3:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.L_shape['A'], self.x)
			self.shiftBlock(self.L_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.L_shape['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.L_shape['E'], self.x)
#----------------------------------------------------------------------
class J_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.J_shape = {'A':0, 'E':0, 'F':0, 'G':0}
		piece.generatePiece(self, self.J_shape)

	def fall(self):
		if self.y > BOTTOM + BLOCKLENGTH:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.J_shape['A'], self.y)
			self.fallBlock(self.J_shape['E'], self.y - BLOCKLENGTH)
			self.fallBlock(self.J_shape['F'], self.y - BLOCKLENGTH)
			self.fallBlock(self.J_shape['G'], self.y - BLOCKLENGTH)

	def shiftLeft(self):
		if self.x > 0:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.J_shape['A'], self.x)
			self.shiftBlock(self.J_shape['E'], self.x)
			self.shiftBlock(self.J_shape['F'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.J_shape['G'], self.x + BLOCKLENGTH*2)

	def shiftRight(self):
		if self.x < WIDTH - BLOCKLENGTH*3:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.J_shape['A'], self.x)
			self.shiftBlock(self.J_shape['E'], self.x)
			self.shiftBlock(self.J_shape['F'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.J_shape['G'], self.x + BLOCKLENGTH*2)
#----------------------------------------------------------------------
class Z_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.Z_shape = {'A':0, 'B':0, 'F':0, 'G':0}
		piece.generatePiece(self, self.Z_shape)

	def fall(self):
		if self.y > BOTTOM + BLOCKLENGTH:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.Z_shape['A'], self.y)
			self.fallBlock(self.Z_shape['B'], self.y)
			self.fallBlock(self.Z_shape['F'], self.y - BLOCKLENGTH)
			self.fallBlock(self.Z_shape['G'], self.y - BLOCKLENGTH)

	def shiftLeft(self):
		if self.x > 0:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.Z_shape['A'], self.x)
			self.shiftBlock(self.Z_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.Z_shape['F'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.Z_shape['G'], self.x + BLOCKLENGTH*2)

	def shiftRight(self):
		if self.x < WIDTH - BLOCKLENGTH*3:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.Z_shape['A'], self.x)
			self.shiftBlock(self.Z_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.Z_shape['F'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.Z_shape['G'], self.x + BLOCKLENGTH*2)
#----------------------------------------------------------------------
class S_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.S_shape = {'E':0, 'F':0, 'B':0, 'C':0}
		piece.generatePiece(self, self.S_shape)

	def fall(self):
		if self.y > BOTTOM + BLOCKLENGTH:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.S_shape['E'], self.y - BLOCKLENGTH)
			self.fallBlock(self.S_shape['F'], self.y - BLOCKLENGTH)
			self.fallBlock(self.S_shape['B'], self.y)
			self.fallBlock(self.S_shape['C'], self.y)

	def shiftLeft(self):
		if self.x > 0:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.S_shape['E'], self.x)
			self.shiftBlock(self.S_shape['F'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.S_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.S_shape['C'], self.x + BLOCKLENGTH*2)

	def shiftRight(self):
		if self.x < WIDTH - BLOCKLENGTH*3:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.S_shape['E'], self.x)
			self.shiftBlock(self.S_shape['F'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.S_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.S_shape['C'], self.x + BLOCKLENGTH*2)
#----------------------------------------------------------------------
class T_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.T_shape = {'B':0, 'E':0, 'F':0, 'G':0}
		piece.generatePiece(self, self.T_shape)

	def fall(self):
		if self.y > BOTTOM + BLOCKLENGTH:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.T_shape['B'], self.y)
			self.fallBlock(self.T_shape['E'], self.y - BLOCKLENGTH)
			self.fallBlock(self.T_shape['F'], self.y - BLOCKLENGTH)
			self.fallBlock(self.T_shape['G'], self.y - BLOCKLENGTH)

	def shiftLeft(self):
		if self.x > 0:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.T_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.T_shape['E'], self.x)
			self.shiftBlock(self.T_shape['F'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.T_shape['G'], self.x + BLOCKLENGTH*2)

	def shiftRight(self):
		if self.x < WIDTH - BLOCKLENGTH*3:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.T_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.T_shape['E'], self.x)
			self.shiftBlock(self.T_shape['F'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.T_shape['G'], self.x + BLOCKLENGTH*2)
#---------------------------------------------------------------------


piece = T_shape(CENTER, TOP)

def fall(dt):
    piece.fall()

def movePieceLeft():
	piece.shiftLeft()

def movePieceRight():
	piece.shiftRight()

def rotatePiece():
	piece.rotatePiece()