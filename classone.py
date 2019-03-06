

#Example of Simple Class in Python and accessing the variables and displaying it!
class classone:
	var = 30

	new_var = 'Python'
	
	def myfunc(self):
		print("Inside the main function block")

obj=classone() # Creating object of classone

print(obj.var) 

print(obj.new_var)

print(obj.functionds)

print(obj.__doc__)
