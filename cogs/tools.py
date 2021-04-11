import discord
import json
import sys
import time

from utils.ctx_class import MyContext
from utils.cog_class import Cog

from discord.ext import commands
from discord.utils import get

with open('release.json') as f:
    data = json.load(f)
    release = data['sVersion']

class Tools(Cog):
    @commands.command()
    async def version(self, ctx: MyContext):
        """
        Returns bot system info/version
        """
        verEmbed = discord.Embed(title="Salvator Version Info", description='', color=0xe14414)
        verEmbed.add_field(name='Version', value=data['sVersion'], inline='true')
        verEmbed.add_field(name='Release Date', value=data['releaseDate'], inline='true')
        verEmbed.add_field(name='Have Issues?', value='Let us know at our GitHub page!\n https://github.com/Grick-Heart-Project/Grick-Heart', inline='false')
        verEmbed.add_field(name='System Info', value=f'Running Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} on {sys.platform}', inline='true')
        await ctx.send(embed=verEmbed)

    @commands.command()
    async def invite(self, ctx: MyContext):
        """
        Grabs bot invite link/support server link
        """
        inviteEmbed = discord.Embed(title='Salvator Invite Links', color=0xe14414)
        inviteEmbed.add_field(name='Bot Invite', value=f'https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=872934480', inline=True)
        inviteEmbed.add_field(name='Support Server Invite', value='https://discord.gg/myJh5hkjpS')
        inviteEmbed.set_footer(text=f'Current Bot Version: v{release}')
        await ctx.send(embed=inviteEmbed)

    @commands.command()
    async def credits(self, ctx: MyContext):
        """
        Returns bot credits
        """
        hydro: discord.User = await self.bot.fetch_user(711960088553717781)
        eyes: discord.User =  await self.bot.fetch_user(138751484517941259)
        zero: discord.User = await self.bot.fetch_user(661660243033456652)
        hydro_mention: str = hydro.mention
        eyes_mention: str = eyes.mention
        zero_mention: str = zero.mention
        creditsEmbed = discord.Embed(title='Salvator Credits', color=0xe14414)
        creditsEmbed.add_field(name='Developer', value=hydro_mention)
        creditsEmbed.add_field(name='Developer', value=zero_mention)
        creditsEmbed.add_field(name='Bot Framework Developer', value=eyes_mention)
        creditsEmbed.add_field(name='Copyright', value='"Never Gonna Give You Up" was created by Rick Astley, and is owned by RCA Records', inline=False)
        creditsEmbed.set_footer(text=f'Current Bot Version: v{release}')
        await ctx.send(embed=creditsEmbed)

    @commands.command()
    async def ping(self, ctx: MyContext):
        """
        Check that the bot is online, give the latency between the bot and discord servers.
        """
        _ = await ctx.get_translate_function()

        t_1 = time.perf_counter()
        await ctx.trigger_typing()  # tell Discord that the bot is "typing", which is a very simple request
        t_2 = time.perf_counter()
        time_delta = round((t_2 - t_1) * 1000)  # calculate the time needed to trigger typing
        await ctx.send(_("Pong. — Time taken: {miliseconds}ms", miliseconds=time_delta))  # send a message telling the user the calculated ping time


setup = Tools.setup
