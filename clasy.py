class MyClass(object):


    def __init__(self):
    	family = 'family'
    	socktype = 'socktype'
    	proto = 'proto'
    	canonname = 'canonname'
    	sockaddr = 'sockaddr'




class Person(object):
	#name = None
	#surname = None  -- ak su tu, tak su to staticke premenne (static variables)
	#age = 0         -- nazyvane tiez aj premenne triedy (class variables)
	#salary = 0
	#hasCar = False

	def __init__(self, name, surname, age, salary=1000, car=False):
		self.name, self.surname, self.age = name, surname, age
		self.salary, self.hasCar = salary, car

	def __str__(self):
		return "Person: {self.name} {self.surname} has {self.age} years, salary {self.salary}, hasCar={self.hasCar}".format(self=self)
		