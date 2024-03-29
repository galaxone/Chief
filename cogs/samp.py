import discord
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import context
from samp_client.client import SampClient

class Samp(commands.Cog, name='Samp'):

    def __init__(self,bot):
        self.bot = bot


    @commands.command() #SERVER INFO   --- $ip [ip] [port] 
    async def ip(self,ctx,ADD,NUM):
        with SampClient(address=ADD, port=NUM) as client:
            info = client.get_server_info()
            rulevalue = [rule.value for rule in client.get_server_rules()]        
            await ctx.send(f'```Server: {info.hostname}\nIP: {ADD}:{NUM}\nPlayers: {info.players}/{info.max_players}\nGame Mode: {info.gamemode}\nLanguage: {info.language}\nCAC Version: {rulevalue[0]}\nLag Comp: {rulevalue[1]}\nMap: {rulevalue[2]}\nVersion: {rulevalue[3]}\nWeather: {rulevalue[4]}\nWeburl: {rulevalue[5]}\nWorld Time: {rulevalue[6]}```')

    @ip.error
    async def ip_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: $ip [ip] [port]\n```For Ex:- $ip rp.valrisegaming.com 7777```')




    @commands.command() #SERVER INFO   ---   $players [ip] [port]
    async def players(self,ctx,ADD,NUM):
        with SampClient(address=ADD, port=NUM) as client:
            info = client.get_server_info()
            players = [client.name for client in client.get_server_clients_detailed()]
            score = [client.score for client in client.get_server_clients_detailed()]
            playerping = [client.ping for client in client.get_server_clients_detailed()]
            res2 = [players[i] + " - " + str(score[i]) + " - " + str(playerping[i]) for i in range(len(players))]
            s = '\n'
            s = s.join(res2)
            await ctx.send(f'```Server: {info.hostname}\nPlayers: {info.players}/{info.max_players}\nIP: {ADD}\nGame Mode: {info.gamemode}\nLanguage: {info.language}```')
            await ctx.send(f'```--Player Name-- | --Score-- | --Ping--\n{s}```\n**Total Online: {info.players}**')

    @players.error
    async def players_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: $players [ip] [port]\n```For Ex:- $players rp.valrisegaming.com 7777```')
        





def setup(bot):
    bot.add_cog(Samp(bot))
    print("Samp cog is loaded!")
    