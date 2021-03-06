import discord 
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import sys, traceback
import random
import datetime
import time


class Mod:
    """Moderator Commands"""
    def __init__(self, bot):
        self.bot = bot

    

    @commands.command(pass_context=True, aliases=["clear"])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount):
        """Clear messages from the chat"""
        try:
            x = int(amount)
            if x < 2 or x > 500:
                return await ctx.send("Must be in range of 2 to 500 messages.")
            await ctx.channel.purge(limit=x)
            await ctx.send("Cleared {} messages for you. Emjoy the clear chat!", delete_after=5)
        except ValueError:
            await ctx.send("Please select a number.")
        except commands.errors.MissingPermissions:
            await ctx.send("You lack the permissions to use this command")
        except Exception as e:
            await ctx.send("Something went wrong. Here it is: {}".format(e))
            print(e)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member):
        """Kick a user from your discord server."""
        try:
            await ctx.send(f"**{user.name}** has been kicked from the server.")
            await ctx.guild.kick(user)
        except discord.Forbidden:
            await ctx.send(f"Bravo Zulu lacks the permission to kick **{user.name}**.")
        except commands.errors.MissingPermissions:
            await ctx.send("You don't have the nessecary perms to do that.")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member):
        """Ban a user from your discord server."""
        try:
            await ctx.send(f'**{user.name}** is now banned from the server!')
            await ctx.guild.ban(user)
        except discord.Forbidden:
            await ctx.send(f"Bravo Zulu lacks the permission to ban **{user.name}**.")
        except commands.errors.MissingPermissions:
            await ctx.send("no perms bro")
            

    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, user: discord.Member = None):
        """Mute a user. Works only for 1 channel."""
        if user is None:
            return await ctx.send("Please tag the user in order to mute them.")
        try:
            await ctx.channel.set_permissions(user, send_messages=False)
            return await ctx.send(f"{user.mention} has been muted. Unmute them when you see fit.")
        except commands.errors.MissingPermissions:
            return await ctx.send("You lack perms")
        except discord.Forbidden:
            return await ctx.send("I lack the **Manage channel** permission.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, user: discord.Member = None):
        """Unmute a user from 1 channel."""
        if user is None:
            return await ctx.send("Please tag the user in order to unmute them")
        try:
            await ctx.channel.set_permissions(user, send_messages=True)
            return await ctx.send(f"{user.mention} has been unmuted. Enjoy freedom. While it lasts.")
        except commands.errors.MissingPermissions:
            return await ctx.send("You lack perms")
        except discord.Forbidden:
            return await ctx.send("I lack the **Manage Channel** permission.")

    
        
     
        
        
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def softban(self, ctx, user: discord.Member):
        """Soft bans a member from the server.
        """

        obj = discord.Object(id=user)
        await ctx.guild.ban(obj, reason=reason)
        await ctx.guild.unban(obj, reason=reason)
        await ctx.send('YeAh BOI! That ~~bitch~~ user got ~~soft~~banned!!!')
        


def setup(bot):
    bot.add_cog(Mod(bot))
