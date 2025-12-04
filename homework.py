class Lego:
	def __init__(self, shape, color, is_rare):
		self.shape = shape
		self.color = color
		self.is_rare = is_rare
	def pickup(self):
		print(f"you pickup the {self.color} brick")
	def putdown(self):
		print(f"you putdown the {self.color} brick")

brick = Lego("square", "blue", False)
brick2 = Lego("rectangle", "gold", True)
print(brick.is_rare)
print(brick.color)
print(brick.shape)
print(brick2.is_rare)
print(brick2.color)
print(brick2.shape)
brick.pickup()
brick2.putdown()
