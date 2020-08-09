import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix= '$')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'fumo! {round(client.latency * 1000)}ms')

# @client.command(aliases=['odeio cigarro', 'odeiocigarro'])
# async def cigarro(ctx, member: discord.Member):
#     await kick(ctx, member)

@client.command(aliases=['odeio cigarro', 'odeiocigarro'])
async def membros(ctx):
    members = ctx.guild.members
    #member_name, member_discriminator = member.split('#')

    for memb in members:
        await ctx.send(f'{memb.mention} fumante entrou as {memb.joined_at}\n')


@client.command(aliases=['pergunta', 'test'])
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


client.run('NzQwOTg4MzA5NzAyMDQ5ODQ0.XyxBIw.3UonLKmh_YTVplIs_NhyHhfI_ow')