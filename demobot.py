# demobot.py

import discord
from db import Database
from googlesearch import google_search
import settings as appconfig

client = discord.Client()

@client.event
async def on_ready():
	print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
	"""
		This function listen for all the message that user send 
		and response if message meets one of three 
		hi ---> hey
		!google nodejs ----> search on google for nodejs and return top
							5 results
		!recent nodejs ----> search for nodejs in the search history and return
							all the search query related to nodejs
	"""
	if message.author == client.user:
		return
	if message.content == "hi":
		await message.channel.send("hey")

	if message.content.startswith('!google'):
		try:
			user_query = message.content.split(None, 1)[1]
			author_id = message.author.id
			db = Database()
			db.connect()
			db.save_search_query(author_id, user_query)

			search_results = google_search(user_query)
			if search_results:
				links = ' \n'.join(search_results)
				response_msg = 'Here are the top five results for you query {}: \n {}'.format(
					 user_query, links)
			else:
				response_msg = 'Sorry, no matching links found for your query {}.'.format(
					user_query)
		except IndexError:
			response_msg = 'below are the example of search !google nodejs'
		await message.channel.send(response_msg)

	if message.content.startswith('!recent'):
		try:
			user_query = message.content.split(None, 1)[1]
			author_id = message.author.id
			db = Database()
			db.connect()
			results = db.fetch_recent_search_query(author_id, user_query)
			if(len(results) > 0):
				keywords = 'Here are the matching search results are: \n' + \
					' \n'.join([x[1] for x in results])
			else:
				keywords = 'Oops! No matching results found'
		except IndexError:
			keywords = 'Oops! No matching results found'
		await message.channel.send(keywords)


client.run(appconfig.DISCORD_CLIENT_TOKEN)