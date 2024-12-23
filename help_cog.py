from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
COMMANDS:
!help - displays all available commands
!play or !p - plays a song from youtube   
!queue or !q - displays the current queue
!skip or !s - skips the current song
!clear - clears the queue
!leave or !disconnect - leaves the voice channel
!pause - pauses the current song
!resume - resumes the current song
```
"""
    
    @commands.command(name="help", help="Displays all available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

async def setup(bot):
    await bot.add_cog(help_cog(bot))