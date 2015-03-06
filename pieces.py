#A B C D
#E F G H

#E A
#F B
#G C 
#H D

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

		self.ROTATE_CONSTANT_Ax = 0
		self.ROTATE_CONSTANT_Ay = 0

		self.ROTATE_CONSTANT_Cx = 0
		self.ROTATE_CONSTANT_Cy = 0

		self.ROTATE_CONSTANT_Dx = 0
		self.ROTATE_CONSTANT_Dy = 0

		self.ROTATE_CONSTANT_Ex = 0
		self.ROTATE_CONSTANT_Ey = 0

		self.ROTATE_CONSTANT_Fx = 0
		self.ROTATE_CONSTANT_Fy = 0

		self.ROTATE_CONSTANT_Gx = 0
		self.ROTATE_CONSTANT_Gy = 0

		self.ROTATE_CONSTANT_BOTTOM = BOTTOM
		self.ROTATE_CONSTANT_LEFT = 0

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

	def fallBlock(self, sprite, y, x):
		sprite.set_position(x=x, y=y)

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

		self.ROTATE_CONSTANT_RIGHT = WIDTH - BLOCKLENGTH*4

	def fall(self):
		if self.y > self.ROTATE_CONSTANT_BOTTOM:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.I_shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
								self.x + self.ROTATE_CONSTANT_Ax)
			self.fallBlock(self.I_shape['B'], self.y, self.x + BLOCKLENGTH)
			self.fallBlock(self.I_shape['C'], self.y + self.ROTATE_CONSTANT_Cy, 
								self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)
			self.fallBlock(self.I_shape['D'], self.y + self.ROTATE_CONSTANT_Dy,
								self.x + BLOCKLENGTH*3 + self.ROTATE_CONSTANT_Dx)

	def shiftLeft(self):
		if self.x > self.ROTATE_CONSTANT_LEFT:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.I_shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.I_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.I_shape['C'], self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.I_shape['D'], self.x + BLOCKLENGTH*3 + self.ROTATE_CONSTANT_Dx)

	def shiftRight(self):
		if self.x < self.ROTATE_CONSTANT_RIGHT:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.I_shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.I_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.I_shape['C'], self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.I_shape['D'], self.x + BLOCKLENGTH*3 + self.ROTATE_CONSTANT_Dx)

	def rotatePiece(self):
		if self.ROTATE_CONSTANT_Ax == 0:
			self.ROTATE_CONSTANT_Ax = BLOCKLENGTH
			self.ROTATE_CONSTANT_Ay = BLOCKLENGTH

			self.ROTATE_CONSTANT_Cx = -BLOCKLENGTH
			self.ROTATE_CONSTANT_Cy = -BLOCKLENGTH

			self.ROTATE_CONSTANT_Dx = -2*BLOCKLENGTH
			self.ROTATE_CONSTANT_Dy = -2*BLOCKLENGTH

			self.ROTATE_CONSTANT_BOTTOM += 2*BLOCKLENGTH
			self.ROTATE_CONSTANT_RIGHT = WIDTH - 2*BLOCKLENGTH
			self.ROTATE_CONSTANT_LEFT = -BLOCKLENGTH

		else:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT - BLOCKLENGTH:
				self.ROTATE_CONSTANT_Ax = 0
				self.ROTATE_CONSTANT_Ay = 0

				self.ROTATE_CONSTANT_Cx = 0
				self.ROTATE_CONSTANT_Cy = 0

				self.ROTATE_CONSTANT_Dx = 0
				self.ROTATE_CONSTANT_Dy = 0

				self.ROTATE_CONSTANT_BOTTOM = BOTTOM
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 4*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = 0

		self.fallBlock(self.I_shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
							self.x + self.ROTATE_CONSTANT_Ax)

		self.fallBlock(self.I_shape['C'], self.y + self.ROTATE_CONSTANT_Cy, 
							self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)

		self.fallBlock(self.I_shape['D'], self.y + self.ROTATE_CONSTANT_Dy,
							self.x + BLOCKLENGTH*3 + self.ROTATE_CONSTANT_Dx)

