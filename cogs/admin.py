import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

import json

import sys
sys.path.append("../")
from config import Config

class Admin(commands.Cog):
    def __init__(self, client, Config):
        self.config = Config
        self.client = client
    
    @commands.command(hidden=True)
    @has_permissions(administrator=True)
    async def rules(self, ctx):
        rulesChannel = self.client.get_channel(926321641162678322)
        embed = discord.Embed(
            title = "Discord General Rules",
            colour = self.config.mainColor,
            description = "Every player from our community should understand our rules to be able to play on the server otherwise you'll be punished.\n\n1. We do not tolerate toxic behavior in our community.\n2. You cannot post sexual content on any channel.\n3. You cannot post racist content, regardless of the subject.\n4. You cannot request any roles from any administrators.\n5. You cannot publish any personal pieces of information, even if it's your information or that of other players. (names, addresses, e-mails, password, bank account, cards, or any other thing that can affect somebody).\n6. You cannot spam on any channel, even if it is a bot command.\n7. You cannot send messages about other communities.",
        )
        embed.set_footer(text=self.config.embedCopyright)
        await rulesChannel.send(embed=embed)

    @commands.command(hidden=True)
    @has_permissions(administrator=True)
    async def regulament(self, ctx):
        rulesChannel = self.client.get_channel(1045022262874624185)
        embed = discord.Embed(
            title = "Regulament General",
            colour = self.config.mainColor,
            description = "Fiecare jucator din comunitatea noastra ar trebui sa inteleaga regulamentul nostru pentru a putea juca pe server.\n\n1. Nu toleram comportamente toxice in comunitatea noastra.\n2. Nu puteti posta continut sexual pe niciun canal.\n3. Nu puteti posta continut rasist, indiferent de subiect.\n4. Nu puteti solicita niciun rol de la niciun administrator.\n5. Nu puteti publica informatii personale, chiar daca sunt informatiile tale sau ale altor jucatori. (nume, adresa, e-mail, parole, conturi bancare, carduri sau orice alt lucru care poate afecta pe cineva)\n6. Nu puteti face spam pe nici un canal, chiar daca este o comanda de la orice bot.\n7. Nu puteti trimite mesaje despre alte comunitati.",
        )
        embed.set_footer(text=self.config.embedCopyright)
        await rulesChannel.send(embed=embed)

    @commands.command(hidden=True)
    @has_permissions(administrator=True)
    async def overview(self, ctx):
        overviewChannel = self.client.get_channel(926333309414441000)
        embed = discord.Embed(
            title = "Server Overview",
            colour = self.config.mainColor,
            description = "As you know, we want to keep you all up to date with all the pieces of information about the server so here you have some useful links that might help you.\n\nTime Zone: **Eastern European Standard Time (GMT+2)**\n\nWebsite: https://koa2.ro/\nDiscord: https://koa2.ro/discord\nDownloads: https://koa2.ro/downloads",
        )
        embed.set_footer(text=self.config.embedCopyright)
        await overviewChannel.send(embed=embed)

    @commands.command(hidden=True)
    @has_permissions(administrator=True)
    async def overview_ro(self, ctx):
        overviewChannel = self.client.get_channel(1045022355535175790)
        embed = discord.Embed(
            title = "Server Overview",
            colour = self.config.mainColor,
            description = "Dupa cum stiti, dorim sa va tinem pe toti la curent cu toate informatiile despre server, asa ca aici aveti cateva link-uri utile care v-ar putea ajuta.\n\nTime Zone: **Eastern European Standard Time (GMT+2)**\n\nWebsite: https://koa2.ro/\nDiscord: https://koa2.ro/discord\nDownloads: https://koa2.ro/downloads",
        )
        embed.set_footer(text=self.config.embedCopyright)
        await overviewChannel.send(embed=embed)

    @commands.command(hidden=True)
    @has_permissions(administrator=True)
    async def faq(self, ctx):
        overviewChannel = self.client.get_channel(926650411761410068)
        embed = discord.Embed(
            title = "Frequently Asked Questions",
            colour = self.config.mainColor,
            description = "Most of you might have different questions about the server and here we have the most \"asked\" questions.\n\n**1. Is the server an International project?**\n— Yes, but as you can see we are only a few members that can speak more than one language and we are trying to support you as hard as we can.\n\n**2. Why we don't have a specific channel for every nationality?**\n— At this moment, we don't have a huge team that can speak at least two languages and we decided that we will have only the English channel until we'll have a big amount of knowledge.\n\n**3. Are we going to have a multi-language system on the server?**\n— Of course, you will have several languages to select on the game itself and even on our website.\n\n**4. When is the server going to open?**\n— Currently, we are working on the server and there is no date for the upcoming lunch. Also, keep an eye on our announcements channel.\n\n**5. How can I help you?**\n— If you want to help us with the server development or mapping development, you can speak with one of our Administrators.\n\n**6. Where can I see the progress of the server?**\n— We are trying to post everything on the sneak-peaks channel and on our website.\n\n**7. What is the current stage of the server?**\n— Currently, we are working at the server and we are growing up every day.\n\n**8. What will be the maximum level on the server?**\n— The maximum level on the server will be 120.",
        )
        embed.set_footer(text=self.config.embedCopyright)
        await overviewChannel.send(embed=embed)

    @commands.command(hidden=True)
    @has_permissions(administrator=True)
    async def faq_ro(self, ctx):
        overviewChannel = self.client.get_channel(1045022431624052797)
        embed = discord.Embed(
            title = "Frequently Asked Questions",
            colour = self.config.mainColor,
            description = "Cei mai multi dintre voi ar putea avea diferite intrebari despre server, iar aici avem cele mai intrebare intrebari.\n\n**1. Este serverul un proiect international?**\n— Da, dar momentan incercam sa adunam cat mai multe persoane in staff incat sa ne putem ocupa de toate sectiuniile pentru limba aferenta.\n\n**2. De ce nu avem un canal specific pentru fiecare nationalitate in parte?**\n— In acest moment, nu avem atat de multe persoane in staff incat sa ne putem ocupa de toate sectiuniile asa ca momentan o sa avem doar limba romana pe server.\n\n**3. Vom avea sistem de multi-language pe server?**\n— Bineinteles, dar momentan o sa ne ocupam mai mult de sectiuniile in limba romana .\n\n**4. Cand se va deschide serverul?**\n— Momentan nu avem o data stabilita pentru deschiderea serverului asa ca va rugam sa asteptati pana cand o sa anuntam pe canalul nostru de anunturi.\n\n**5. Cum putem ajuta?**\n— Pentru cei ce vor sa ne ajuta in orice mod de dezvoltare a serverului va rugam sa contactati un Administrator.\n\n**6. Unde putem sa vedem progresul serverului?**\n— Incercam din toate puteriile sa va tinem la curent cu tot ce se petrece cu serverului pe canalul de sneak-peaks.\n\n**7. Care este stadiul actual al serverlui?**\n— In prezent, lucram la server si progresam in fiecare zi.\n\n**8. What will be the maximum level on the server?**\n— Nivelul maxim pe server o sa fie 120.",
        )
        embed.set_footer(text=self.config.embedCopyright)
        await overviewChannel.send(embed=embed)

    @commands.command(hidden=True)
    @has_permissions(administrator=True)
    async def questions(self, ctx):
        await ctx.send("Because we want to be as much transparent as we can, you can ask us any questions about the server on this channel. This channel have 30 seconds slowmode so make sure that your question is understandable.")

    @commands.command()
    @has_permissions(administrator=True)
    async def language_role(self, ctx):
        languages = self.config.languages
        embed = discord.Embed(
            title = "Choose Your Language",
            colour = self.config.mainColor,
            description = "If you want to see the chat rooms and some other important information, please choose your language.\n\n**We are sorry if you don't find your native language.**",
        )
        embed.set_image(url='https://i.imgur.com/9u3PTgU.png')
        message = await ctx.send(embed=embed)

        for language in languages:
            await message.add_reaction(language)

    @commands.command()
    @has_permissions(administrator=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(ctx.author.mention + ' deleted %s messages!' % amount, delete_after=2)

    @commands.command()
    @has_permissions(administrator=True)
    async def custom_embed(self, ctx, *args):
        response = '''
            {
            "title": "Testy Test",
            "description": "Hello World!",
            "color": 16711680,
            "footer": {
                "text": "I hope this works"
            },
            "timestamp": "2021-12-09T11:36:00.000+00:00"
            }
        '''
        embed = ' '.join(args)
        if "null" not in embed:
            parseEmbed = json.loads(embed)
            await ctx.message.delete()
            await ctx.send(content=parseEmbed['content'])
            for x in parseEmbed['embeds']:
                loadEmbed = discord.Embed.from_dict(x)
                await ctx.send(embed=loadEmbed)
        else:
            await ctx.send("The JSON must not contains a null value.")
        # print(parseEmbed['embeds'][0])

def setup(client):
    client.add_cog(Admin(client, Config()))