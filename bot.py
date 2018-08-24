import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='u.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

bot.run('<NDgyMTY1MDk3NDI3MzcwMDA1.DmERkQ.Bg_yy6NNprjads6dHSrrgYBLnnE>')
