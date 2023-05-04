#importing library for web scrapping
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

#Main Function for Scrapping
def main(emotion):
    # Movie Database Url for Drama genre of
    # movie against emotion Sad
    if(emotion == "Sad"):
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
  
    # Movie Database Url for Musical genre of
    # movie against emotion Disgust
    elif(emotion == "Disgust"):
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
  
    # Movie Database Url for Family genre of
    # movie against emotion Anger
    elif(emotion == "Anger"):
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
  
    # Movie Database Url for Thriller genre of
    # movie against emotion Anticipation
    elif(emotion == "Anticipation"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    # Movie Database Url for Sport genre of
    # movie against emotion Fear
    elif(emotion == "Fear"):
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
  
    # Movie Database Url for Thriller genre of
    # movie against emotion Enjoyment
    elif(emotion == "Enjoyment"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    # Movie Database Url for Western genre of
    # movie against emotion Trust
    elif(emotion == "Trust"):
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
  
    # Movie Database Url for Film_noir genre of
    # movie against emotion Surprise
    elif(emotion == "Surprise"):
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
  
    # HTTP request to get the data of
    # the whole page
    response = HTTP.get(urlhere)
    data = response.text
  
    # Parsing the data using
    # BeautifulSoup.This will help analyze the sentiment value of the movie according to the emotion associated
    soup = SOUP(data, "lxml")
  
    # Extract movie titles from the
    # data using regex
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    return title
  
# Driver Function
if __name__ == '__main__':
  
    emotion = input("Enter the emotion: ")
    a = main(emotion)
    count = 0
  
    if(emotion == "Disgust" or emotion == "Anger"
                           or emotion=="Surprise"):
  
        for i in a:
  
            # Splitting each line of the
            # Movie Database data to scrape movies
            tmp = str(i).split('>;')
  
            if(len(tmp) == 3):
                print(tmp[1][:-3])
  
            if(count > 13):
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split('>')
  
            if(len(tmp) == 3):
                print(tmp[1][:-3])
  
            if(count > 11):
                break
            count+=1