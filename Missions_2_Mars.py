#!/usr/bin/env python
# coding: utf-8

# In[35]:


from bs4 import BeautifulSoup
import pandas as pd
import time
from splinter import Browser
import requests


# In[36]:


executable_path = {"executable_path": "/Users/saleh/Downloads/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[37]:


#NASA Mars News
# Navigate to the page
news_url = 'https://mars.nasa.gov/news/'
browser.visit(news_url)


# In[39]:


time.sleep(4)

# Assign the HTML content of the page to a variable
news_html = browser.html

# Parse HTML with Beautifulsoup
soup = BeautifulSoup(news_html,'html.parser')


# In[40]:


# Retrieve the latest News Title and Paragraph Text
result = soup.find('div', class_="list_text")

news_title = result.a.text
news_p = result.find('div',class_="article_teaser_body").text

print(f"news_title: {news_title}")
print(f"news_p: {news_p}")


# In[42]:


#JPL Mars Space Images - Featured Image
# Navigate to the page
img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(img_url)


# In[43]:


time.sleep(4)

# Assign the HTML content of the page to a variable
imgs_html = browser.html
# Parse HTML with Beautifulsoup
soup = BeautifulSoup(imgs_html,'html.parser')


# In[44]:


# Find the image url for the current Featured Mars Image
img_result = soup.find('article', class_="carousel_item")['style']

img_url = img_result.replace("background-image: url('","").replace("');","")
featured_image_url = f"https://www.jpl.nasa.gov{img_url}"

print(featured_image_url)


# In[45]:


#Mars Weather
# Navigate to the page
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)


# In[47]:


time.sleep(4)

# Assign the HTML content of the page to a variable
weather_html = browser.html
# Parse HTML with Beautifulsoup
soup = BeautifulSoup(weather_html, 'html.parser')


# In[48]:


span_class = "css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"
results = soup.body.find_all("span", class_=span_class)

# Retrieve the latest Mars weather tweet from the page.
for index, result in enumerate(results):
    if "InSight" in result.text:
        mars_weather = result.text
        print(mars_weather)
        break  # get the first result only
    else:
        pass


# In[49]:


#Mars Facts
# Collect the tables from the page 
facts_url = 'https://space-facts.com/mars/'
browser.visit(facts_url)

# Retrieve the table containing facts about the planet 

#tables = pd.read_html(requests.get('https://space-facts.com/mars/').text)
tables = pd.read_html(facts_url)
df = tables[0]
df.columns = ["Description","Value"]
idx_df = df.set_index("Description")
idx_df


# In[50]:


## Export to a HTML file
mars_df = idx_df.to_html("table.html", border="1",justify="left")


# In[51]:


#Mars Hemispheres
# Navigate to the page
hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemisphere_url)


# In[52]:


time.sleep(4)

# Assign the HTML content of the page to a variable
hemisphere_html = browser.html
# Parse HTML with Beautifulsoup
soup = BeautifulSoup(hemisphere_html,'html.parser')


# In[53]:


# Collect the urls for the hemisphere images
items = soup.find_all("div", class_="item")

main_url = "https://astrogeology.usgs.gov"
hemisphere_urls = []

for item in items:
    hemisphere_urls.append(f"{main_url}{item.find('a', class_='itemLink')['href']}")

print(*hemisphere_urls, sep = "\n") 


# In[54]:


# Create a list to store the data
hemisphere_image_urls=[]

# Loop through each url
for url in hemisphere_urls:
    # Navigate to the page
    browser.visit(url)
    
    time.sleep(4)
    
    # Assign the HTML content of the page to a variable
    hemisphere_html = browser.html
    # Parse HTML with Beautifulsoup
    soup = BeautifulSoup(hemisphere_html,'html.parser')
    
    img_url = soup.find('img', class_="wide-image")['src']
    title = soup.find('h2', class_="title").text
    
    hemisphere_image_urls.append({"title":title,"img_url":f"https://astrogeology.usgs.gov{img_url}"})


# In[55]:


hemisphere_image_urls


# In[32]:


browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




