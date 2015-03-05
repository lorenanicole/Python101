Python 101
==========

A gentle introduction to python.

Setup
-----

1. Download [sublime](http://www.sublimetext.com/ "Sublime")
2. Download the [sample code](https://github.com/lorenanicole/Python101)

For more:

http://learnpythonthehardway.org/
```
with open('my_tweets.csv', 'wb') as csv_file:
	writer = csv.writer(csv_file)
	for tweet in twitter.get_user_timeline():
		writer.writerow([tweet['created_at'], tweet['text']])

```
