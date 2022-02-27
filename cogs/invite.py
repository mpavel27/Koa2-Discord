import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from config import Config
import datetime

import json

class Invite(commands.Cog):
    def __init__(self, client, Config):
        self.config = Config
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        file = open('invites.json')
        self.client.invites = json.load(file)
        fileData = open('data.json')
        self.client.data = json.load(fileData)
        await self.updateLeaderboard()

    @commands.command()
    async def invites(self, ctx):
        if str(ctx.author.id) in self.client.invites:
            totalInvites = len(self.client.invites[str(ctx.author.id)]['members'])
        else:
            totalInvites = 0
        await ctx.send(f"{ctx.author.mention} invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")
        

    @commands.command(hidden=True)
    @has_permissions(administrator=True)
    async def leaderboard(self, ctx):
        channel = self.client.get_channel(self.client.data['leaderboardChannel'])
        message = discord.utils.get(await channel.history(limit=100).flatten(), id=self.client.data['leaderboard'])
        if(message is not None and 'leaderboard' in self.client.data):
            await self.updateLeaderboard()
        else:
            embed = discord.Embed(
                title = "Live Leaderboard - Top 10 Inviters",
                colour = self.config.mainColor,
            )
            msg = await ctx.send(embed=embed)
            self.client.data['leaderboard'] = msg.id
            self.client.data['leaderboardChannel'] = msg.channel.id
            with open("data.json", "w") as file:
                file.write(json.dumps(self.client.data))
            await self.updateLeaderboard()

    async def updateLeaderboard(self):
        if 'leaderboard' in self.client.data and 'leaderboardChannel' in self.client.data:
            sort = sorted(self.client.invites,key = lambda item:len(self.client.invites[item]["members"]), reverse = True)
            channel = self.client.get_channel(self.client.data['leaderboardChannel'])
            msg = discord.utils.get(await channel.history(limit=100).flatten(), id=self.client.data['leaderboard'])
            embed = discord.Embed(
                title = "Live Leaderboard - Top 10 Inviters",
                colour = self.config.mainColor,
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f"Here you can see all the best inviters from the server.\n{self.config.embedCopyright}")
            emojies = [':first_place:', ':second_place:', ':third_place:']
            for x in range(0, 9):
                if x < len(sort):
                    userName = self.client.get_user(int(sort[x]))
                    userInvites = len(self.client.invites[str(sort[x])]['members']) if str(sort[x]) in self.client.invites else 0
                    embed.add_field(name=f"{x+1}. {userName} {emojies[x] if x < 3 else ''}", value=f"Invited - {userInvites} member{'' if userInvites == 1 else 's'}", inline=False)
            await msg.edit(embed=embed)


def setup(client):
    client.add_cog(Invite(client, Config()))