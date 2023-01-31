# Python Webscraping Workshop 

## Introduction to Webscraping in Python 

Webscraping in Python is an interesting skill that can be explored by new learners of the language to get a better understanding of what you can use Python to acomplish and the 'tools' within the langauge that help do it. 

## What is the process of the workshop? 

In this particular workshop, it is imperative for new programmers to learn key concepts of programming in general. In this scenario, the end goal is to allow our learners to understand for loops, dictionaries and variables in python. We will be utilizing the website, placekitten.com, to download the images on its homepage to our replit repositories. 

### 1. Running the Program

In order for our students to get an idea of what they will be doing today, I believe its important to show them exactly what they'll be making. Hosted on replit, our learners will run the completed program and see the end result. We will then move into the actual building phase of the program. 


### 2. Procedure

The instruction set consists of using the concepts I will provide to them in order to complete the program. Using For loops, f-string, lists and functions and the template provided, our learners will be able to complete the workshop. 

### 3. Demo

In the remaining time for the workshop we'll allow learners to actually run their programs, debug if needed and even ask questions on where they could learn more information on the topic before they finish for the day. 


## Creating the Image-Downloader 

### 1. The Boilerplate

The Boilerplate consists of the code needed to retrieve the html from a webpage. In our workshop, we will be using placekitten.com, as it is a static website that doesn't load anything dynamically through Javascript or otherwise. Meaning we can always find and save the same images on the webpage without anything changing for each person attending the workshop.

```python
# Modules 
from bs4 import BeautifulSoup
import requests
import urllib.request

# ----- Start ----- # 

image_links = []
counter = 0

# Requests. Get
r = requests.get('https://placekitten.com/')  # ------- Starter Code
# State function takes two parameters, The HTML and the HTML Parser.
soup = BeautifulSoup(r.text, 'lxml')

# ------- Starter Code End -------- #

```

Using Python3's BeautifulSoup and Request libaries, and using their functions requests.get and BeautifulSoup we can create a soup object that contains the html for placekitten.com. (Depending on time restraints I will go over the parameters that the BeautifulSoup function takes in part one of our workshop process) 

### 2. Itterating through the webpage's content 

Using BS4's find_all function and a for loop, we can search for all 'img' tags within the document and print it to the console. This we use a for-loop in order to itterate through all matching elements in the webpage with the img tag. 

```python
for images in soup.find_all('img'):
    print(images)
```

The output should look like this: 

```html
<img alt="" id="image-0" src="408/287"/>
<img alt="" id="image-1" src="/200/287"/>
<img alt="" id="image-2" src="/200/140"/>
<img alt="" id="image-3" src="/200/139"/>
<img alt="" id="image-4" src="/200/286"/>
<img alt="" id="image-5" src="/96/140"/>
<img alt="" id="image-6" src="/96/139"/>
<img alt="" id="image-7" src="/200/138"/>
```

### 3. HTML Attributes

Elements we can find using BS4 may contain attributes. This is apparent within the image elements we printed to the console in our last step. We can access the attributes of an element using bracket notation.

```python
for images in soup.find_all('img'):
    # print(images)
    print(images['src'])
```

Using the for-loop we made previously, we can access each 'src' attribute to retreive the source to the images we want to download. 

The Output should look like this: 

```
408/287
/200/287
/200/140
/200/139
/200/286
/96/140
/96/139
/200/138
```

### 4. Combining the image source with the webpage links. 

#### 4a. F-String Notation

 We can use f-strings, which allows us to virtually put any python code inside of a string, to input our image source within it's link. But before doing that, it's important to understand how f-strings work. 

The notation looks like this: 

```python
age = 22 
print(f'I am {age} years old")
```

In which the output would be: 

```
I am 22 years old
```

#### 4b. Image Link 

In order to autonomously get the image source, we need to combine the webpage link with the image source in order to get the actual link to the image for downloading. We will append (add) the results to our list 'image_links'.  

```python
for images in soup.find_all('img'):
    # print(images)
    print(images['src'])

    link = f'https://placekitten.com/{images["src"]}'
    image_links.append(link)
```

Lets make a second for loop to itterate through and print out all elements within our list 'image_links' 

```python
for images in image_links: 
    print(images) 
```

The output should look like this: 
    
```
https://placekitten.com/408/287
https://placekitten.com//200/287
https://placekitten.com//200/140
https://placekitten.com//200/139
https://placekitten.com//200/286
https://placekitten.com//96/140
https://placekitten.com//96/139
https://placekitten.com//200/138
```


### 5. Downloading the Image 

In order to download the image, we will be using the urllib.request module and it's function urlretrieve. Urlretrieve takes two parameters, the image link and the path in which we want to save the images to. Using the previous for loop, we can save each image into a folder 'Images' thats already in the repo. 


In addition, we'll add a counter that we will add 1 to on each itteration so that the files won't overwrite each other because they have the same file name. We will use f-strings to input this into the function. and save the file. 

```python
for images in image_links: 
     counter += 1 
     urllib.request.urlretrieve(images, f"./Images/{counter}.jpg")
```


At the end of the workshop, we should have 8 images saved in total! 


### 6. Additonal Learning

Now that we've completed the workshop, I want you to take the time to find other elements within this webpage and try to print it out to the console. Review the code we've just completed and try it yourself. It doesn't hurt messing around. 


| Additional Learning  | Description |
| ------------- |:-------------:|
| [BeautifulSoup4 Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)     | Documentation for Beautiful Soup 4! Learn more information <br> on how to find certian elements in a webpage|
| [For Loops in Python3 - W3Schools](https://www.w3schools.com/python/python_for_loops.asp)    | Learn all about for loops in Python3 and how to use them. |
| [String Formatting in Python3 - W3Schools](https://www.w3schools.com/python/python_string_formatting.asp)| Learn how to format your strings in a multitude of ways |
| [Lists in Python3 - W3Schools](https://www.w3schools.com/python/python_lists.asp) | Understand how Lists work in Python3 and the operations you can perform on them|


Use this information to webscrape your own content. It can even be on another website if you'd like! 
