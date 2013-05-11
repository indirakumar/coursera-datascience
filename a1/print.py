#! /usr/bin/python


# a) Write a program, print.py, to print out the text of each tweet in the result.
# b) Generalize your program, print.py, to fetch and print 10 pages of results. 
# Note that you can return a different page of results by passing an additional argument in the url:
#	http://search.twitter.com/search.json?q=microsoft&page=2
# When executed, the script should print each tweet on an individual line to stdout.


import urllib
import json



url_base = "http://search.twitter.com/search.json?q=microsoft&page="


# Iterate through ten pages
for i in range(1,10):
	response = urllib.urlopen(url_base + str(i))

	results = json.load(response)["results"]

	for r in results:
		print r["text"]




