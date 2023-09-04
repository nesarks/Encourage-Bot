import hikari
import lightbulb
import random
import text
import music
import jokes


bot = lightbulb.BotApp(
    token='MTA5MjExNjg5NDMxNzgwNTU4OA.GWaAgQ.Z47N44fdUNH80Z8hxTalI6f85tbYNOlkTNXNaU',#(Add your owwn Bot Key here)
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(1090187834700345344)
)

# Define a list of encouragement messages
encouragement_messages = text.encouragement_messages


# Define a list of motivational songs
motivational_songs = music.motivational_songs

#Define a list of comfort/lofi songs
comfort_lofi = music.comfort_lofi_songs


#Define a list of Jokes
Joke = jokes.silly_jokes

@bot.command
@lightbulb.command('encourage', 'Sends a random motivational message')
@lightbulb.implements(lightbulb.SlashCommand)
async def encourage_command(ctx: lightbulb.Context):
    
    message = random.choice(encouragement_messages)
    await ctx.respond(message)

    
@bot.command
@lightbulb.command('motivational_songs', 'Suggests a random motivational song')
@lightbulb.implements(lightbulb.SlashCommand)
async def motivate_command(ctx):
    # Select a random motivational song from the list
    song = random.choice(motivational_songs)
    
    # Send the song as a plain text message
    await ctx.respond(f"Here's a motivational song for you: {song}")

@bot.command
@lightbulb.command('comfort_lofi', 'Suggests a random comfort/lofi song')
@lightbulb.implements(lightbulb.SlashCommand)
async def motivate_command(ctx):
    # Select a random comfort/lofi song from the list
    song = random.choice(comfort_lofi)
    
    # Send the song as a plain text message
    await ctx.respond(f"Here's a comfort/lofi song for you: {song}")


@bot.command
@lightbulb.command('jokes', 'Tells a silly joke')
@lightbulb.implements(lightbulb.SlashCommand)
async def jokes_command(ctx):
    Jo = random.choice(Joke)
    await ctx.respond(Jo)




bot.run()
