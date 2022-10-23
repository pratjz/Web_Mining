'''

Web Scraping the URLs and Email IDs

'''

import urllib.request
from bs4 import BeautifulSoup

# url to Scrap

wiki = 'https://dlca.logcluster.org/display/public/DLCA/4.1+Nepal+Government+Contact+List'



page = urllib.request.urlopen(wiki)


soup = BeautifulSoup(page, features = 'html.parser')
print('\n\nPage Scrapped !!! \n\n')

print('\n\nTitle of the Page \n\n')
print(soup.title.string)


print('\n\nALL THE URLs IN THE WEB PAGE\n\n')


all_links = soup.find_all('a')


print('Total number of URLs present = ',len(all_links))



print('\n\nLast 5 URLs in the page are : \n')



if len(all_links) > 5 :
  last_5 = all_links[len(all_links)-5:]
  for url in last_5 :
    print(url.get('href'))
    
    
emails = []

for url in all_links :
  if(str(url.get('href')).find('@') > 0):
    emails.append(url.get('href'))
    
    
print('\n\nTotal Number of Email IDs Present: ', len(emails))


print('\n\nSome of the emails are: \n\n')

for email in emails[:5]:
  print(email)


