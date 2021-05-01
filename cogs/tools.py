import discord
from typing import Optional

from discord.ext import commands, tasks
from discord.utils import get
from discord.utils import escape_markdown, escape_mentions

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import get_from_db

class RickTools(Cog):
    @commands.command(aliases=['config'])
    async def configuration(self, ctx: MyContext, option = 0):
        """
        Salvator's Configuration
        """
        if option < 1 or option > 2:
            embed = discord.Embed(title='Salvator\'s Response Configurator', description='You can configure how Salvator should respond to Rick Roll links', color=self.bot.color)
            embed.add_field(name='Delete Links (1)', value='Salvator will delete any links that have been reported as Rick Rolls.', inline=False)
            embed.add_field(name='Warn Links (2)', value='Salvator will warn people if a link has been reported as a Rick Roll', inline=False)
            embed.set_footer(text='Add the corresponding number as an argument to this command to set')
            await ctx.send(embed=embed)
        else:
            db_guild = await get_from_db(ctx.guild)
            if option != 0:
                db_guild.rickpref = int(option)
            await db_guild.save()

            _ = await ctx.get_translate_function()
            if db_guild.rickpref:
                await ctx.send(_('The server Rick-Roll preference is `{value}`',
                                 value=escape_mentions(escape_markdown(str(db_guild.rickpref)))))
            else:
                await ctx.send(_('There is no specific preference set for this guild.'))




setup = RickTools.setup
