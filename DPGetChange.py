class MakeChange:
	def recMC(self,coinValueList,change):
	   minCoins = change
	   if change in coinValueList:
	     return 1
	   else:
	      for i in [c for c in coinValueList if c <= change]:
	         numCoins = 1 + self.recMC(coinValueList,change-i)
	         if numCoins < minCoins:
	            minCoins = numCoins
	   return minCoins

	def recMCMemoized(coinValueList,change):
		#to implement
		pass

	def DPMC(coinValueList,change):
		#to implement
		pass


if __name__ == "__main__":
	GetChangeInstance = MakeChange()

	#u slow m8
	print(GetChangeInstance.recMC([1,5,10,25,21],63))
	
	#better
	print(GetChangeInstance.recMCMemoized([1,5,10,25,21],63))

	#duuuude
	print(GetChangeInstance.DPMC([1,5,10,25,21],63))