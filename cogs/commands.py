import discord
from discord.ext import commands
from cogs.invite import Invite

from nextcord import File # pip install nextcord
from easy_pil import Canvas, Editor, Font, load_image_async # pip install easy-pil

from config import Config
import datetime

class Commands(commands.Cog):
    def __init__(self, client, Config):
        self.config = Config
        self.client = client

    @commands.command()
    async def stats(self, ctx, user: discord.Member = None):
        today = datetime.datetime.utcnow()
        time = today.strftime("%H:%M")
        target = user if user is not None else ctx.author
        user_data = {
            "name": str(target.name),
            "nameTag": str(target),
            "invites": str(len(self.client.invites[str(target.id)]['members'])) if str(target.id) in self.client.invites else "0",
            "created_at": str(target.created_at.strftime("%d.%m.%Y")),
            "joined_at": str(target.joined_at.strftime("%d.%m.%Y")),
            "role": str(target.top_role.name)
        }
        background = Editor(Canvas((800, 240), color="#23272A"))

        avatarLink = target.default_avatar if not hasattr(target.avatar, 'url') else target.avatar.url
        profile_image = await load_image_async(str(avatarLink))
        profile = Editor(profile_image).resize((200, 200)).circle_image()

        font_40 = Font.poppins(size=40)
        font_20 = Font.montserrat(size=20)
        font_15 = Font.montserrat(size=15)
        font_25 = Font.poppins(size=25)
        font_40_bold = Font.poppins(size=40, variant="bold")

        background.paste(profile, (20, 20))
        background.ellipse((20, 20), 200, 200, outline=str(target.top_role.color), stroke_width=3)
        background.text((240, 20), user_data["name"], font=font_40, color="white")
        background.text((770, 30), user_data["nameTag"], font=font_20, color="white", align='right')
        background.text((770, 200), self.config.embedCopyright, font=font_15, color="white", align='right')
        background.text((495, 30), time, font=font_25, color='white', align='center')
        background.text((240, 70), "Invites: " + user_data["invites"] , font=font_25, color="white")
        background.text((240, 110), "Account Created: " + user_data["created_at"] , font=font_25, color="white")
        background.text((240, 150), "Joined Us: " + user_data["joined_at"] , font=font_25, color="white")
        background.text((240, 190), "Role:", font=font_25, color="white")
        background.text((310, 190), user_data["role"] , font=font_25, color=str(target.top_role.color))

        file = File(fp=background.image_bytes, filename='stats.png')
        print(file)
        await ctx.send(file=file)

def setup(client):
    client.add_cog(Commands(client, Config()))