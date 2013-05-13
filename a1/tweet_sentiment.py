import sys, json, re

scores = {} #initalize empty dictionary
tweets = []



def parse_dict(sentiment_fp):

	for line in sentiment_fp:
		term, score = line.split("\t")
		scores[term] = int(score)



def parse_tweets(tweet_fp):

	data = []

	for line in tweet_fp:
		data.append(json.loads(line))

	for t in data:
		try:
			tweets.append(t["text"])
		except KeyError:
			pass


def calc_sentiment():

	for t in tweets:

		score = 0.0

		wordList = re.sub("[^\w]", " ",  t).split()
		for w in wordList:

			try:
				score += scores[w]
			except KeyError:
				score += 0
		
		print score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    parse_dict(sent_file)
    parse_tweets(tweet_file)
    calc_sentiment()

if __name__ == '__main__':
    main()
