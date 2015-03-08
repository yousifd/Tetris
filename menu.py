##create a class for a button that takes sprite and has attirubtes related to button
##if clicked based on the sprites attributes you should do what is expected
##Important Method: When clicked!
from constants import *

from pyglet import graphics
from pyglet import image as pygletImage
from pyglet import sprite

class Image(object):
	def __init__(self, image, xPos, yPos, batch):
		self.image = pygletImage.load(image)
		self.imageWidth = self.image.width
		self.imageHeight = self.image.height
		self.sprite = sprite.Sprite(self.image, x=xPos, y=yPos, batch=batch)

	def deleteSprite(self):
		self.sprite.delete()

class Button(Image):
	def ifAbove(self, xMouse, yMouse):
		#figure out the x and y boundaries of the button
		xBoundary = 0
		yBoundary = 0
		return (xBoundary <= xMouse <= (xBoundary + self.imageWidth)) and (yBoundary <= yMouse <= (yBoundary + self.imageHeight))

	def animate(self, image):
		pass

class Title(Image):
	def animate(self, image):
		pass

class Menu(object):
	def __init__(self, width, height):
		self.batch = graphics.Batch()
		self.title = None
		self.buttons = []

	def addTitle(self, image, xPos, yPos):
		self.title = Title(image, xPos, yPos, batch=self.batch)

	def addButton(self, image, xPos, yPos):
		self.buttons.append(Button(image, xPos, yPos, batch=self.batch))

	def draw(self):
		self.batch.draw()

	def delete(self):
		if self.title != None:
			self.title.deleteSprite()
		for button in self.buttons:
			button.deleteSprite()