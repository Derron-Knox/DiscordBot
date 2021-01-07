import discord
from discord.ext import commands


class modcommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount=6):
        if ctx.message.author.permissions_in(ctx.message.channel).manage_messages:
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send("You don't have permission to do this")

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.permissions_in(ctx.message.channel).kick_members:
            await member.kick(reason=reason)
        else:
            await ctx.send("You don't have permission to do this")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.permissions_in(ctx.message.channel).ban_members:
            await member.ban(reason=reason)
        else:
            await ctx.send("You don't have permission to do this")

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if ctx.message.author.permissions_in(ctx.message.channel).ban_members:
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                    return


def setup(client):
    client.add_cog(modcommands(client))