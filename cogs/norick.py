import discord
import json

from discord.ext import commands

from utils.cog_class import Cog
from utils.models import get_from_db

class NoRickCog(Cog):
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        with open('ricks.json') as f:
            url_list = json.load(f)

        if message.author == self.bot.user:
            return
        
        db_guild = await get_from_db(message.guild)
        if len(message.content) > 0:
            for word in message.content.split():
                if word in url_list:
                    if db_guild.rickpref == 2:
                        await message.reply(':octagonal_sign: WARNING: This is a Rick-Roll. Proceed with caution...')
                    else:
                        await message.channel.send(f'Hey {message.author.mention}, that wasn\'t very nice of you! (Message deleted was a Rick-Roll)', delete_after=60)
                        await message.delete()
                    return

setup = NoRickCog.setup