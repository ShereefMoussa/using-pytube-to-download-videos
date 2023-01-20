from pytube import YouTube, Playlist

print('start aud')
url_list = [
 #   enter your urls here

]


for i in url_list:
    p = Playlist(i)
    num = 0
    for url in p.video_urls:
        num = num + 1 
        y = YouTube(url)
        file_location = p.title + '/' 
        try:
            #for s in y.streams.filter(mime_type="audio/mp4" ,abr="128kbps"):
            #    print(s)

            y.streams.filter(mime_type="audio/mp4").first().download(file_location , filename_prefix = f"{num:03d}" + ' - ')
        except:
            print(url)
