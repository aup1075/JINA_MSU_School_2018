"""
An example of abstract base classes in Python 
Please refer tutorial at:
https://github.com/CodeSports/Modern-Python-Programming/blob/master/PythonABC/dakshhub_python_abc.py
"""

import abc 

# An abstract base class is a parent class of (child) classes to come. It only provides an interface and 
# virtual functions. The child classes provide implementations. 

# class providing a skeleton/interface/boiler-plate of State.
class State(abc.ABC):
	
	@abc.abstractmethod
	def in_state(self):
		pass					

# Classes implementing the abstract base class of state. 		
class HappyState(State):
	def in_state(self):
		print("I am in a happy state")
		
class SadState(State):
	def in_state(self):
		print("I am in a sad state")
		
#### ---------------------------------- ####

# class providing a skeleton/interface/boiler-plate of Event. 
class Event(abc.ABC):
	@abc.abstractmethod
	def in_event(self):
		pass

# Classes providing an implementation of the abc Event. 
class recieved_money(Event):
	def in_event(self):
		print("I got money")
		
class lost_money(Event):
	def in_event(self):
		print("I lost money")

#### ---------------------------------- ####

class state_machine():

	def __init__(self):			# Constructor/Initializer for the state machine 
		self.currstate = HappyState() # Here we have passed a class constructor 
		
	def current_state(self):
		print(self.currstate.in_state())
		
	def recieve_event(self, event):
		if isinstance(event, lost_money): # isinstance() compares class names / types 
			self.currstate = SadState()
		if isinstance(event, recieved_money):
			self.currstate = HappyState()



		

		

		