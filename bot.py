import discord
import os

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == self.bot.user.id:
        return
    print('Incoming message')
    print("guild: ",message.guild)
    print("author: ",message.author)
    print("channel: ",message.channel)
    print("content: ",message.content)
    channel = message.channel
    if message.content.startswith('@Bump Reminder'):
        await message.channel.send('/bump')
        async for command in channel.slash_commands(query="bump"):
            if command.name == "bump":
                break
            print(f"command: {command}")
            user = self.bot.get_user(message.user_id)
            command = await command.__call__(channel=channel, user=user)
    if message.content.startswith('!drp bump'):
        async for command in channel.slash_commands(query="bump"):
            if command.name == "bump":
                break
            print(f"command: {command}")
            user = self.bot.get_user(message.user_id)
            command = await command.__call__(channel=channel, user=user)

client.run(os.getenv("TOKEN"))

