class C:
	@property
	def token(self):    #To access token variable from the instance of the class
		print("Getter called")
		if self.__token == 2:    #Using __ as it is a hidden variable
			raise AssertionError
		return self.__token
	@token.setter
	def token(self,value):    #To set the value of token
		print("Setter called")
		self.__token = value


c = C()
c.token = 3
print(c.token)