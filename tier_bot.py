import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import time
import random
import requests
from bs4 import BeautifulSoup
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from urllib import parse
import os


bot_command = '`'
token = os.environ['token']
thatId = "282534461101572097"
myId = "490745605069602816"
DEVELOPMENTAPIKEY = os.environ['riotapi']
riotHeaders = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": DEVELOPMENTAPIKEY,
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
}



"""
라이엇 API키
RGAPI-1d8d0bcb-19e3-4ee0-8579-bdc41b002ec1

"""



client = discord.Client()
bot = commands.Bot(command_prefix = bot_command)



@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)


@bot.command(pass_context = True)
async def 명령어(ctx):
    await ctx.send("""명령어 사용법 : """ + bot_command + """명령어
명령어 목록

일반 명령어
안녕      : 인사
죽어      : 10초동안 명령어 무시. 10초 뒤에 그동안 입력된 명령어 몰아서 실행.
say       : say 뒤에 한 말을 따라함


음악 명령어
join      : 명령어 사용자가 현재 속한 음성채널로 들어감
leave     : 음성채널에서 나옴


씹덕 명령어
catgirl   : 고양이여자 사진
neko      : catgirl과 동일
hug       : 껴안는 사진
""")

@bot.command(pass_context = True)
async def command(ctx):
    await ctx.send("""명령어 사용법 : """ + bot_command + """명령어
명령어 목록

일반 명령어
안녕      : 인사
죽어      : 10초동안 명령어 무시. 10초 뒤에 그동안 입력된 명령어 몰아서 실행.
say       : say 뒤에 한 말을 따라함


음악 명령어
join      : 명령어 사용자가 현재 속한 음성채널로 들어감
leave     : 음성채널에서 나옴


씹덕 명령어
catgirl   : 고양이여자 사진
neko      : catgirl과 동일
네코      : catgirl과 동일
hug       : 껴안는 사진
""")



@bot.command(pass_context=True)
async def on(ctx):
    if(str(ctx.author.id) != myId):
        await ctx.send("안켜질거야")
        return 0
    print("켜진다")
    try:
        await ctx.channel.purge(limit = 1)
    except:
        await ctx.send("메시지 삭제 권한이 없습니다.")
    x = input()
    while(x != "끝"):
        await ctx.send(x)
        x = input()
    


@bot.command(pass_context=True)
async def off(ctx):
    if(str(ctx.author.id) == thatId):
        await ctx.send("너나 꺼져")
        return 0
    if(str(ctx.author.id) != myId):
        await ctx.send("안꺼질거야")
        return 0
    await ctx.send("잘자! 난 끌게!")
    await bot.change_presence(status=discord.Status.offline)
    exit()



@bot.command(pass_context=True)
async def 안녕(ctx):
    message = ctx.message
    print("id : " + str(message.author.id) + "name : " + message.author.name)
    myembed = discord.Embed()
    myurl='https://mblogthumb-phinf.pstatic.net/20140916_106/beyi_1410824552717nHRqp_PNG/peanuts-movie-2015.png?type=w2'
    myembed.set_image(url = myurl)
    await ctx.send("안녕, <@!" + str(message.author.id) + ">", embed = myembed)



@bot.command(pass_context=True)
async def 점프(ctx):
    message = ctx.message
    print("id : " + str(message.author.id) + "name : " + message.author.name)
    myembed = discord.Embed()
    myurl="https://cdn.discordapp.com/attachments/737557822727782473/738449176811274330/image0.jpg"
    myembed.set_image(url = myurl)
    await ctx.send(embed = myembed)


