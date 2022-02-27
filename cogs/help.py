import discord
from discord.ext import commands
from discord.errors import Forbidden
from config import Config


async def send_embed(ctx, embed):
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        await ctx.author.send(
            f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
            f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


class Help(commands.Cog):
    def __init__(self, bot, Config):
        self.bot = bot
        self.config = Config

    @commands.command()
    async def help(self, ctx, *input):
        prefix = self.bot.config["COMMAND_PREFIX"] # ENTER YOUR PREFIX - loaded from config, as string or how ever you want!

        if not input:
            emb = discord.Embed(title='Commands and modules', color=self.config.mainColor, description=f'Use `{prefix}help <module>` to gain more information about that module ' f':smiley:\n')

            cogs_desc = ''
            for cog in self.bot.cogs:
                if cog != "events" and cog != "OwnerCog":
                    cogs_desc += f'`{cog}`\n'

            emb.add_field(name='Modules', value=cogs_desc, inline=False)

            commands_desc = ''
            for command in self.bot.walk_commands():
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

        elif len(input) == 1:
            for cog in self.bot.cogs:
                if cog.lower() == input[0].lower():

                    emb = discord.Embed(title=f'{cog} - Commands', description=f"Down below you have a list with all commands from {cog} module", color=self.config.mainColor)
                    commands_list = ""
                    for command in self.bot.get_cog(cog).get_commands():
                        if not command.hidden:
                            commands_list += f"{prefix}{command.name}\n"
                    emb.add_field(name='Commands', value=commands_list, inline=False)
                    break
            else:
                emb = discord.Embed(title="What's that?!", description=f"I've never heard from a module called `{input[0]}` before :scream:", color=self.config.mainColor)

        elif len(input) > 1:
            emb = discord.Embed(title="That's too much.", description="Please request only one module at once :sweat_smile:", color=self.config.mainColor)

        await send_embed(ctx, emb)


def setup(client):
    client.add_cog(Help(client, Config()))