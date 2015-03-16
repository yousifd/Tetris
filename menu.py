from pyglet import graphics
from pyglet import image as pygletImage
from pyglet import sprite

# work on creating a resource file that you go to for all resources
# Try creating a list menu that is a subclass of menu!
# Try creating a circular menu that is a subclass of menu!

# Don't use getters and settrs

class Image(object):
	def __init__(self, image, xPos, yPos, batch, animation=None):
		self.name = image.split('.')[0]
		self.image = pygletImage.load(image)
		self.width = self.image.width
		self.height = self.image.height
		self.image.anchor_x = self.width/2
		self.image.anchor_y = self.height/2
		self.sprite = sprite.Sprite(self.image, x=xPos, y=yPos, batch=batch)
		self.animate = animation

	def getName(self):
		return self.name

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getAnchor_x(self):
		return self.image.anchor_x

	def getAnchor_y(self):
		return self.image.anchor_y

	def getX(self):
		return self.sprite.x

	def getY(self):
		return self.sprite.y

	def deleteSprite(self):
		self.sprite.delete()

	# Add more Functionality to image:
	#	- Resize

	def animate(self):
		'''Switches between image and animate to create animation,
			the animate could be another image or gif'''
		if self.animate == None:
			print 'Image has no animation provided!'
			pass
		else:
			self.image=pygletImage.load(self.aniamte)
			#figure out how to return to original image if not .gif

class Title(Image):
	pass

class Button(Image):
	def ifAbove(self, x, y):
		leftBoundary = self.getX() - self.getAnchor_x()
		rightBoundary = self.getX() + self.getAnchor_x()
		bottomBoundary = self.getY() - self.getAnchor_y()
		topBoundary = self.getY() + self.getAnchor_y()
		return ((leftBoundary <= x <= rightBoundary) and (bottomBoundary <= y <= topBoundary))


class Menu(object):
	def __init__(self, menuWidth, menuHeight, x=0, y=0):
		'''Menu Width: width of menu
		   Menu Height: height of menu
		   #used as relative positioning for buttons
		   x: Position of menu Horizontally inside of the window
		   y: Position of menu Vertically inside of the window

		   buttonShift: the shift of buttons from mid height'''
		self.batch = graphics.Batch()
		self.title = None
		self.buttons = []
		self.width = menuWidth
		self.height = menuHeight
		self.x = x
		self.y = y
		self.buttonShift = 0

	def addTitle(self, image, xPos, yPos):
		self.title = Title(image, xPos + self.x, yPos + self.y, self.batch)

	def addButton(self, image, xPos, yPos):
		self.buttons.append(Button(image, xPos + self.x, yPos + self.y, self.batch))

	def addCenterButton(self, image, margine=0):
		self.addButton(image, self.width/2 + self.x, self.height/2 + self.y + self.buttonShift)
		self.buttonShift -= self.buttons[-1].getHeight() + margine

	def getButton(self, name):
		for button in self.buttons:
			if button.getName() == name:
				return button

	def ifAbove(self, name, x, y):
		return self.getButton(name).ifAbove(x, y)

	def draw(self):
		self.batch.draw()

	def delete(self):
		if self.title != None:
			self.title.deleteSprite()
		if len(self.buttons) != 0:
			for button in self.buttons:
				button.deleteSprite()