#----------------------------------------------------------------------			
class L_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.L_shape = {'E':0, 'A':0, 'B':0, 'C':0}
		piece.generatePiece(self, self.L_shape)

		self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH

	def fall(self):
		if self.y > BOTTOM + BLOCKLENGTH:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.L_shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
									self.x + self.ROTATE_CONSTANT_Ax)
			self.fallBlock(self.L_shape['B'], self.y, self.x)
			self.fallBlock(self.L_shape['C'], self.y + self.ROTATE_CONSTANT_Cy,
									self.x + self.ROTATE_CONSTANT_Cx)
			self.fallBlock(self.L_shape['E'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Ey, 
									self.x + self.ROTATE_CONSTANT_Ex)

	def shiftLeft(self):
		if self.x > 0:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.L_shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.L_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.L_shape['C'], self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.L_shape['E'], self.x + self.ROTATE_CONSTANT_Ex)

	def shiftRight(self):
		if self.x < WIDTH - BLOCKLENGTH*3:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.L_shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.L_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.L_shape['C'], self.x + BLOCKLENGTH*2 +self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.L_shape['E'], self.x + self.ROTATE_CONSTANT_Ex)

	def rotatePiece(self):
		if self.ROTATE_CONSTANT_Ax == 0:
			self.ROTATE_CONSTANT_Ax = BLOCKLENGTH
			self.ROTATE_CONSTANT_Ay = BLOCKLENGTH

			self.ROTATE_CONSTANT_Cx = -BLOCKLENGTH
			self.ROTATE_CONSTANT_Cy = -BLOCKLENGTH

			self.ROTATE_CONSTANT_Ey = BLOCKLENGTH

			#WE ARE WHO WE ARE
			#DO NOT FORGET OTHER 
			self.ROTATE_CONSTANT_LEFT = -BLOCKLENGTH
			self.ROTATE_CONSTANT_BOTTOM += BLOCKLENGTH

			self.ROTATE_CONSTANT_RIGHT = WIDTH - 2*BLOCKLENGTH

		else:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT - BLOCKLENGTH:
				self.ROTATE_CONSTANT_Ax = 0
				self.ROTATE_CONSTANT_Ay = 0

				self.ROTATE_CONSTANT_Cx = 0
				self.ROTATE_CONSTANT_Cy = 0

				self.ROTATE_CONSTANT_Ex = 0
				self.ROTATE_CONSTANT_Ey = 0

				self.ROTATE_CONSTANT_BOTTOM = BOTTOM
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 4*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = 0

		self.fallBlock(self.I_shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
							self.x + self.ROTATE_CONSTANT_Ax)

		self.fallBlock(self.I_shape['C'], self.y + self.ROTATE_CONSTANT_Cy, 
							self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)

		self.fallBlock(self.I_shape['D'], self.y + self.ROTATE_CONSTANT_Dy,
							self.x + BLOCKLENGTH*3 + self.ROTATE_CONSTANT_Dx)
#----------------------------------------------------------------------
class J_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.J_shape = {'A':0, 'B':0, 'C':0, 'G':0}
		piece.generatePiece(self, self.J_shape)

	def fall(self):
		if self.y > BOTTOM + BLOCKLENGTH:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.J_shape['A'], self.y)
			self.fallBlock(self.J_shape['B'], self.y)
			self.fallBlock(self.J_shape['C'], self.y)
			self.fallBlock(self.J_shape['G'], self.y - BLOCKLENGTH)

	def shiftLeft(self):
		if self.x > 0:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.J_shape['A'], self.x)
			self.shiftBlock(self.J_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.J_shape['C'], self.x + 2*BLOCKLENGTH)
			self.shiftBlock(self.J_shape['G'], self.x + 2*BLOCKLENGTH)

	def shiftRight(self):
		if self.x < WIDTH - 3*BLOCKLENGTH:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.J_shape['A'], self.x)
			self.shiftBlock(self.J_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.J_shape['C'], self.x + 2*BLOCKLENGTH)
			self.shiftBlock(self.J_shape['G'], self.x + 2*BLOCKLENGTH)
#----------------------------------------------------------------------
class Z_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.Z_shape = {'A':0, 'B':0, 'F':0, 'G':0}
		piece.generatePiece(self, self.Z_shape)

		self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
		self.ROTATE_CONSTANT_BOTTOM = BLOCKLENGTH

	def fall(self):
		if self.y > self.ROTATE_CONSTANT_BOTTOM:
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.Z_shape['A'], self.y + self.ROTATE_CONSTANT_Ay,
									self.x + self.ROTATE_CONSTANT_Ax)
			self.fallBlock(self.Z_shape['B'], self.y, self.x + BLOCKLENGTH)
			self.fallBlock(self.Z_shape['F'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Fy,
									self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
			self.fallBlock(self.Z_shape['G'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Gy,
									self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)

	def shiftLeft(self):
		if self.x > self.ROTATE_CONSTANT_LEFT:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.Z_shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.Z_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.Z_shape['F'], self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
			self.shiftBlock(self.Z_shape['G'], self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)

	def shiftRight(self):
		if self.x < self.ROTATE_CONSTANT_RIGHT:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.Z_shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.Z_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.Z_shape['F'], self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
			self.shiftBlock(self.Z_shape['G'], self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)

	def rotatePiece(self):
		if self.ROTATE_CONSTANT_Ax == 0:
			self.ROTATE_CONSTANT_Ax = BLOCKLENGTH
			self.ROTATE_CONSTANT_Ay = BLOCKLENGTH

			self.ROTATE_CONSTANT_Fx = -BLOCKLENGTH
			self.ROTATE_CONSTANT_Fy = BLOCKLENGTH

			self.ROTATE_CONSTANT_Gx = -2*BLOCKLENGTH

			self.ROTATE_CONSTANT_BOTTOM += BLOCKLENGTH
			self.ROTATE_CONSTANT_RIGHT = WIDTH - 2*BLOCKLENGTH
			self.ROTATE_CONSTANT_LEFT = 0

		else:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT:
				self.ROTATE_CONSTANT_Ax = 0
				self.ROTATE_CONSTANT_Ay = 0

				self.ROTATE_CONSTANT_Fx = 0
				self.ROTATE_CONSTANT_Fy = 0

				self.ROTATE_CONSTANT_Gx = 0

				self.ROTATE_CONSTANT_BOTTOM = BLOCKLENGTH
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = 0

		self.fallBlock(self.Z_shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
							self.x + self.ROTATE_CONSTANT_Ax)

		self.fallBlock(self.Z_shape['F'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Fy, 
							self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)

		self.fallBlock(self.Z_shape['G'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Gy,
							self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)
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


piece = Z_shape(CENTER, TOP)

def fall(dt):
    piece.fall()

def movePieceLeft():
	piece.shiftLeft()

def movePieceRight():
	piece.shiftRight()

def rotatePiece():
	piece.rotatePiece()