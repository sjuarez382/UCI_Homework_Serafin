import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
import pymongo

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return browser = Browser('chrome', **executable_path, headless=False))


def scrape():
    ### NASA Mars News ###
    # Visit NASA page
    browser = init_browser()
    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)

    time.sleep(1)

    # Scrape page into Soup
    nasa_html = browser.html
    nasa_soup = BeautifulSoup(nasa_html, "html.parser")
    
    # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
    nasa_results = nasa_soup.find("ul", class_="item_list")
    news_title = nasa_results.find("div", class_="content_title").text
    news_p = nasa_results.find("div", class_="article_teaser_body").text


    ### JPL Mars Space Images - Featured Image ###
    # Visit JPL page
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    jpl_url_root = jpl_url.split('/spaceimages')[0]
    browser.visit(jpl_url)

    # Click full image and more info to get image url
    browser.click_link_by_partial_text('FULL')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')

    # Scrape page into Soup
    jpl_html = browser.html
    jpl_soup = BeautifulSoup(jpl_html, "html.parser")

    # Find figure to retrieve section that has image url
    jpl_img_result = jpl_soup.find("figure", class_="lede")
    jpl_img_result

    # Find the image url to the full size .jpg image
    featured_image_url = jpl_url_root + jpl_img_result.a["href"]
    featured_image_url


    ### Mars Weather ###
    # Set up url
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    twitter_response = requests.get(twitter_url)
    
    # Scrape page into Soup
    soup_twitter = BeautifulSoup(twitter_response.text, "html.parser")
    tweets = soup_twitter.find_all('div', class_='js-tweet-text-container')

    # Retrive tweets with weather information. Remove picture in the end
    for tweet in tweets:
        mars_weather = tweet.find('p').text
        if 'sol' in mars_weather:
            mars_weather_tweet = mars_weather.split("pic.twitter")[0]
            break
        else:
            pass

    ### Mars Facts ###
    # Set up url
    facts_url = "https://space-facts.com/mars/"

    # Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    browser.visit(facts_url)
    facts_df = pd.read_html(facts_url)[0]
    facts_df.columns = ["description","value"]
    facts_df = facts_df.set_index("description")
    
    # Use Pandas to convert the data to a HTML table string.
    html_table = facts_df.to_html()
    html_table.replace("\n","")
    facts_df.to_html('table_v2.html')

    ### Mars Hemispheres ###
    # Visit the USGS Astrogeology site 
    h_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    h_url_root = h_url.split('/search')[0]
    browser.visit(h_url)

    # Scrape the site and visit each hemisphere page
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

    # Get image url from each page and create url list
    url_dict_list = []

    for item_url in url_list:
        browser.visit(item_url)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        img_path = soup.select_one("ul")
        image_url = img_path.a["href"]
        url_dict_list.append(image_url)

    # Combine 2 lists to get one list of dictionaries
    hemisphere_image_urls = []
    for url,title in zip(url_dict_list,title_list):
        hemisphere_image_dict = {}
        hemisphere_image_dict["title"] = title
        hemisphere_image_dict["img_url"] = url
        hemisphere_image_urls.append(hemisphere_image_dict)
        

    # Return all results as one dictionary
    mars_data_dict = {
        "news_title" : news_title,
        "news_paragraph" : news_p,
        "featured_image_url" : featured_image_url,
        "weather_tweet" : mars_weather_tweet,
        "hemisphere_image" : hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return(mars_data_dict)