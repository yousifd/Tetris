from constants import *

from pyglet import graphics
from pyglet import image
from pyglet import sprite

gameBatch = graphics.Batch()

blockImage = image.load('block.png')

blockSprite = sprite.Sprite(blockImage, x=WIDTH/2, y=HEIGHT, batch=gameBatch)

block = {'A':blockSprite} #this is Block
y = HEIGHT #this is top of screen
x = WIDTH / 2 #this is center of screen

def fall(dt):
    global y
    
    if y > BOTTOM:
	y -= MOVMENT_CONSTANT
	block['A'].set_position(x=x, y=y)
	print 'Y:', y
    else:
        y = HEIGHT

def movePieceLeft():
	global x, y
	
	if x > 0:
		x -= MOVMENT_CONSTANT
		block['A'].set_position(x=x, y=y)
		print 'X:', x

def movePieceRight():
	global x, y

	if x < WIDTH - MOVMENT_CONSTANT:
		x += MOVMENT_CONSTANT
		block['A'].set_position(x=x, y=y)
		print 'X:', x

def rotatePiece():
	print 'Rotate'