@bot.command(pass_context=True)
async def 멍멍(ctx):
    message = ctx.message
    print("id : " + str(message.author.id) + "name : " + message.author.name)
    await ctx.send("""┈┈╱▏┈┈┈┈┈╱▔▔▔▔╲┈ 
┈┈▏▏┈┈┈┈┈▏╲▕▋▕▋▏
┈┈╲╲┈┈┈┈┈▏┈▏┈▔▔▔▆ ------- 멍멍!
┈┈┈╲▔▔▔▔▔╲╱┈╰┳┳┳╯ 
╱╲╱╲▏┈┈┈┈┈┈▕▔╰━╯ 
▔╲╲╱╱▔╱▔▔╲╲╲╲┈┈┈ 
┈┈╲╱╲╱┈┈┈┈╲╲▂╲▂┈ 
┈┈┈┈┈┈┈┈┈┈┈╲╱╲╱┈""")


@bot.command(pass_context=True)
async def say(ctx):
    try:
        await ctx.channel.purge(limit = 1)
    except:
        await ctx.send("메시지 삭제 권한이 없습니다.")
    await ctx.send(ctx.message.content[len(bot_command) + 4:])
    print(ctx.message.content)


def getTier(jsonlst):
    if(not len(jsonlst)):
        raise IndexError
    for i in jsonlst:
        if(i["queueType"] == "RANKED_SOLO_5x5"):
            return i

def searchsoloRank(summonerName):
    encodingSummonerName = parse.quote(summonerName)
    APIURL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + encodingSummonerName
    res = requests.get(APIURL, headers = riotHeaders)
    data = res.json()
    try:
        summonerId = data["id"]
    except:
        return "찾을 수 없는 계정입니다.\n"
    leagueAPIURL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerId
    result = requests.get(leagueAPIURL, headers = riotHeaders)
    try:
        findata = getTier(result.json())
        printingmsg = (summonerName + "의 현재 솔로랭크 티어 : " + findata["tier"] + " " + findata["rank"] + "  " + str(findata["leaguePoints"]) + "LP\n")
        return printingmsg
    except:
        return "배치를 완료하지 않는 등의 이유로 인해 현재 랭크를 불러올 수 없습니다.\n"

