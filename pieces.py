#A B C D
#E F G H

#E A
#F B
#G C 
#H D

# # Size of play area 10x18 blocks

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

		self.rotationNumber = 0

	def generatePiece(self, dic):
		for key in dic:
			dic[key] = sprite.Sprite(blockImage, x=CENTER, y=TOP, batch=gameBatch)

	def fallBlock(self, sprite, y, x):
		sprite.set_position(x=x, y=y)

	def shiftBlock(self, sprite, x):
		sprite.set_position(x=x, y=sprite.y)

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
		self.shape = {'C':0, 'D':0, 'G':0, 'H':0}
		piece.generatePiece(self, self.shape)

	def fall(self):
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.shape['C'], self.y)
			self.fallBlock(self.shape['D'], self.y)
			self.fallBlock(self.shape['G'], self.y - BLOCKLENGTH)
			self.fallBlock(self.shape['H'], self.y - BLOCKLENGTH)

	def shiftLeft(self):
		if self.x > 0 - 2*BLOCKLENGTH:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.shape['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.shape['D'], self.x + BLOCKLENGTH*3)
			self.shiftBlock(self.shape['G'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.shape['H'], self.x + BLOCKLENGTH*3)

	def shiftRight(self):
		if self.x < WIDTH - BLOCKLENGTH*4:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.shape['C'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.shape['D'], self.x + BLOCKLENGTH*3)
			self.shiftBlock(self.shape['G'], self.x + BLOCKLENGTH*2)
			self.shiftBlock(self.shape['H'], self.x + BLOCKLENGTH*3)
#---------------------------------------------------------------------
class I_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.shape = {'A':0, 'B':0, 'C':0, 'D':0}
		piece.generatePiece(self, self.shape) 

		self.ROTATE_CONSTANT_RIGHT = WIDTH - BLOCKLENGTH*4

	def fall(self):
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
								self.x + self.ROTATE_CONSTANT_Ax)
			self.fallBlock(self.shape['B'], self.y, self.x + BLOCKLENGTH)
			self.fallBlock(self.shape['C'], self.y + self.ROTATE_CONSTANT_Cy, 
								self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)
			self.fallBlock(self.shape['D'], self.y + self.ROTATE_CONSTANT_Dy,
								self.x + BLOCKLENGTH*3 + self.ROTATE_CONSTANT_Dx)

	def shiftLeft(self):
		if self.x > self.ROTATE_CONSTANT_LEFT:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.shape['C'], self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.shape['D'], self.x + BLOCKLENGTH*3 + self.ROTATE_CONSTANT_Dx)

	def shiftRight(self):
		if self.x < self.ROTATE_CONSTANT_RIGHT:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.shape['C'], self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.shape['D'], self.x + BLOCKLENGTH*3 + self.ROTATE_CONSTANT_Dx)

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

		self.fallBlock(self.shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
							self.x + self.ROTATE_CONSTANT_Ax)

		self.fallBlock(self.shape['C'], self.y + self.ROTATE_CONSTANT_Cy, 
							self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)

		self.fallBlock(self.shape['D'], self.y + self.ROTATE_CONSTANT_Dy,
							self.x + BLOCKLENGTH*3 + self.ROTATE_CONSTANT_Dx)

