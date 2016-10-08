import Queue as Q
from urllib2 import *
from bs4 import BeautifulSoup
from crawler import *

def BFS(start, goal):
	crawled = []
	path = []
	q = Q.Queue()
	if start == goal:
				return goal
	start = [start]
	q.put(start)
	while not q.empty():
		url = q.get()
		if url[-1] not in crawled:
			path.append(url)
			fullUrl = "http://en.wikipedia.org"+url[-1]
			links = getLinks(fullUrl)
			crawled.append(url[-1])
			if goal in links:
				path.append(goal)
				return path
			del path[-1]
			if links != None:
				for i in links:
					nurl = url + [i]
					q.put(nurl)

	return path
