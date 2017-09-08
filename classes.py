class animal():
	group="mammals"
	noise= "speak"




class dog(animal):
	"""docstring for dog"""
	name="Jon"
	color="Brown"
	def get_color(self,you="none"):
		return self.color, you

obj=animal()
gim=dog()
print(obj.group)
print(gim.noise)
print(gim.get_color('bus'))