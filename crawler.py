# Web Crawler

import urllib2
###
# urllib is a python module consiting
# of important url related functions
# which are helpful in Web Crawler's working.
###

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
    try:
        while tocrawl:
            url = tocrawl.pop(0)
            if url.find("http") == -1:
                url = seed+"/"+url
            if url not in crawled:
                tocrawl = union(tocrawl,get_all_links(extract_page(url)))
                crawled.append(url)
    except:
        pass
    return  crawled
