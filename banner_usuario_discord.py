import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 
 
@bot.command()
async def banner(ctx, usuario:discord.Member):
    if usuario == None:
        usuario = ctx.author
    req = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=usuario.id))
    banner_id = req["banner"]
   
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{usuario.id}/{banner_id}?size=1024"

    try:

     await ctx.send(f"{banner_url}")
    except UnboundLocalError:
       await ctx.send("No tiene banner❌")
        
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('') #OBTEN UN TOKEN EN: https://discord.com/developers/applications