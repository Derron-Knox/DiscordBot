import discord
from discord.ext import commands, tasks
from itertools import cycle

class statcoms(commands.Cog):

    status = cycle(["Suck it!",
                    "I'm just a sexy boy",
                    "The Heartbreak Kid!",
                    "I am simply the very best sports entertainer",
                    "It's time to stop your grinnin' and drop your linen!"])

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print('Bot is up and ready')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please pass in all required arguments')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("That's not a command")

    @tasks.loop(seconds=1800)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(self.status)))

    # Alerts server when a user joins
    @commands.command()
    async def on_member_join(self, member):
        for channel in member.guild.channels:
            if str(channel) == "squaredcircle":
                await channel.send(f"""{member.mention} has entered the ring""")
                print(f"""{member} has joined""")

    # Alerts when a user leaves
    @commands.command()
    async def on_member_remove(self, member):
        for channel in member.guild.channels:
            if str(channel) == "squaredcircle":
                await channel.send(f"""{member.mention} has been eliminated""")
                print(f"""{member} has left""")

def setup(client):
    client.add_cog(statcoms(client))
