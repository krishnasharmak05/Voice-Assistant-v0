__doc__ = 'Gets news from Google News and prints it to the terminal'


import random
from bs4 import BeautifulSoup as BS
import requests
import assets.TTSEngine_Handler as tts

def get_website():
    website = "https://news.google.com/"
    response = requests.get(website)
    return response

def get_headlines():
    response = get_website()
    soup = BS(response.text, "html.parser")
    headlines = soup.find("body").find_all("a")
    return headlines

def sort_tags()->tuple[list[int], list[str]]:
    headlines = get_headlines()
    news = []
    unwanted = [
    "News",
    "Sign in",
    "Home",
    "For you",
    "Following",
    "News Showcase",
    "India",
    "World",
    "Local",
    "Business",
    "Technology",
    "Entertainment",
    "Sports",
    "Science",
    "Health",
    "More on weather.com",
    "Top stories",
    "Full coverage",
    "Local news",
    ]
    for x in list(dict.fromkeys(headlines)):
        if x.text.strip() != "" and x.text.strip() not in unwanted:
            news.append(x.text.strip())

    list1 = [x for x in range(len(news))]
    random_news = random.choices(list1, k = 5)
    temp = []
    temp = [x for x in random_news if x not in temp]
    return temp.copy(), news
    
    
def print_and_say_news():
    random_news = sort_tags()[0]
    news = sort_tags()[1]
    for i in range(len(random_news)):
        print(news[random_news[i]])
    tts.engine.say(" ")
    tts.engine.runAndWait()
    for i in range(3):
        tts.engine.say(news[random_news[i]])
        tts.engine.runAndWait()
    tts.engine.say("And more")
    tts.engine.runAndWait()

if __name__ == "__main__":
    print_and_say_news()


# Code needs to be looked over again!