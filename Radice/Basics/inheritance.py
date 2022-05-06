"""
A simple illustration of the OOP concept of inheritance in Python 

"""

class parent_class:
	def __init__(self, fname, lname):
		self.firstname = fname 
		self.lastname = lname 
	
	def print_name(self):
		print(self.firstname, self.lastname)
		

class child_class(parent_class):	# Syntax to show that one class inherits from the other 
	pass	# No real functionality apart from the inherited ones 
	
class child_class2(parent_class):
	def print_reversed_name(self):
		print(self.lastname, self.firstname)