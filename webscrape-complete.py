from bs4 import BeautifulSoup 
import requests
import urllib.request
import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'lxml'])

image_links = []
counter = 0 

# Requests. Get 
r = requests.get('https://placekitten.com/') # ------- Starter Code 
# State function takes two parameters, The HTML and the HTML Parser. 
soup = BeautifulSoup(r.text, 'lxml')

                # ------- Starter Code End -------- # 

for images in soup.find_all('img'):
    print(images)

    # To get the attribute within an element, we can search through it using this notation: 
    print(images['src'])

    # Now lets combine the image src with the link to retrieve the image source. 
    # We're using f-strings, which allows us to add expressions in a string. 
    link = f'https://placekitten.com/{images["src"]}'
    image_links.append(link)

    
for images in image_links: 
  counter += 1 
  urllib.request.urlretrieve(images, f"./Images/{counter}.jpg")
  
