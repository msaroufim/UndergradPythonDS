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



	def recDCMemoized(coinValueList,change,knownResults):
	   minCoins = change
	   if change in coinValueList:
	      knownResults[change] = 1
	      return 1
	   elif knownResults[change] > 0:
	      return knownResults[change]
	   else:
	       for i in [c for c in coinValueList if c <= change]:
	         numCoins = 1 + recDCMemoized(coinValueList, change-i,
	                              knownResults)
	         if numCoins < minCoins:
	            minCoins = numCoins
	            knownResults[change] = minCoins
	   return minCoins
	
	
	def DPMC(coinValueList,change,minCoins):
	   for cents in range(change+1):
	      coinCount = cents
	      for j in [c for c in coinValueList if c <= cents]:
	            if minCoins[cents-j] + 1 < coinCount:
	               coinCount = minCoins[cents-j]+1
	      minCoins[cents] = coinCount
	   return minCoins[change]


if __name__ == "__main__":
	GetChangeInstance = MakeChange()

	#u slow m8
	print(GetChangeInstance.recMC([1,5,10,25,21],63))
	
	#better
	print(GetChangeInstance.recMCMemoized([1,5,10,25,21],63))

	#duuuude
	print(GetChangeInstance.DPMC([1,5,10,25,21],63))
