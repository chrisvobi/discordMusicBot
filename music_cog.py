import discord
from discord.ext import commands
from yt_dlp import YoutubeDL

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_playing = False
        self.is_paused = False
        self.queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        self.vc = None

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: info = ydl.extract_info(f"ytsearch:{item}", download=False)['entries'][0]
            except: return False
        return {'source': info['url'], 'title': info['title']}
    
    def play_next(self):
        if len(self.queue) > 0:
            self.is_playing = True
            m_url = self.queue[0][0]['source']
            self.queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    async def play_music(self, ctx):
        if len(self.queue) > 0:
            self.is_playing = True
            m_url = self.queue[0][0]['source']
            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.queue[0][1].connect()
                if self.vc == None:
                    await ctx.send("Failed to join the channel.")
                    return
            else:
                self.vc = await self.vc.move_to(self.queue[0][1])
            self.queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.command(name="play", aliases=["p", "playing"], help="Plays a selected song from youtube")
    async def p(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Connect to a voice channel!")
        elif self.is_paused:
            self.vc.resume()
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Could not download the song. Incorrect format try another keyword.")
            else:
                await ctx.send("Song added to the queue")
                self.queue.append([song, voice_channel])
                if self.is_playing == False:
                    await self.play_music(ctx)

    @commands.command(name="pause", help="Pauses the current song")
    async def pause(self, ctx):
        if self.is_playing:
            self.is_playing = False
            self.vc.pause()
            self.is_paused = True
            await ctx.send("Paused ⏸️")
    
    @commands.command(name="resume", help="Resumes the current song")
    async def resume(self, ctx):
        if self.is_paused:
            self.vc.resume()
            self.is_playing = True
            self.is_paused = False
            await ctx.send("Resumed ▶️")

    @commands.command(name="skip", aliases=["s"], help="Skips the current song")
    async def skip(self, ctx):
        if self.vc != None and self.is_playing:
            self.vc.stop()
            await self.play_music(ctx)

    @commands.command(name="queue", aliases=["q"], help="Displays the current songs in queue")
    async def queue_info(self, ctx):
        retval = ""
        for i in range(len(self.queue)):
            retval += f'{i+1}: {self.queue[i][0]["title"]}\n'
        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("No songs in queue")

    @commands.command(name="clear", help="Clears the queue")
    async def clear_queue(self, ctx):
        if self.vc != None and self.is_playing:
            self.queue = []
            self.vc.stop()
            self.is_playing = False
            await ctx.send("Queue cleared")

    @commands.command(name="leave", aliases=["disconnect", "l"], help="Leaves the voice channel")
    async def leave(self, ctx):
        if self.vc != None:
            await self.vc.disconnect()
            self.queue = []
            self.is_playing = False
            self.is_paused = False
            await ctx.send("Disconnected")

async  def setup(bot):
    await bot.add_cog(music_cog(bot))