def searchMatchList(summonerName, gameNum = 10):
    encodingSummonerName = parse.quote(summonerName)
    APIURL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + encodingSummonerName
    res = requests.get(APIURL, headers = riotHeaders)
    data = res.json()
    try:
        accountId = data["accountId"]
    except:
        return "찾을 수 없는 계정입니다.\n"
    matchListURL = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId
    matchResult = requests.get(matchListURL, headers = riotHeaders)
    matchdata = matchResult.json()
    n = 0
    count = 0
    printingmsg = ""
    currentTime = int(time.time() * 1000)
    while(count < gameNum):
        try:
            if(matchdata['matches'][n]['queue'] == 420):
                count += 1
        except IndexError:
            break
        nowMatch = matchdata['matches'][n]
        gameTime = nowMatch['timestamp']
        matchId = nowMatch['gameId']
        gameURL = "https://kr.api.riotgames.com/lol/match/v4/matches/" + str(matchId)
        gamedata = requests.get(gameURL, headers = riotHeaders).json()
        players = gamedata["participantIdentities"]

        teamcode = 0
        for i in players:
            if(i["player"]["accountId"] == accountId):
                if(i["participantId"] <= 5):
                    teamcode = 100
                else:
                    teamcode = 200

        isSame = None
        if(gamedata["teams"][0]["teamId"] == teamcode):
            if(gamedata["teams"][0]["win"] == "Fail"):
                printingmsg += "패, "
            else:
                printingmsg += "승, "
        else:
            if(gamedata["teams"][0]["win"] == "Fail"):
                printingmsg += "승, "
            else:
                printingmsg += "패, "
        timeGap = (currentTime - gameTime) // 1000 - 30 * 60
        print(timeGap)
        if (timeGap < 60): # 초단위
            printingmsg += "방금 전"
        elif (timeGap // 60 <= 60): # 분단위
            printingmsg += str(timeGap // 60) + "분 전"
        elif (timeGap // 60 // 60 <= 24): # 시간단위
            printingmsg += str(round(timeGap // 60 / 60)) + "시간 전"
        else:
            printingmsg += str(timeGap // 60 // 60 // 24) + "일 전"
        printingmsg += "\n"
        n += 1
    return printingmsg


@bot.command(pass_context=True)
async def 랭크(ctx):
    summonerNamelst = ctx.message.content[len(bot_command) + 3:].split(",")
    printingmsg = ""
    for name in summonerNamelst:
        # await ctx.send(name)
        printingmsg += searchsoloRank(name.strip())
    

    printingmsg = "=" * 50 + "\n" + printingmsg + "=" * 50
    await ctx.send(printingmsg)
    print(ctx.message.content)
    return 0


@bot.command(pass_context=True)
async def 전적(ctx):
    summonerName = ctx.message.content[len(bot_command) + 3:]
    printingmsg = searchMatchList(summonerName)
    await ctx.send("최근 10게임의 솔로랭크 전적을 보여줍니다")
    await ctx.send(printingmsg)
    print(ctx.message.content)
    return 0



@bot.command(pass_context=True)
async def 롤토(ctx):
    summonerName = ctx.message.content[len(bot_command) + 3:]
    encodingSummonerName = parse.quote(summonerName)
    APIURL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + encodingSummonerName
    res = requests.get(APIURL, headers = riotHeaders)
    data = res.json()
    try:
        summonerId = data["id"]
    except:
        await ctx.send("찾을 수 없는 계정입니다.")
        return 1
    leagueAPIURL = "https://kr.api.riotgames.com/tft/league/v1/entries/by-summoner/" + summonerId
    result = requests.get(leagueAPIURL, headers = riotHeaders)
    try:
        findata = result.json()[0]
        printingmsg = (summonerName + "의 현재 롤토체스 티어 : " + findata["tier"] + " " + findata["rank"] + "  " + str(findata["leaguePoints"]) + "LP")
    except:
        await ctx.send("배치를 완료하지 않는 등의 이유로 인해 현재 랭크를 불러올 수 없습니다.")
        return 2

    printingmsg = "=" * 50 + "\n" + printingmsg + "\n" + "=" * 50
    await ctx.send(printingmsg)
    print(ctx.message.content)
    return 0



@bot.command(pass_context=True)
async def 엄준식(ctx):
    message = ctx.message
    channel = message.channel    
    myembed = discord.Embed()
    myurl='https://ext.fmkorea.com/files/attach/new/20191021/486616/2514059/2302590490/284867d0eef326a324e36df5cf79e69f.jpg'
    myembed.set_image(url = myurl)
    await ctx.send("엄\n준\n식\n", embed = myembed)


@bot.command(pass_context=True)
async def 게임(ctx):
   gamename=ctx.message.content[6:]
   await ctx.send(gamename)
   await bot.change_presence(activity=discord.Game(name=gamename))


@bot.command(pass_context=True)
async def 죽어(ctx):
    await ctx.send("너나 뒤지세요")
    return 0
    await ctx.send("10초동안 말을 듣지 못해...")
    timer= 10
    while(timer > 0):
        timer -= 1
        time.sleep(1)


@bot.command(pass_context=True)
async def catgirl(ctx):
    url = 'https://nekos.life/api/neko'
    req = requests.get(url)
    html = req.text
    catlist = html[9:-3]
    myembed = discord.Embed()
    myembed.set_image(url = catlist)
    await ctx.send(embed = myembed)


@bot.command(pass_context=True)
async def neko(ctx):
    url = 'https://nekos.life/api/neko'
    req = requests.get(url)
    html = req.text
    catlist = html[9:-3]
    myembed = discord.Embed()
    myembed.set_image(url = catlist)
    await ctx.send(embed = myembed)


@bot.command(pass_context=True)
async def 네코(ctx):
    url = 'https://nekos.life/api/neko'
    req = requests.get(url)
    html = req.text
    catlist = html[9:-3]
    myembed = discord.Embed()
    myembed.set_image(url = catlist)
    await ctx.send(embed = myembed)



@bot.command(pass_context=True)
async def hug(ctx):
    url = 'https://imgur.com/a/jHJOc'
    response = requests.get(url)
    result = response.text
    html = BeautifulSoup(result, 'html.parser')
    lists = html.select('.post-image>meta')
    x = random.randint(0, len(lists) - 1)
    if(lists[x]['content'][0] != 'h'):
        huglist = "https:" + lists[x]['content']
    else:
        huglist = list[x]['content']
    myembed = discord.Embed()
    myembed.set_image(url = huglist)
    await ctx.send(embed = myembed)


@bot.command(pass_context=True)
async def 청소(ctx):
    #await ctx.send("지랄 ㅋㅋ")
    #return
    print(ctx.message.content)
    print(ctx.message.content.split()[2])
    try:
        print(ctx.message.content.split()[2])
        msg = float(ctx.message.content.split()[2])
        print(msg)
        times = int(msg)
        print(times)
        if(msg - times >= 0.5):
            times+=1
        print(times)
    except ValueError:
        await ctx.send("스누피 청소 숫자 형태로 입력해주세요.")
    try:
        await ctx.channel.purge(limit = times)
    except:
        await ctx.send("메시지 삭제 권한이 없습니다.")




@bot.command(pass_context=True)
async def join(ctx):
    connected = ctx.author.voice
    print(connected)
    print(connected.channel)
    if connected:
        try:
            await connected.channel.connect()
        except:
            await leave(ctx)
            await connected.channel.connect()
    else:
        await ctx.send("현재 접속한 보이스 채널이 발견되지 않았습니다!")
        return


@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect(force = True)


@bot.command(pass_context=True)
async def 이거루(ctx):
    urllists = ['https://cdn.discordapp.com/attachments/737728958325588050/739888490308698142/unknown.png',
    'https://cdn.discordapp.com/attachments/737728958325588050/740240993017659472/unknown.png',
    'https://cdn.discordapp.com/attachments/737728958325588050/740548404781776896/unknown.png',
    'https://cdn.discordapp.com/attachments/737728958325588050/740893902369718343/unknown.png',
    'https://cdn.discordapp.com/attachments/737728958325588050/740894193702011010/unknown.png',
    'https://cdn.discordapp.com/attachments/725597655866277942/742634275030958140/Screenshot_20200811-154321_Discord.jpg',
    'https://cdn.discordapp.com/attachments/737728958325588050/743719084448940052/unknown.png',
    'https://cdn.discordapp.com/attachments/737728958325588050/743719218784108574/unknown.png',
    'https://cdn.discordapp.com/attachments/737728958325588050/743719293421879366/unknown.png',
    'https://cdn.discordapp.com/attachments/737728958325588050/743719387349123154/unknown.png',
    'https://cdn.discordapp.com/attachments/737728958325588050/743719988317126746/unknown.png',
    'https://cdn.discordapp.com/attachments/737728958325588050/743720067484745759/unknown.png',
    'https://cdn.discordapp.com/attachments/737728958325588050/744164815924101120/unknown.png',
    'https://cdn.discordapp.com/attachments/737728958325588050/751306280437809182/unknown.png'
    ]
    num = random.randint(0, len(urllists) - 1)
    selected = urllists[num]
    myembed = discord.Embed()
    myembed.set_image(url = selected)
    await ctx.send(embed = myembed)


@bot.command(pass_context=True)
async def 응애(ctx):
    await ctx.send("응애")


@bot.command(pass_context=True)
async def 추가(ctx):
    pass
    global driver
    default_url='https://www.youtube.com/results?search_query='
    keyword = ctx.message.content[len(bot_command) + 3:]
    driver.get(default_url + keyword)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('#video-title')

    result=""
    while(1):
        try:
            result_link = 'https://www.youtube.com/'+str(links[0]['href'])
            result_title = str(links[0]['title'])
            break
        except:
            pass
    current_list['result_title'] = result_link
    await ctx.send(result_link)
    player = await voice_client.create_ytdl_player(result_link)
    player.start()
    await ctx.send(result_link)


@bot.command(pass_context=True)
async def 재생(ctx):
    pass


#해야할 것 : 큐 저장하기 구현
#해야할 것 : 음악 실행하기 구현


bot.run(token)