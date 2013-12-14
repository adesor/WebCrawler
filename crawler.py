# Web Crawler

import urllib2
from bs4 import BeautifulSoup

###
# urllib is a python module consiting
# of important url related functions
# which are helpful in Web Crawler's working.
###




def get_all_links(page,seed):
    links = []
    for link in page.find_all('a'):
        url = (link.get('href'))
        if url.find("http") == -1:
            url = seed+"/"+url
        links.append(str(url))
    return links


def extract_page(seed):
    soup = BeautifulSoup(urllib2.urlopen(seed).read())
    return soup                


def union(l1,l2):
    for i in l2:
        if i not in l1:
            l1.append(i)      
    return l1
    
def crawling(seed):
    tocrawl = [seed]
    crawled = []
    try:
        while tocrawl:
            url = tocrawl.pop(0)
            if url not in crawled:
                tocrawl = union(tocrawl,get_all_links(extract_page(url),seed))
                crawled.append(url)
                print url
    except:
        pass
    return  crawled