#----------------------------------------------------------------------			
class L_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.L_shape = {'E':0, 'A':0, 'B':0, 'C':0}
		piece.generatePiece(self, self.L_shape)

		self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH

	def fall(self):
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.L_shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
									self.x + self.ROTATE_CONSTANT_Ax)
			self.fallBlock(self.L_shape['B'], self.y, self.x + BLOCKLENGTH)
			self.fallBlock(self.L_shape['C'], self.y + self.ROTATE_CONSTANT_Cy,
									self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)
			self.fallBlock(self.L_shape['E'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Ey, 
									self.x + self.ROTATE_CONSTANT_Ex)

	def shiftLeft(self):
		if self.x > self.ROTATE_CONSTANT_LEFT:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.L_shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.L_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.L_shape['C'], self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.L_shape['E'], self.x + self.ROTATE_CONSTANT_Ex)

	def shiftRight(self):
		if self.x < self.ROTATE_CONSTANT_RIGHT:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.L_shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.L_shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.L_shape['C'], self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.L_shape['E'], self.x + self.ROTATE_CONSTANT_Ex)

	def rotatePiece(self):

	
		if self.rotationNumber == 0:
			self.ROTATE_CONSTANT_Ax = BLOCKLENGTH
			self.ROTATE_CONSTANT_Ay = BLOCKLENGTH

			self.ROTATE_CONSTANT_Cx = -BLOCKLENGTH
			self.ROTATE_CONSTANT_Cy = -BLOCKLENGTH

			self.ROTATE_CONSTANT_Ex = 0
			self.ROTATE_CONSTANT_Ey = 2*BLOCKLENGTH

			
			self.rotationNumber = 1
			self.ROTATE_CONSTANT_BOTTOM = BOTTOM 
			self.ROTATE_CONSTANT_RIGHT = WIDTH - 2*BLOCKLENGTH
			self.ROTATE_CONSTANT_LEFT = 0
			
				# E A
				#   B
				#   C

		elif self.rotationNumber == 1:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT:
				self.ROTATE_CONSTANT_Ax = 2*BLOCKLENGTH
				self.ROTATE_CONSTANT_Ay = 0

				self.ROTATE_CONSTANT_Cx = -2*BLOCKLENGTH
				self.ROTATE_CONSTANT_Cy = 0

				self.ROTATE_CONSTANT_Ex = 2*BLOCKLENGTH
				self.ROTATE_CONSTANT_Ey = 2*BLOCKLENGTH

				self.ROTATE_CONSTANT_BOTTOM = BOTTOM 
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = 0

				self.rotationNumber = 2

					#     E
					# C B A
	
		elif self.rotationNumber == 2:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT:
				self.ROTATE_CONSTANT_Ax = BLOCKLENGTH
				self.ROTATE_CONSTANT_Ay = -BLOCKLENGTH

				self.ROTATE_CONSTANT_Cx = -BLOCKLENGTH
				self.ROTATE_CONSTANT_Cy = BLOCKLENGTH

				self.ROTATE_CONSTANT_Ex = 2*BLOCKLENGTH
				self.ROTATE_CONSTANT_Ey = 0

				self.ROTATE_CONSTANT_BOTTOM = BOTTOM 
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = -BLOCKLENGTH

				self.rotationNumber = 3

					# C
					# B 
					# A E

		elif self.rotationNumber == 3:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT:
				self.ROTATE_CONSTANT_Ax = 0
				self.ROTATE_CONSTANT_Ay = 0

				self.ROTATE_CONSTANT_Cx = 0
				self.ROTATE_CONSTANT_Cy = 0

				self.ROTATE_CONSTANT_Ex = 0
				self.ROTATE_CONSTANT_Ey = 0

				self.ROTATE_CONSTANT_BOTTOM = BOTTOM
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = 0

				self.rotationNumber = 0

					#A B C
					#E

		self.fallBlock(self.shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
							self.x + self.ROTATE_CONSTANT_Ax)

		self.fallBlock(self.shape['C'], self.y + self.ROTATE_CONSTANT_Cy, 
							self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)

		self.fallBlock(self.shape['E'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Ey,
							self.x + self.ROTATE_CONSTANT_Ex)
#----------------------------------------------------------------------
class J_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.shape = {'A':0, 'B':0, 'C':0, 'G':0}
		piece.generatePiece(self, self.shape)

	def fall(self):
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
												self.x + self.ROTATE_CONSTANT_Ax)
			self.fallBlock(self.shape['B'], self.y, self.x + BLOCKLENGTH)
			self.fallBlock(self.shape['C'], self.y + self.ROTATE_CONSTANT_Cy,
												self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Cx)
			self.fallBlock(self.shape['G'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Gy, 
												self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)

	def shiftLeft(self):
		if self.x > self.ROTATE_CONSTANT_LEFT:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.shape['C'], self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.shape['G'], self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)

	def shiftRight(self):
		if self.x < self.ROTATE_CONSTANT_RIGHT:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.shape['C'], self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.shape['G'], self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)

	def rotatePiece(self):

	
		if self.rotationNumber == 0:
			self.ROTATE_CONSTANT_Ax = BLOCKLENGTH
			self.ROTATE_CONSTANT_Ay = BLOCKLENGTH

			self.ROTATE_CONSTANT_Cx = -BLOCKLENGTH
			self.ROTATE_CONSTANT_Cy = -BLOCKLENGTH

			self.ROTATE_CONSTANT_Gx = -2*BLOCKLENGTH
			self.ROTATE_CONSTANT_Gy = 0

			
			self.rotationNumber = 1
			self.ROTATE_CONSTANT_BOTTOM = BOTTOM 
			self.ROTATE_CONSTANT_RIGHT = WIDTH - 2*BLOCKLENGTH
			self.ROTATE_CONSTANT_LEFT = 0
			
				#   A
				#   B
				# G C

		elif self.rotationNumber == 1:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT:
				self.ROTATE_CONSTANT_Ax = 2*BLOCKLENGTH
				self.ROTATE_CONSTANT_Ay = 0

				self.ROTATE_CONSTANT_Cx = -2*BLOCKLENGTH
				self.ROTATE_CONSTANT_Cy = 0

				self.ROTATE_CONSTANT_Gx = -2*BLOCKLENGTH
				self.ROTATE_CONSTANT_Gy = 2*BLOCKLENGTH

				self.ROTATE_CONSTANT_BOTTOM = BOTTOM 
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = 0

				self.rotationNumber = 2

					# G
					# C B A
	
		elif self.rotationNumber == 2:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT:
				self.ROTATE_CONSTANT_Ax = BLOCKLENGTH
				self.ROTATE_CONSTANT_Ay = -BLOCKLENGTH

				self.ROTATE_CONSTANT_Cx = -BLOCKLENGTH
				self.ROTATE_CONSTANT_Cy = BLOCKLENGTH

				self.ROTATE_CONSTANT_Gx = 0
				self.ROTATE_CONSTANT_Gy = 2*BLOCKLENGTH

				self.ROTATE_CONSTANT_BOTTOM = BOTTOM 
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = -BLOCKLENGTH

				self.rotationNumber = 3

					# C G
					# B 
					# A 

		elif self.rotationNumber == 3:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT:
				self.ROTATE_CONSTANT_Ax = 0
				self.ROTATE_CONSTANT_Ay = 0

				self.ROTATE_CONSTANT_Cx = 0
				self.ROTATE_CONSTANT_Cy = 0

				self.ROTATE_CONSTANT_Gx = 0
				self.ROTATE_CONSTANT_Gy = 0

				self.ROTATE_CONSTANT_BOTTOM = BOTTOM
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = 0

				self.rotationNumber = 0

					#A B C
					#    G

		self.fallBlock(self.shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
							self.x + self.ROTATE_CONSTANT_Ax)

		self.fallBlock(self.shape['C'], self.y + self.ROTATE_CONSTANT_Cy, 
							self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)

		self.fallBlock(self.shape['G'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Gy,
							self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)
#----------------------------------------------------------------------
class Z_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.shape = {'A':0, 'B':0, 'F':0, 'G':0}
		piece.generatePiece(self, self.shape)

		self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
		self.ROTATE_CONSTANT_BOTTOM = BLOCKLENGTH

	def fall(self):
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.shape['A'], self.y + self.ROTATE_CONSTANT_Ay,
									self.x + self.ROTATE_CONSTANT_Ax)
			self.fallBlock(self.shape['B'], self.y, self.x + BLOCKLENGTH)
			self.fallBlock(self.shape['F'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Fy,
									self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
			self.fallBlock(self.shape['G'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Gy,
									self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)

	def shiftLeft(self):
		if self.x > self.ROTATE_CONSTANT_LEFT:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.shape['F'], self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
			self.shiftBlock(self.shape['G'], self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)

	def shiftRight(self):
		if self.x < self.ROTATE_CONSTANT_RIGHT:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.shape['A'], self.x + self.ROTATE_CONSTANT_Ax)
			self.shiftBlock(self.shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.shape['F'], self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
			self.shiftBlock(self.shape['G'], self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)

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

		self.fallBlock(self.shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
							self.x + self.ROTATE_CONSTANT_Ax)

		self.fallBlock(self.shape['F'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Fy, 
							self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)

		self.fallBlock(self.shape['G'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Gy,
							self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Gx)
#----------------------------------------------------------------------
class S_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.shape = {'E':0, 'F':0, 'B':0, 'C':0}
		piece.generatePiece(self, self.shape)

		self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
		self.ROTATE_CONSTANT_BOTTOM = BLOCKLENGTH

	def fall(self):
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.shape['E'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Ey,
								self.x + self.ROTATE_CONSTANT_Ex)
			self.fallBlock(self.shape['F'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Fy,
								self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
			self.fallBlock(self.shape['B'], self.y, self.x + BLOCKLENGTH)
			self.fallBlock(self.shape['C'], self.y + self.ROTATE_CONSTANT_Cy,
								self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Cx)

	def shiftLeft(self):
		if self.x > self.ROTATE_CONSTANT_LEFT:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.shape['E'], self.x + self.ROTATE_CONSTANT_Ex)
			self.shiftBlock(self.shape['F'], self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
			self.shiftBlock(self.shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.shape['C'], self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Cx)

	def shiftRight(self):
		if self.x < self.ROTATE_CONSTANT_RIGHT:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.shape['E'], self.x + self.ROTATE_CONSTANT_Ex)
			self.shiftBlock(self.shape['F'], self.x + BLOCKLENGTH  + self.ROTATE_CONSTANT_Fx)
			self.shiftBlock(self.shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.shape['C'], self.x + 2*BLOCKLENGTH  + self.ROTATE_CONSTANT_Cx)

	def rotatePiece(self):
		if self.ROTATE_CONSTANT_Fx == 0:
			self.ROTATE_CONSTANT_Ex = 0
			self.ROTATE_CONSTANT_Ey = 2*BLOCKLENGTH

			self.ROTATE_CONSTANT_Fx = -BLOCKLENGTH
			self.ROTATE_CONSTANT_Fy = BLOCKLENGTH

			self.ROTATE_CONSTANT_Cx = -BLOCKLENGTH
			self.ROTATE_CONSTANT_Cy = -BLOCKLENGTH

			self.ROTATE_CONSTANT_BOTTOM = BLOCKLENGTH
			self.ROTATE_CONSTANT_RIGHT = WIDTH - 2*BLOCKLENGTH
			self.ROTATE_CONSTANT_LEFT = 0
		else:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT:
				self.ROTATE_CONSTANT_Ex = 0
				self.ROTATE_CONSTANT_Ey = 0

				self.ROTATE_CONSTANT_Fx = 0
				self.ROTATE_CONSTANT_Fy = 0

				self.ROTATE_CONSTANT_Cx = 0
				self.ROTATE_CONSTANT_Cy = 0

				self.ROTATE_CONSTANT_BOTTOM = BLOCKLENGTH
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = 0

		self.fallBlock(self.shape['E'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Ey,
							self.x + self.ROTATE_CONSTANT_Ex)
		self.fallBlock(self.shape['F'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Fy,
							self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
		self.fallBlock(self.shape['B'], self.y, self.x + BLOCKLENGTH)
		self.fallBlock(self.shape['C'], self.y + self.ROTATE_CONSTANT_Cy,
							self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Cx)
#----------------------------------------------------------------------
class T_shape(piece):
	def __init__(self, x, y):
		piece.__init__(self, x, y)
		self.shape = {'A':0, 'B':0, 'C':0, 'F':0}
		piece.generatePiece(self, self.shape)

		self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
		self.ROTATE_CONSTANT_BOTTOM = BLOCKLENGTH

	def fall(self):
			self.y -= MOVMENT_CONSTANT
			self.fallBlock(self.shape['B'], self.y, self.x + BLOCKLENGTH)
			self.fallBlock(self.shape['C'], self.y + self.ROTATE_CONSTANT_Cy,
											self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Cx)
			self.fallBlock(self.shape['F'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Fy, 
											self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
			self.fallBlock(self.shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
											self.x + self.ROTATE_CONSTANT_Ax)

	def shiftLeft(self):
		if self.x > self.ROTATE_CONSTANT_LEFT:
			self.x -= MOVMENT_CONSTANT
			self.shiftBlock(self.shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.shape['C'], self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.shape['F'], self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
			self.shiftBlock(self.shape['A'], self.x + self.ROTATE_CONSTANT_Ax)

	def shiftRight(self):
		if self.x < self.ROTATE_CONSTANT_RIGHT:
			self.x += MOVMENT_CONSTANT
			self.shiftBlock(self.shape['B'], self.x + BLOCKLENGTH)
			self.shiftBlock(self.shape['C'], self.x + 2*BLOCKLENGTH + self.ROTATE_CONSTANT_Cx)
			self.shiftBlock(self.shape['F'], self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
			self.shiftBlock(self.shape['A'], self.x + self.ROTATE_CONSTANT_Ax)

	def rotatePiece(self):

	
		if self.rotationNumber == 0:
			self.ROTATE_CONSTANT_Ax = BLOCKLENGTH
			self.ROTATE_CONSTANT_Ay = BLOCKLENGTH

			self.ROTATE_CONSTANT_Cx = -BLOCKLENGTH
			self.ROTATE_CONSTANT_Cy = -BLOCKLENGTH

			self.ROTATE_CONSTANT_Fx = -BLOCKLENGTH
			self.ROTATE_CONSTANT_Fy = BLOCKLENGTH

			
			self.rotationNumber = 1
			self.ROTATE_CONSTANT_BOTTOM = BOTTOM 
			self.ROTATE_CONSTANT_RIGHT = WIDTH - 2*BLOCKLENGTH
			self.ROTATE_CONSTANT_LEFT = 0
			
				#   A
				# F B
				#   C

		elif self.rotationNumber == 1:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT:
				self.ROTATE_CONSTANT_Ax = 2*BLOCKLENGTH
				self.ROTATE_CONSTANT_Ay = 0

				self.ROTATE_CONSTANT_Cx = -2*BLOCKLENGTH
				self.ROTATE_CONSTANT_Cy = 0

				self.ROTATE_CONSTANT_Fx = 0
				self.ROTATE_CONSTANT_Fy = 2*BLOCKLENGTH

				self.ROTATE_CONSTANT_BOTTOM = BOTTOM 
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = 0

				self.rotationNumber = 2

					#   F
					# C B A
	
		elif self.rotationNumber == 2:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT:
				self.ROTATE_CONSTANT_Ax = BLOCKLENGTH
				self.ROTATE_CONSTANT_Ay = -BLOCKLENGTH

				self.ROTATE_CONSTANT_Cx = -BLOCKLENGTH
				self.ROTATE_CONSTANT_Cy = BLOCKLENGTH

				self.ROTATE_CONSTANT_Fx = BLOCKLENGTH
				self.ROTATE_CONSTANT_Fy = BLOCKLENGTH

				self.ROTATE_CONSTANT_BOTTOM = BOTTOM 
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = -BLOCKLENGTH

				self.rotationNumber = 3

					# C 
					# B F
					# A 

		elif self.rotationNumber == 3:
			if self.ROTATE_CONSTANT_LEFT < self.x < self.ROTATE_CONSTANT_RIGHT:
				self.ROTATE_CONSTANT_Ax = 0
				self.ROTATE_CONSTANT_Ay = 0

				self.ROTATE_CONSTANT_Cx = 0
				self.ROTATE_CONSTANT_Cy = 0

				self.ROTATE_CONSTANT_Fx = 0
				self.ROTATE_CONSTANT_Fy = 0

				self.ROTATE_CONSTANT_BOTTOM = BOTTOM
				self.ROTATE_CONSTANT_RIGHT = WIDTH - 3*BLOCKLENGTH
				self.ROTATE_CONSTANT_LEFT = 0

				self.rotationNumber = 0

					#A B C
					#  F 

		self.fallBlock(self.shape['A'], self.y + self.ROTATE_CONSTANT_Ay, 
							self.x + self.ROTATE_CONSTANT_Ax)

		self.fallBlock(self.shape['C'], self.y + self.ROTATE_CONSTANT_Cy, 
							self.x + BLOCKLENGTH*2 + self.ROTATE_CONSTANT_Cx)

		self.fallBlock(self.shape['F'], self.y - BLOCKLENGTH + self.ROTATE_CONSTANT_Fy,
							self.x + BLOCKLENGTH + self.ROTATE_CONSTANT_Fx)
#---------------------------------------------------------------------