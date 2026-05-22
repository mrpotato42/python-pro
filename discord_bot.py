import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Información del Servidor",
        description="Aquí tienes algunos detalles del servidor actual.",
        color=discord.Color.purple()
    )
    embed.add_field(name="Miembro", value=ctx.author.name, inline=True)
    embed.add_field(name="Canal", value=ctx.channel.name, inline=True)
    embed.set_footer(text="Bot creado con discord.py")
    
    await ctx.send(embed=embed)

@bot.command()
async def health(ctx):
    ready = bot.is_ready()
    if ready: 
        await ctx.send(f"¡Hola! {ctx.author.name}. Soy {bot.user} y estoy listo para empezar")
    else:
        await ctx.send("Ups! Ocurrio un problema x.x")

if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("Error: No se encontró la variable de entorno DISCORD_TOKEN.")