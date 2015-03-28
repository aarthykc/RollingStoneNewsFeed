import feedparser
import json
import mechanize

def getLatestPosts():
	feed = feedparser.parse("http://www.rollingstone.com/music.rss")
	posts = feed["entries"]
	parsedPosts = []
	for post in posts:
		parsedPost = {}
		link = parsedPost["link"] = post["link"]
		parsedPost["title"] = post["title"]
		parsedPost["summary"] = post["summary"]
		parsedPost["thumbnail"] = post["links"][1]["href"]
		if(link.find("/news/") is not -1):
			parsedPost["type"] = "news"
		elif(link.find("/pictures/") is not -1):
			parsedPost["type"] = "pictures"
		elif(link.find("/videos/") is not -1):
			parsedPost["type"] = "videos"
		elif(link.find("/features/") is not -1):
			parsedPost["type"] = "features"
		elif(link.find("/premieres/") is not -1):
			parsedPost["type"] = "premieres"
		elif(link.find("/live-reviews/") is not -1):
			parsedPost["type"] = "live-reviews"
		parsedPosts.append(parsedPost)
	return parsedPosts







