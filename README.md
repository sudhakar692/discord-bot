# Discord Bot

# Instructions

* Create a simple discord bot that would reply **hey** to your **hi**. 

* Add functionality to allow a user to search on google through discord. If the user types **!google nodejs**, reply with top 5 links that you would get when you search **nodejs** on **google.com**

* Implement functionality to search through your search history. If a user uses **!google** to search for **"nodejs"** **"apple games"** **"game of thrones"**, and after these searches, if user types **!recent game**, your bot should reply with **"apple games"** and **"game of thrones"**

* Make user search history persistent. Use any storage system to store your searches, so even when you kill your nodejs server and start again, your search history is maintained.

## Steps to run bot:

1. Create and activate virtual environment -
   `python3 -m venv bot_env`
   `source bot_env/bin/activate`
2. Install dependencies -
   `pip install -r requirements.txt`
3. Create .env file and add the contents using **sample_env.txt** file.
4. Create your discord bot by visiting [developers console](https://discordapp.com/developers/applications)
5. Copy the bot token and add to .env file.
6. Create your **_Postgres Database_** and enter credentials in .env file
7. Create the **table 'Search_History'_** importing sql query from bot.sql
8. Create custom search engine using Google Search API and insert the developer and search engine ID in .env file.
9. Run the app -
   `python3 demobot.py`
