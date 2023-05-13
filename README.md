# Encourage-Bot

Encourage Bot is a discord bot that is a chatbot that provides motivation, comfort, and entertainment to users through encouraging messages, suggestions for motivational and lofi comfort songs,  designed to help users who may be feeling down, stressed, or in need of a pick-me-up. The bot's personalized messages, motivational quotes, and carefully selected songs can help users relax, focus, and feel better. With its easy-to-use interface, Encourage Bot is accessible to everyone and can be used whenever and wherever needed. Its features make it a valuable tool for anyone looking for a little support and encouragement in their daily life.

# How to create a discord bot

In order to work with the Python library and the Discord API, we must first create a Discord Bot account.

Here are the step to creating a Discord Bot account.

1. Make sure you’re logged on to the Discord website.
2. Navigate to the application page.
3. Click on the “New Application” button.
4. Give the application a name and click “Create”.
5. Go to the “Bot” tab and then click “Add Bot”. You will have to confirm by clicking "Yes, do it!"
6. Keep the default settings for Public Bot (checked) and Require OAuth2 Code Grant (unchecked).

Your bot has been created. The next step is to copy the token.
This token is your bot's password so don't share it with anybody. It could allow someone to log in to your bot and do all sorts of bad things.

You can regenerate the token if it accidentally gets shared.

# How to Invite Your Bot to Join a Server

Now you have to get your Bot User into a server. To do this, you should create an invite URL for it.

Go to the "OAuth2" tab. Then select "bot" under the "scopes" section.
Now choose the permissions you want for the bot. Our bot is going to mainly use text messages so we don't need a lot of the permissions. You may need more depending on what you want your bot to do. Be careful with the "Administrator" permission.

After selecting the appropriate permissions, click the 'copy' button above the permissions. That will copy a URL which can be used to add the bot to a server.

Paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”.

To add the bot, your account needs "Manage Server" permissions.

Now that you've created the bot user, we'll start writing the Python code for the bot.

# Coding part

We are using Python. And in python we are using Hikari and Hikari Lightbulb Libraries.

Hikari and Hikari Lightbulb are Python libraries designed to simplify the process of building Discord bots.

Hikari provides low-level access to the Discord API, allowing developers to create custom functionality for their bots. 

Hikari Lightbulb builds on top of Hikari, offering a higher-level framework for building bots with features such as command handling, event listeners, and plugin support. Also with its high-level access to the Discord API, it provides an abstraction layer on top of Hikari and simplifies the communication with the API

# Installation

hikari-
python -m pip install -U hikari
Windows users may need to run this instead...
py -3 -m pip install -U hikari

hikari lightbulb-
pip install hikari-lightbulb

After this i have uploaded the Code files. In the bot.py file change the token to your bot token and default_enabled_guilds to your community id and run the file now your bot will start working succesfully.

# Functionality of the bot

Motivational quotes: 
Our encouragement bot can offer a variety of uplifting sayings to motivate and inspire the person using it. These motivational quotes are meant to encourage and give a positive boost to the user, helping them to feel more confident and motivated. The purpose of the quotes is to inspire and uplift the user, giving them a positive outlook on life and helping them to achieve their goals.

Motivational songs: 
Our encouragement bot has a collection of motivational songs is carefully curated to uplift and inspire the user, with each track selected for its empowering lyrics, upbeat rhythms, and motivational messages designed to help the listener overcome challenges, stay motivated, and achieve their goals.

Comfort/lofi songs: 
The bot's selection of comfort songs is thoughtfully chosen to soothe and calm the user, with each track selected for its gentle melodies, comforting lyrics, and emotional resonance, providing the listener with a sense of solace and peace during difficult times. 

Jokes:
The bot's repertoire of jokes is designed to tickle the user's funny bone and brighten their day, with each joke carefully selected to provide a lighthearted and humorous respite from the stresses of daily life.


You can add as many as messages and music suggestions or jokes in the python list files i have created.
