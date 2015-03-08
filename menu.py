from constants import *

from pyglet import graphics
from pyglet import image as pygletImage
from pyglet import sprite

class Image(object):
	def __init__(self, image, xPos, yPos, batch, animation=None):
		self.image = pygletImage.load(image)
		self.imageWidth = self.image.width
		self.imageHeight = self.image.height
		self.sprite = sprite.Sprite(self.image, x=xPos, y=yPos, batch=batch)
		self.animation = animation

	def deleteSprite(self):
		self.sprite.delete()

	def animate(self):
	#TODO<yousif>: You might only need to define this here and not in each object of image
		pass

class Title(Image):
	def animate(self, image):
	#TODO<youisf>: image could be gif
		pass

class Button(Image):
	def ifAbove(self, xMouse, yMouse):
		#figure out the x and y boundaries of the button
		xBoundary = 0
		yBoundary = 0
		return (xBoundary <= xMouse <= (xBoundary + self.imageWidth)) and (yBoundary <= yMouse <= (yBoundary + self.imageHeight))

	def animate(self, image):	
	#TODO<youisf>: image could be gif
		pass

class Centerbutton(Button):
	pass

class Menu(object):
	#TODO<yousif>:What is the reference to the positiong of the menu items
	#				Title: TOP/CENTER
	#				Button: Based on Number of Buttons and type of menu
	#				MainMenu: Center
	#				PauseMenu: Depends
	#				OptionsMenu?

	def __init__(self, width, height):
		self.batch = graphics.Batch()
		self.title = None
		self.buttons = []

	def addTitle(self, image, xPos, yPos):
		self.title = Title(image, xPos, yPos, batch=self.batch)

	def addButton(self, image, xPos, yPos):
		self.buttons.append(Button(image, xPos, yPos, batch=self.batch))

	#How to check if button is being clicked all the time? without lag inside menu

	def draw(self):
		self.batch.draw()

	def delete(self):
		if self.title != None:
			self.title.deleteSprite()
		for button in self.buttons:
			button.deleteSprite()