from datetime import datetime

def twitter_datetime_to_python_datetime(twitter_date_string):
	return datetime.strptime(twitter_date_string, '%a %b %d %H:%M:%S +0000 %Y')