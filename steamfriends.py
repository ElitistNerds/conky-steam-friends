#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup

# Enter your SteamID below
steamid = ""

# BeautifulSoup Setup
url = "http://steamcommunity.com/profiles/" + steamid + "/friends"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page)

# Username Scraping
u = []
for username in soup.find_all("div", class_="friendBlockContent"):
	name = username.contents[0].strip()
	name = (name[:15] + '..') if len(name) > 15 else name
	u.append(name)

# Status Scraping
s = []
for status in soup.find_all("span", class_="friendSmallText"):
        stat = status.contents[0].strip()
        stat = (stat[:30] + '..') if len(stat) > 30 else stat
        if stat == "":
                stat = status.contents[1]
                stat = stat.prettify()
                stat = BeautifulSoup(''.join(stat))
                stat = stat.find("span", class_="linkFriend_in-game")
                stat = "In-Game: " + stat.contents[2].strip()
                stat = (stat[:30] + '..') if len(stat) > 30 else stat
                s.append(stat)
        else:
                s.append(stat)

# Combine Username & Status list
list = zip(u,s)

# Print list
for item in list:
	print("".join(word.ljust(22) for word in item))
