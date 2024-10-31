from discord.ext import commands, tasks

import discord

class DisboardResponder(commands.Cog, name="Disboard Responder"):
    def __init__(self, bot, intents) -> None:
        self.bot = bot
        self.intents = intents


    @commands.Cog.listener()
    async def on_message(self, message):
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

    @commands.Cog.listener()
    async def on_ready(self):
            print(f'Logged in and ready')

async def setup(bot) -> None:
    await bot.add_cog(DisboardResponder(bot))
