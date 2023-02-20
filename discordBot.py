import os
import openai
import discord
import config

def askChatGPT(userPrompt):
    response = openai.Completion.create(model="text-davinci-003", prompt=userPrompt, temperature=0, max_tokens=3700)
    return response

openai.api_key = config.openai.api_key

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
    
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game('-help'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.lower().startswith('-help'):
        await message.channel.send("-ask {your message here}")
        
    elif message.content.lower().startswith('-ask '):
        query = message.content[5:]
        response = askChatGPT(query)
        print(response["choices"][0]["text"])
        await message.channel.send(response["choices"][0]["text"])

client.run(config.discordKey)
