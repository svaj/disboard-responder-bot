from discord.ext import commands, tasks

import discord

class DisboardResponder(commands.Cog):

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.user:
            return
        print('Incoming message')
        print("guild: ",message.guild)
        print("author: ",message.author)
        print("channel: ",message.channel)
        print("content: ",message.content)
        if message.content.startswith('@Bump Reminder'):
            await message.channel.send('/bump')

    @commands.Cog.listener()
    async def on_ready(self):
            print(f'Logged in and ready')

async def setup(bot) -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    await bot.add_cog(DisboardResponder(intents=intents))