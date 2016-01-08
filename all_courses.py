from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'https://www.coursera.org/courses/?primaryLanguages=en').read()
soup = BeautifulSoup(r)

print(soup.status, soup.data)
