from bs4 import BeautifulSoup
import requests
import urllib.request
import sys
import subprocess

# -------------------------------
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'lxml'])
# -------------------------------



# ----- Start ----- # 
image_links = []
counter = 0

# Requests. Get
r = requests.get('https://placekitten.com/')  # ------- Starter Code
# State function takes two parameters, The HTML and the HTML Parser.
soup = BeautifulSoup(r.text, 'lxml')

# ------- Starter Code End -------- #


# Find all img tags in the webpage

  # We can print the attributes of an element using brackets. e.x image['src'] ---> Since we know     this element has an attribute of 'src'

# Now lets combine the image src with the link to retrieve the image source. 
# We're using f-strings, which allows us to add expressions in a string. 

# Append the links we find into the list variable we created. 


# Now lets itterate through the list we made
  # We Add add 1 to the counter per each ittertion so we don't create duplicate image files. 

