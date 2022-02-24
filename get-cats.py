import requests
from bs4 import BeautifulSoup as bs
import os

# website to retrieve cat pics from
url = 'https://www.reddit.com/r/cat/'

# downloads webpage to parse for cat images
page = requests.get(url)
soup = bs(page.text, 'html.parser')
#print(soup.title)

# finds all images on webpage
image_tags = soup.findAll('img')

# create directory for cat images
if not os.path.exists('cat-pics'):
    os.makedirs('cat-pics')

# move to new directory
os.chdir('cat-pics')

# image file name variable
x = 0

# writes images
for image in image_tags:
    try:
        url = image['src']
        print(url)
        source = requests.get(url)
        if source.status_code == 200:
            with open('cat-' + str(x) + '.jpg', 'wb') as f:
                f.write(source.content)
                f.close()
                x += 1
    except:
        print('loop not run')
        pass
