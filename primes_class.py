class Primes:
	def __init__(self, start, end):
		self.start = start
		self.end = end
		# raising assertion error while starting number is less than 0 or while start < end.
		assert (self.start > 0), "starting number shoupd be greater than 0"
		assert (self.start < self.end), "starting number should be less than end number"
		self.__prints_prime()
		
	def __checkPrime(self, n):
			count = 0
			for k in range(1, int(pow(n, .5)) + 1):
				if n % k == 0:
					count += 1
			if count == 1: return True
		
	def __prints_prime(self):
			
			for i in range(self.start, self.end + 1):
				if self.__checkPrime(i):
					print(i)
				
				
		
t = Primes(-2, 20)