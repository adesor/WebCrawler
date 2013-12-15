# Web Crawler

import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse, urljoin

###
# urllib is a python module consiting
# of important url related functions
# which are helpful in Web Crawler's working.
###




def get_all_links(page,seed):
    links = []
    for link in page.find_all('a'):
        url = (link.get('href'))
        if url:
            parse_url = urlparse(url)
            if not parse_url.scheme:
                url = urljoin(seed, url)
            links.append(url)
    return links


def extract_page(seed):
    try:
        page = urllib2.urlopen(seed).read()
    except:
        page = ""
    soup = BeautifulSoup(page)
    return soup                


def union(l1,l2):
    for i in l2:
        if i not in l1:
            l1.append(i)      
    return l1
    
def crawling(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        url = tocrawl.pop(0)
        if url not in crawled:
            tocrawl.extend(get_all_links(extract_page(url),url))
            crawled.append(url)
            print url
    return  crawled
