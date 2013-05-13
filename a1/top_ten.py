import sys, json, re, operator

tweets = []
tags = {}

def parse_tweets(tweet_fp):

	data = []

	for line in tweet_fp:
		data.append(json.loads(line))

	for t in data:
		try:
			tag_entity = t["entities"]["hashtags"]
			if len(tag_entity) > 0:
				for e in tag_entity:
					try:
						tags[e["text"]] += 1
					except KeyError:
						tags[e["text"]] = 1.0
		except KeyError:
			pass



def sort_tags():
	sorted_tags = sorted(tags.iteritems(), key=operator.itemgetter(1))
	sorted_tags.reverse()

	for i in range(0,10):
		key,value = sorted_tags[i]
		print key + " " + str(value)
	



def main():
    tweet_file = open(sys.argv[1])
    parse_tweets(tweet_file)
    sort_tags()

if __name__ == '__main__':
    main()



