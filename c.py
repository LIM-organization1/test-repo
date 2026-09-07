from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.nate.com/')
source = response.text
#print(source)

soup = BeautifulSoup(source, 'html.parser')
#result = soup.select('olLiveIssueKeyword > li:nth-child(1) > a > span.txt_rank')
result = soup.select('#olLiveIssueKeyword > li:nth-child(1)')
print(result)

for li in result:
    span = li.select_one('.txt_rank')
    #print(span)

    if span:
        print(span.get_text(strip=True))