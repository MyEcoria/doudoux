import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Bot de MyEcoria")

@bot.event
async def on_ready():
        print("C'est parti mon kiki !")

@bot.command()
async def coucou(ctx):
        server = ctx.guild
        serverDiscordNameCoucou = server.name
        await ctx.send(f"Coucou jeune **padawan** et bienvenue sur le serveur de **{serverDiscordNameCoucou}**")

@bot.command()
async def bonjour(ctx):
        server = ctx.guild
        serverDiscordNameBonjour = server.name
        await ctx.send(f"Bonjour jeune **padawan** et bienvenue sur le serveur de **{serverDiscordNameBonjour}**")

@bot.command()
async def don(ctx):
        nanoAdresse = "nano_3qbb3pn5yhiqkrqztfn7q4ffjo73szz4z5e7hp838uaa4e195oooiowwmyb5"
        ethereumAdresse = "0x3b34E0F5d167FE4CacC48c7C8d31437db4ac0a6B"
        await ctx.send(f"**Me faire un don:** \n nano: \n")
        await ctx.send(f"> `{nanoAdresse}` \n Ethereum: \n")
        await ctx.send(f"> `{ethereumAdresse}`")

@bot.command()
async def commandesInfos(ctx):
        await ctx.send(f"Les commandes de ce bot son: \n `!coucou` \n `!bonjour` \n `!don` \n `!serverInfo` \n `!commandesInfos` \n `!films` \n `!twitchlive`")

@bot.command()
async def films(ctx):
        await ctx.send(f"**Liste des films disponibles grace Ã  DoudouxBot:** \n \n **https://bit.ly/3BfuQe7 \n https://bit.ly/3jnjxKB \n https://bit.ly/3yjaluZ \n https://bit.ly/3kulIeH \n https://bit.ly/3Bn8RSD \n https://bit.ly/3jtbRqx **")

@bot.command()
async def twitchlive(ctx):
        await ctx.send(f"**La chaine twitch de DoudouxGamingBzh: https://www.twitch.tv/doudouxgamingbzh**")

@bot.command()
async def serverInfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possÃ¨de {numberOfTextChannels} salons Ã©crit et {numberOfVoiceChannels} salon vocaux."
	await ctx.send(message)

bot.run("ODgwNDE1Mzc4NzIxODkwMzM1.YSd8tw.d3HYGsyn8LcMvTCct-cR7f6GOCc")
