class Student:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
	def print_name(self):
		return f'The name is {self.name}'
		
	def print_age(self):
		return f'The age is {self.age}'
		
s = Student("amrendra", 39)

print(s.print_name())
print(s.print_age())