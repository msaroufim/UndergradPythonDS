import Graph
import Vertex
import Queue


class GraphSearch(Graph):

def bfs(g,start):
	start.setDistance(0)
	start.setPred(None)
	vertQueue = Queue()
	vertQueue.enqueue(start)
	while(vertQueue.size() > 0):
		currentVert = vertQueue.dequeue()
		for nbr in currentVert.getConnections():
			if (nbr.getColor == 'white'):
				nbr.setColor('gray')
				nbr.setDistance(currentVert.getDistance() + 1)
				nbr.setPred(currentVert)
				vertQueue.enqueue(nbr)
			currentVert.setColor('black')

def dfs(g,start):
	start.setDistance(0)
	start.setPred(None)
	vertStack = Stack()
	vertStack.push(start)
	while (vertStack.size() > 0):
		currentVert = vertStack.pop()
		for nbr in currentVert.getConnections():
			if(nbr.getColor == 'white'):
				nbr.setColor('gray')
				nbr.setDistance(currentVert.getDistance() + 1)
				nbr.setPred(currentVert)
				vertStack.push(nbr)
			currentVert.setColor('black')
