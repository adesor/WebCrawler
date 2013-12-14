# Web Crawler


import urllib2

from bs4 import BeautifulSoup

def get_all_links(page):
    links = []
    for link in page.find_all('a'):
        links.append(link.get('href'))
    return links

def extract_page(seed):
    soup = BeautifulSoup(urllib2.urlopen(seed).read())
    return soup                


def union(l1,l2):
    for i in l2:
        if i not in l1:
            print i
            l1.append(i)      
    return l1
    
def crawling(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        url = tocrawl.pop()
        if url not in crawled:
            tocrawl = union(tocrawl,get_all_links(extract_page(url)))
            crawled.append(url)
    return  crawled
