import discord
import os
from dotenv import load_dotenv


client = discord.Client(self_bot=True)
bot = None
@client.event
async def on_ready():
    print(f'Logged in and ready')

@client.event
async def on_message(message):
    # if message.author == bot.user.id:
    #     return
    print('Incoming message')
    print("guild: ",message.guild)
    print("author: ",message.author)
    print("channel: ",message.channel)
    print("content: ",message.content)
    channel = message.channel
    if message.content == '@Bump Reminder':
        commands = await message.channel.application_commands()
        print("commands",commands)
        for command in commands:
            print("command", command.name)
            if command.name == "bump":
                command_res = await command.__call__(channel=channel) #, user=command.user)
                print(command_res)

load_dotenv()
token = os.getenv("TOKEN")
print("LOGGING IN WITH TOKEN: ", token)
client.run(token)

