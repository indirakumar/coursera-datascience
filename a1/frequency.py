import sys, json, re, operator

tweets = []
words = {}

def parse_tweets(tweet_fp):

	data = []

	for line in tweet_fp:
		data.append(json.loads(line))

	for t in data:
		try:
			tweets.append(t["text"])
		except KeyError:
			pass

def calc_frequency():

	total_words = 0.0

	for t in tweets:

		wordList = re.sub("[^\w]", " ",  t).split()

		for w in wordList:
			total_words += 1
			try:
				words[w] += 1
			except KeyError:
				words[w] = 1.0

	sorted_x = sorted(words.iteritems(), key=operator.itemgetter(1))
	for k,v in sorted_x:
		print k + " " + str(v/total_words)



def main():
    tweet_file = open(sys.argv[1])
    parse_tweets(tweet_file)
    calc_frequency()

if __name__ == '__main__':
    main()



