import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message: discord.Message):
    # Empêcher le bot de répondre à lui-même
    if message.author == bot.user:
        return
    
    channel_alert = bot.get_channel(1355408554336456856)

    # Remplace par l'ID de l'utilisateur à surveiller
    linker_id = 1355406939353383014  # ID de la personne cible

    # admin
    message_text = "EG_rix issued server command: /tp vers un autre joueur"
    mot_cible = "issued server command: /tp"


    if message.guild:
        luc = message.guild.get_member(1234145217095929909)

    # Liste des mots à rechercher
    mots_cibles = ["issued server command: /tp", "issued server command: /give", "issued server command: /locate", "issued server command: /gamemode", "issued server command: /xp"]

    # Vérifier si le message vient de la personne ciblée et contient un mot cible
    if message.author.id == linker_id and any(mot in message.content.lower() for mot in mots_cibles):
        await channel_alert.send(f"{luc.mention}, une commande a était executée !")
        


    # Vérifier si le message est "bonjour"
    if message.content.lower() == 'bonjour':
        await message.channel.send("Salut ...")

bot.run(os.getenv('DISCORD_TOKEN'))
