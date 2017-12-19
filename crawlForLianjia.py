from bs4 import BeautifulSoup
import urllib2

originUrl = "http://sh.lianjia.com/zufang"

def main():
    if __name__ == '__main__':
        num = 10
        for i in range(1,num,1):
            crawling(i)

def crawling(pageNum):
    nextUrl = originUrl + "/d" + pageNum
    soup = BeautifulSoup(urllib2.urlopen(nextUrl), 'lxml')

    items = soup.find(id="house-lst").findAll('li')
    for each in items:
        print each
main()