import discord
from discord.ext import commands, tasks
import random
from google import google
import time
from itertools import cycle

status = cycle(['seu cu no meu pau', 'sua boca na minha pica'])

client = commands.Bot(command_prefix= '$')

def search(search):
    _search_ = google.search(search, 1)
    search_ = _search_[0]
    return search_.name, search_.description, search_.link

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_ready():
    change_status.start()
    #lista_canais = discord.guild.channels
    #teste = client.get_channel(lista_canais[0])
    #await client.send_message(destination=teste, content='Cheguei nessa porra')
    for guild in client.guilds:
         for channel in guild.channels:
             if channel.name == "geraldo" or channel.name == "bot" or channel.name == "testando-bot":
                 await channel.send('quem leu é viado')
    print('Bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'fumo! {round(client.latency * 1000)}ms')


@client.command(aliases=['component', 'datasheet'])
async def componente(ctx, *, componente):
    await ctx.send(f'aqui: https://www.alldatasheet.com/view.jsp?Searchword={componente}')

# @client.event
# async def on_message(message):
#     channel = message.channel
#     await channel.send(f'{message.author} Calaboca sua puta')


@client.command(aliases=['ask', 'question'])
async def pergunta(ctx, *args):
    mensagem = search(str(args))
    await ctx.send(f'Oque encontrei foi : {mensagem[0]}\n\nDescrição: {mensagem[1]}\n\nPode ser acessado em: {mensagem[2]}')

# @client.command(aliases=['odeio cigarro', 'odeiocigarro'])
# async def cigarro(ctx, member: discord.Member):
#     await kick(ctx, member)

@client.command()
async def membros(ctx):
    members = ctx.guild.members
    #member_name, member_discriminator = member.split('#')

    for memb in members:
        await ctx.send(f'{memb.mention} fumante entrou as {memb.joined_at}\n')

@client.command()
async def biri(ctx):
    for i in range (20):
        await ctx.send('pls porngif')
        time.sleep(1)


@client.command(aliases=['test'])
async def _8ball(ctx, *, question):
    responses = ['Certamente um cigarro é a melhor opção',
        'Um malboro se enquadraria nesse caso',
        'Não, pare com isso e vá fumar',
        'delicia de cigarro',
        'Não sei, podemos ir fumar?',
        'quero Maconha',
        'Não sei oque responder a isso, vamos fumar?']
    await ctx.send(f'Olha só {ctx.guild.me.mention},\nQuestão: {question}\nResposta: {random.choice(responses)}')


@client.command()
async def info(ctx, *, member: discord.Member):
    await ctx.send(f'Entrou as: {member.joined_at}\nnick: {member.nick}\nGuild: {member.guild}\nStatus: {member.status}\navatar: {member.avatar_url}\nRelação: {member.relationship}')


@client.command(aliases=['musica', 'music'])
async def spotify(ctx, *, member: discord.Member):
    print(dir(member))
    spotify = member.activity
    await ctx.send(f'Artista: {spotify.title}\nArtista: {spotify.artist}\nAlbum: {spotify.album}\nDuração: {spotify.duration}\n')

@client.command(aliases=['manda', 'envia'])
async def message(ctx, *args):
    print(ctx.message.mentions)
    member = ctx.message.mentions[0]
    lista = []
    for agr in args:
        lista.append(agr)
    lista.pop(0)
    content = ' '.join(lista) 
    if member.dm_channel:
        await member.dm_channel.send(content=content, tts=True, delete_after=3)
    else:
        await member.create_dm()
        await member.dm_channel.send(content=content, tts=True, delete_after=3)

print(client.get_all_channels)
#print(dir(discord))

    
client.run('')