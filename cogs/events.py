import discord
from discord.ext import commands
import DiscordUtils
from cogs.invite import Invite

import sys
sys.path.append("../")
from config import Config

import json

class events(commands.Cog):
    def __init__(self, client, Config):
        self.config = Config
        self.client = client
        self.tracker = DiscordUtils.InviteTracker(client)
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        inviter = await self.tracker.fetch_inviter(member)
        channel = self.client.get_channel(926314891957121088)
        rulesChannel = self.client.get_channel(926321641162678322)
        role = self.client.guilds[0].get_role(926316890480062474)
        await member.add_roles(role)
        await channel.send(f"Welcome to our Discord server, {member.mention}! To don't be punished make sure that you read our server rules from {rulesChannel.mention}.")
        if str(inviter.id) not in self.client.invites:
            self.client.invites[str(inviter.id)] = {'members': []}
        self.client.invites[str(inviter.id)]['members'].append(member.id)
        with open("invites.json", "w") as file:
            file.write(json.dumps(self.client.invites))
        await Invite(self.client, self.config).updateLeaderboard()

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(926314891957121088)
        inviter = next((item for item in self.client.invites for item2 in self.client.invites[item]['members'] if item2 == member.id), None)
        await channel.send(f"{member.mention} has left the server. Members count: {channel.guild.member_count}")
        if str(inviter) in self.client.invites:
            self.client.invites[str(inviter)]['members'].pop(self.client.invites[str(inviter)]['members'].index(member.id))
            with open("invites.json", "w") as file:
                file.write(json.dumps(self.client.invites))
        await Invite(self.client, self.config).updateLeaderboard()

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.message.id)
    #     print(reaction.message.channel.id)
    #     # if reaction.message.channel.id != '1044009870497677434':
    #     #     return
    #     # if reaction.emoji == '🇬🇧':
    #     #     await client.add_roles(user, '1044003678329258004')
    #     #     print('role gb adaugat')
    #     # elif reaction.emoji == '🇷🇴':
    #     #     await client.add_roles(user, '1044003742116229211')
    #     #     print('role ro adaugat')
        

def setup(client):
    client.add_cog(events(client, Config()))