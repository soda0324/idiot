import discord
import youtube_dl
import asyncio
import os
import random
import requests

from random import choice
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get
from discord.abc import User
from discord.voice_client import VoiceClient




app = commands.Bot(command_prefix='!')



@app.event #봇준비
async def on_ready():
    game = discord.Game("영원하리 하승")
    print("안녕 나는 봇")
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=game)



@app.command() #청소
async def 청소(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    

@app.command() #호출
async def 멤버호출(ctx):
    Member = get(ctx.guild.roles, name="고멤")
    await ctx.send(f"{Member.mention}")



@app.command() #봇 통화방 입장
async def 입장(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@app.command() #봇 통화방 퇴장
async def 퇴장(ctx):
    await ctx.voice_client.disconnect()


@app.command()
async def 핑(ctx):
    await ctx.send(f'```Ping : {round(app.latency * 1000)}ms```')



@app.event 
async def on_message(message):
    helpEmbed = discord.Embed(title="하승크루", color =0x27FF44) #도움말
    helpEmbed.set_image(url="https://cdn.discordapp.com/attachments/737668156834840708/793070386001608754/18a8ad5511b6ff1f.png")
    helpEmbed.add_field(name ="!멤버호출", value ="[멤버태그를 가지고 있는 사람호출]", inline =False)
    helpEmbed.add_field(name ="!청소(숫자)", value ="[채팅청소]", inline =False)
    helpEmbed.add_field(name ="!투표 (투표하고싶은내용)", value ="[그냥 투표기능]", inline =False)
    helpEmbed.add_field(name="멤버", value="!하승ㅣ!하롱ㅣ!꼬비ㅣ!창현ㅣ!다솜ㅣ!바우", inline=False)
    helpEmbed.add_field(name="젤라틴팀", value="!소다ㅣ!무공이ㅣ!머브ㅣ!용한ㅣ!보라ㅣ!어녹", inline=False)
    if message.content == "!정보":
        await message.channel.send(embed=helpEmbed)

    #하승
    haseung = discord.Embed(title="정보", color = 0xFD5E4F)
    haseung.set_thumbnail(url="https://cdn.discordapp.com/attachments/760154235387379812/798499930586218516/fd4bd8d3b402e961.png")
    haseung.add_field(name ="나이", value ="22살", inline=True)
    haseung.add_field(name ="성별", value ="여자", inline=True)
    haseung.add_field(name ="특징", value ="하승크루 대빵", inline=False)
    if message.content == "!하승":
        await message.channel.send(embed=haseung)

    #하롱
    harong = discord.Embed(title="정보", color = 0x00F8FF)
    harong.add_field(name="나이", value="20살", inline=True)
    harong.add_field(name="성별", value="여자", inline=True)
    harong.add_field(name="특징", value="하승오른팔/멤버", inline=False)
    if message.content == "!하롱":
        await message.channel.send(embed=harong)

    #꼬비
    kkobi = discord.Embed(title="정보", color= 0x3F3F3F)
    kkobi.add_field(name="나이", value="19살", inline=True)
    kkobi.add_field(name="성별", value="남자", inline=True)
    kkobi.add_field(name="특징", value="하승크루 담당일찐/멤버", inline=False)
    if message.content == "!꼬비":
        await message.channel.send(embed=kkobi)

    #창현
    changhyeon = discord.Embed(title="정보", color=0xBF61C1)
    changhyeon.add_field(name="나이", value="20살", inline=True)
    changhyeon.add_field(name="성별", value="남자", inline=True)
    changhyeon.add_field(name="특징", value="하승크루 운전기사님?/멤버", inline=False)
    if message.content == "!창현":
        await message.channel.send(embed=changhyeon)

    #바우
    bau = discord.Embed(title="정보", color = 0xC5CE6B)
    bau.set_thumbnail(url="https://cdn.discordapp.com/attachments/762602235346812938/798511222814146600/76a12f457402ece7.png")
    bau.add_field(name="나이", value="21살", inline=True)
    bau.add_field(name="성별", value="남자", inline=True)
    bau.add_field(name="특징", value="메이플을 미친듯이 좋아함/헛소리가 심함/멤버", inline=False)
    if message.content == "!바우":
        await message.channel.send(embed=bau)


    #컨텐츠팀

    #소다
    soda = discord.Embed(title="정보", color =0x27FF44)
    soda.set_thumbnail(url="https://cdn.discordapp.com/attachments/797480155936325635/798499215000993792/248f6447fa746f0d.png")
    soda.add_field(name ="나이", value ="17", inline=True)
    soda.add_field(name ="성별", value="남자", inline=True)
    soda.add_field(name ="특징", value="젤라틴팀 따까리", inline=False)
    if message.content == "!소다":  
        await message.channel.send(embed=soda)

    #머브
    mube = discord.Embed(title="정보", color =0x14B3A0)
    mube.set_thumbnail(url="https://cdn.discordapp.com/attachments/760154235387379812/798497801482141716/483f9f7ba27e31d3.png")
    mube.add_field(name ="나이", value ="18", inline=True)
    mube.add_field(name ="성별", value="남자", inline=True)
    mube.add_field(name ="특징", value="젤라틴팀 따까리", inline=False)
    if message.content == "!머브":
        await message.channel.send(embed=mube)
    
    #용한
    younghan = discord.Embed(title="정보", color =0x954F0D)
    younghan.set_thumbnail(url="")
    younghan.add_field(name ="나이", value ="18", inline=True)
    younghan.add_field(name ="성별", value="남자", inline=True)
    younghan.add_field(name ="특징", value="젤라틴팀 따까리", inline=False)
    if message.content == "!용한":
        await message.channel.send(embed=younghan)

    #무공이
    moogong_E = discord.Embed(title="정보", color =0x331174)
    moogong_E.add_field(name="나이", value="21살", inline=True)
    moogong_E.add_field(name="성별", value="남자", inline=True)
    moogong_E.add_field(name="특징", value="군인", inline=False)
    if message.content == "!무공이":
        await message.channel.send(embed=moogong_E)

    #보라
    bora = discord.Embed(title="정보", color =0x9577D0)
    bora.set_thumbnail(url="")
    bora.add_field(name ="나이", value ="16", inline=True)
    bora.add_field(name ="성별", value="여자", inline=True)
    bora.add_field(name ="특징", value="젤라틴팀 따까리", inline=False)
    if message.content == "!보라":
        await message.channel.send(embed=bora)




    #투표
    if message.content.startswith("!투표"):
        vote = message.content[4:].split("/")
        channel = message.channel
        await channel.send("투표를 시작합니다.")
        for i in range(0, len(vote)):
            lastsend = await channel.send("```" + vote[i] + "```")
            await lastsend.add_reaction('✅')
            await lastsend.add_reaction('❌')




    #선택
    if message.author == app.user:
        return
    
    if message.content.startswith('!골라'):
        message.content = message.content.replace("!골라 ","")
        messagesplit = message.content.split(",")
        msg = random.choice(messagesplit)+'을 골랐습니다.'
        await message.channel.send(msg)






    #금지어
    embed = discord.Embed(title="하승", description="이쁜말 사용합시다.", color=0xFD5E4F)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/797480155936325635/797524157511499797/113BF148512A241E332A37.jpg")
   
    message_content = message.content

    bad = message_content.find("씨발")
    bad2 = message_content.find("야발")
    bad3 = message_content.find("하바승보")
    bad4 = message_content.find("개이쉐")
    bad5 = message_content.find("ㅗ")

    ai = message_content.find("잘자")

    bau = message_content.find("군바")

    dasom = message_content.find("다솜아")

    print(bad)
    if bad >= 0:
        await message.channel.send(embed=embed)
        await message.delete()
    print(bad2)
    if bad2 >= 0:
        await message.channel.send(embed=embed)
        await message.delete()
    print(bad3)
    if bad3 >= 0:
        await message.channel.send(embed=embed)
        await message.delete()
    print(bad4)
    if bad4 >= 0:
        await message.channel.send(embed=embed)
        await message.delete()
    print(bad5)
    if bad5 >= 0:
        await message.channel.send(embed=embed)
        await message.delete()
    print(ai)
    if ai >= 0:
        await message.channel.send("**안녕히주무세요~**")
    print(bau)
    if bau >= 0:
        await message.channel.send("__**^^7바우님 잘가~**__")
    print(dasom)
    if dasom >= 0:
        await message.channel.send("야 다솜! 너 좀 귀엽다")
    await app.process_commands(message)




app.run('Nzk3NTI2NTA1NjA5NDk0NjQx.X_nwcA.krIo4gyXB7OsmBpxUhjCKZSLXGI')