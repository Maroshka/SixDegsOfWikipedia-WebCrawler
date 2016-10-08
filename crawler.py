from urllib2 import *
from bs4 import BeautifulSoup

def getLinks(url):
	try:
		page = urlopen(url)
		bs = BeautifulSoup(page)
		links = [link['href'] for link in bs.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile(r'^(/wiki/)((?!:).)*$')) \
		 if 'href' in link.attrs ]
		return links
	except:
		return None