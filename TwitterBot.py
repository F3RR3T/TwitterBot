#!/usr/bin/python
import tweepy
import random

def word(pos):
	if pos =="verb":
		pos =StripWords(RandomVerb())
	elif pos =="noun":
		pos = StripWords(RandomNoun())
	elif pos == "ad":
		pos = StripWords(RandomAdjective())
	else:
		pos ="help"
		print("error")
	return (pos);
		

def StripWords(words):
	words = ''.join (i for i in words if not i.isdigit())
	words = words.replace("'","")
	words = words.replace(",","")
	words = words.replace('"','')
	words = words.replace('\n','')
	return (words);
	

def CreateWord():
	print("Tweeting this sentence:")
	
	return("there was this "+ word("ad")+" "+ word("noun")+ " that " + word("verb") +" into a "+ RandomNoun())+ " and realized it was actually a large " +word("noun") 
		
	main()
	
def	RandomAdjective():

	InfileAdjective = open("adjectives2.txt", "r")
	linelist = InfileAdjective.readlines()
	rand = random.randrange(1,len(linelist))
	adjective = (linelist [rand])
	return (adjective);

def	RandomNoun():
	
	InfileNoun = open("noun2.txt", "r")
	linelist = InfileNoun.readlines()
	rand = random.randrange(1,len(linelist))
	noun = (linelist [rand])
	return (noun);
	
def RandomVerb():      
	
	InfileVerbs = open("verbs1.txt", "r")
	linelist = InfileVerbs.readlines()
	rand2 = random.randrange(1,len(linelist))
	verb = (linelist [rand2])
	return (verb);
	

def PostTwitter(words):
	CONSUMER_KEY = 'xxxxxxxx'
	CONSUMER_SECRET = 'xxxxxxx' # Make sure access level is Read And Write in the Settings tab
	ACCESS_KEY = 'xxxxxxxxx'
	ACCESS_SECRET = 'xxxxxxxxxx'
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	api.update_status(words)
	print ("it tweeted")
	
def main():
	option = raw_input("1 for random quote \n2 for a typed tweet  \n3 for a random sentence \n4 to exit \n")
	if option == "1":
		quotes=quote()
		PostTwitter(quotes)
		print ("tweeting")
		raw_input("press enter to exit")
		main()
		
	elif option == "2":
		tweet = raw_input("what would you like to tweet \n")
		PostTwitter(tweet)
		print ("tweeting")
	elif option =="4":
		quit()
		
	elif option == "3":
		sentence = CreateWord()
		print (sentence) 
		PostTwitter(sentence)
		print("tweeting")
		raw_input("press enter to exit")
	
			
			
		main()
	
	
	else:
		print("that was not an option")
		main()
	
	return;
	
def quote():
	
	infile = open("quotes.txt", "r")
	linelist = infile.readlines()
	rand = random.randrange(1,len(linelist))
	quote = (linelist [rand])
	quote = StripWords(quote)
	print (quote)
	return(quote);

	
main()
