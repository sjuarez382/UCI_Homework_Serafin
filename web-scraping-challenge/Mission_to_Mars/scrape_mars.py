#!/usr/bin/env python
# coding: utf-8

# In[14]:


#imports
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
import pymongo


# In[1]:


pip install splinter


# In[2]:


pip install webdriver_manager


# In[8]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[9]:


# define news url
mars_news_url = "https://mars.nasa.gov/news/"
browser.visit(mars_news_url)


# NASA Mars News

# In[10]:


#scaping to find list
nasa_html = browser.html
nasa_soup = BeautifulSoup(nasa_html, "html.parser")
nasa_results = nasa_soup.find("ul", class_="item_list")


# In[11]:


#scraping to find latest title and paragraph
news_title = nasa_results.find("div", class_="content_title").text
news_p = nasa_results.find("div", class_="article_teaser_body").text

print(news_title)
print(news_p)


# JPL Mars Space Images - Featured Image

# In[16]:


#define jpl url
jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
jpl_url_root = jpl_url.split('/spaceimages')[0]
browser.visit(jpl_url)


# In[17]:


#clicking on imagine to get info
browser.click_link_by_partial_text('FULL')
time.sleep(5)
browser.click_link_by_partial_text('more info')


# In[19]:


#find imagine url
jpl_html = browser.html
jpl_soup = BeautifulSoup(jpl_html, "html.parser")
jpl_img_result = jpl_soup.find("figure", class_="lede")
jpl_img_result

featured_image_url = jpl_url_root + jpl_img_result.a["href"]
featured_image_url


# Mars Facts

# In[20]:


#visiting url and using pandas to scrape
facts_url = "https://space-facts.com/mars/"
browser.visit(facts_url)
facts_df = pd.read_html(facts_url)[0]
facts_df.columns = ["description","value"]
facts_df = facts_df.set_index("description")


# In[21]:


# convert to HTML table string
html_table = facts_df.to_html()


# In[22]:


# clean and save table
html_table.replace("\n","")
facts_df.to_html('table_v2.html')


# Mars Hemispheres

# In[24]:


#visiting url
h_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
h_url_root = h_url.split('/search')[0]
browser.visit(h_url)


# In[25]:


# scraping using for loop to visit each hemisphere page
title_list = []
url_list = []

for result in range(1):
    h_html = browser.html
    h_soup = BeautifulSoup(h_html, "html.parser")
    h_results = h_soup.find_all("div", class_="item")
    
    # Get url for each hemisphere
    for item in h_results:
        item_url = item.a["href"]
        item_full_url = h_url_root + item_url
        url_list.append(item_full_url)
        title = item.find("h3").text
        title_list.append(title)
        
title_list


# In[27]:


#url form images
url_dict_list = []

for item_url in url_list:
    browser.visit(item_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    img_path = soup.select_one("ul")
    image_url = img_path.a["href"]
    url_dict_list.append(image_url)
    
url_dict_list


# In[28]:


#combining list
hemisphere_image_urls = []

for url,title in zip(url_dict_list,title_list):
    hemisphere_image_dict = {}
    hemisphere_image_dict["title"] = title
    hemisphere_image_dict["img_url"] = url
    hemisphere_image_urls.append(hemisphere_image_dict)
print(hemisphere_image_urls)
