import requests
from bs4 import BeautifulSoup
import random
import sys

data = []

counter = 10


def scrapeWikiArticle(url):
  global counter
  if(counter == 0):
    print(data)
    sys.exit()
  else:
    counter = counter-1
  response = requests.get(
      url=url,
  )
  soup = BeautifulSoup(response.content, 'html.parser')
  title = soup.find(id="firstHeading")
  print(title.text)
  allLinks = soup.find(id="bodyContent").find_all("a")
  random.shuffle(allLinks)
  linkToScrape = 0
  #print(allLinks)
  for link in allLinks:
    data.append(link)
  for link in allLinks:
    #print(link)
    if link['href'].find("/wiki") == -1:
      continue
    linkToScrape = link
    #print(link)
    break
  #print(linkToScrape)
  scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])


scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")
