from constants import *

from pyglet import graphics
from pyglet import image
from pyglet import sprite

gameBatch = graphics.Batch()

blockImage = image.load('block.png')

blockSprite = sprite.Sprite(blockImage, x=WIDTH/2, y=HEIGHT, batch=gameBatch)

block = {'A':blockSprite} #this is Block