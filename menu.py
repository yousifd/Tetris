
#CLEAN UP THE FREAKING CODE OR THIS WILL BE THE END OF YOU

from constants import *

from pyglet import graphics
from pyglet import image as pygletImage
from pyglet import sprite

class Image(object):
	def __init__(self, image, xPos, yPos, batch, animation=None):
		self.name = image.split('.')[0]
		self.image = pygletImage.load(image)
		self.imageWidth = self.image.width
		self.imageHeight = self.image.height
		self.sprite = sprite.Sprite(self.image, x=xPos, y=yPos, batch=batch)
		self.animate = animation

	def getImageName(self):
		return self.name

	def getImageWidth(self):
		return self.imageWidth

	def getImageHeight(self):
		return self.imageHeight

	def deleteSprite(self):
		self.sprite.delete()

	def animate(self):
		'''Switches between image and animate to create animation,
			the animate could be another image or gif'''
		if self.animate == None:
			print 'Image has no animation provided!'
			pass
		else:
			self.image=pygletImage.load(self.aniamte)
			#figure out how to return to original image

class Title(Image):
	pass

class Button(Image):
	def ifAbove(self, x, y):
		#figure out the x and y boundaries of the button
		xBoundary = 0
		yBoundary = 0
		return (xBoundary <= x <= (xBoundary + self.imageWidth)) and (yBoundary <= y <= (yBoundary + self.imageHeight))

class Menu(object):
	#TODO<yousif>:What is the reference to the positiong of the menu items
	#				Title: TOP/CENTER
	#				Button: Based on Number of Buttons and type of menu
	#				MainMenu: Center
	#				PauseMenu: Depends
	#				OptionsMenu?

	#need variable for the parameter of the freaking menu position on window
	#basically a constant used to figure out the position of the menu contents
	def __init__(self, menuWidth, menuHeight):
		'''Menu Width: width of menu
		   Menu Height: height of menu
		   Used as a relative for the position of the 
		   title and buttons

		   buttonShift: the shift of buttons from mid heigth'''
		self.batch = graphics.Batch()
		self.title = None
		self.buttons = []
		self.width = menuWidth
		self.height = menuHeight
		self.buttonShift = 0

	#add getButton() to use with ifAbove method
	#add ifAbove function for menus that use getButton()

	def addTitle(self, image, xPos, yPos):
		self.title = Title(image, xPos, yPos, batch=self.batch)

	def addButton(self, image, xPos, yPos):
		self.buttons.append(Button(image, xPos, yPos, batch=self.batch))

	def addCenterButton(self, image):
		##buttons are positioned based on the left-bottom most point in image
		#change xpos and ypos based on the number of buttons: use a new function
		self.addButton(image, self.width/2, self.height/2 + self.buttonShift)
		#move the buttons based on the number of buttons
		self.buttonShift -= self.buttons[-1].getImageHeight()

	def draw(self):
		self.batch.draw()

	def delete(self):
		if self.title != None:
			self.title.deleteSprite()
		if len(self.buttons) != 0:
			for button in self.buttons:
				button.deleteSprite()