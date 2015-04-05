import PriorityQueue
import Graph
import Vertex
import sys

def prim(G,start):
	pq = PriorityQueue()

	#initialize values
	for v in G:
		v.setDistance(sys.maxsize)
		v.setPred(None) 
	start.setDistance(0)
	pq.buildHeap([(v.getDistance(),v) for v in G])
	while not pq.isEmpty(): 
		currentVert = pq.delMin()
		for nextVert in currentVert.getConnections():
			newCost = currentVert.getWeight(nextVert) + currentVert.getDistance()

			if nextVert in pq and newCost < nextVert.getDistance():
				nextVert.setPred(currentVert)
				nextVert.setDistance(newCost)
				pq.decreaseKey(nextVert,newCost)