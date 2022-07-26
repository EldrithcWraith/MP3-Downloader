import youtube_dl

vurl = input("Enter a link:")

vinfo = youtube_dl.YoutubeDL().extract_info(
url = vurl,download=False)

filen = f"{vinfo['title']}.mp3"

settings={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl':filen
}

with youtube_dl.YoutubeDL(settings) as ydl:
    ydl.download([vinfo['webpage_url']])
print("Download Success. Downloaded to the directory of this file.")