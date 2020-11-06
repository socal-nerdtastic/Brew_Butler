import webbrowser
import urllib.parse
import urllib.request 
import os
import sys 
from bs4 import BeautifulSoup
from requests import get
import wget


#TODO Make recipe an editable value via voice command. Currently a fixed value for testing purposes.
#TODO when asking for recipe if user just says "zombie dirt" or something, add logic to ask for full name.
#split_recipe = recipe.split()
#title = split_recipe[0:2]
#title = "_".join(title)
#print(title)

def extract_or_all_grain(recipe):
    recipe = recipe.lower()
    url = "https://www.northernbrewer.com/products/"
    words = recipe.split()
    #print("got to extract or all grain ")
    
    if "extract" in recipe:
        print("extract")
        end = words.index("extract")
        suffix = words[0:end + 1]
        suffix = "-".join(suffix)
        suffix += "-kit"
        url += suffix
        print(url)
        return url
    elif "all grain" in recipe:
        print("all grain")
        end = words.index("all")
        suffix = words[0:end + 2]
        suffix = "-".join(suffix)
        suffix += "-kit"
        url += suffix
        print(url + " From function")
        return url
    #TODO re-prompt user for all grain or extract



#This section creates a url, goes to the page via BeautifulSoup then parses the page looking for
# the recipe pdf link. It then returns the link and turns it into a string to be used later in
# recipe_url_grabber function.
#TODO add a try block for url response and if it's broken, search for the kit on the website, and return the first choice.
#url = extract_or_all_grain(recipe) 
#response = get(url)
#page = response.text
#soup = BeautifulSoup(page, 'html.parser')
#link = soup.find("td", text = "Beer Recipe Kit Instructions").find_next_sibling("td")
#link_string = str(link)

#print(link_string)

#Takes in the link_string and splits it with the delimiter of a quotation mark.
#This works due to how Northern Brewer stores their recipes on an external source, Shopify.
#def recipe_url_grabber(link):
    #link = link.split('"', 2)
    #new_link = link[1]
    #return new_link

#recipe_url = recipe_url_grabber(link_string)
#print(recipe_url)

#print("Downloading %s" % recipe_url)
#wget.download(recipe_url, (title + ".pdf"))