#This is simple Inheritance Example in python.
#dfdfd
#!/usr/bin/env python3
class person:
	def __init__(self,fname,lname):
		self.fname=fname
		self.lname=lname
	def name(self):
		return self.fname + " " +self.lname


class student(person):
	def __init__(self,fname,lname,ssn):
		person.__init__(self,fname,lname)
		self.ssn=ssn
	def studinfo(self):
		return self.name() + " " +self.ssn

obj = person("XYZ","ABC")
obj2 = student("PQR","STU","45")

print(obj.name())
print(obj2.studinfo())
