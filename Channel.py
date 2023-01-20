from pytube import Channel ,YouTube 

print('start')
c = Channel(
    # enter Channel url here
)
print(f'Downloading videos by: {c.channel_name}')


num = 0
for url in c.video_urls[:116]:
    num = num + 1 

    y = YouTube(url)
    file_location = c.channel_name + '/' 

    try:
        y.streams.filter(progressive=True,mime_type="video/mp4",res="360p").first().download(file_location , filename_prefix = f"{num:03d}" + ' - ')
    except:
        try:
            y.streams.filter(progressive=True,mime_type="video/mp4",res="720p").first().download(file_location , filename_prefix = f"{num:03d}" + ' - ')
        except:
            try:
                y.streams.filter(progressive=True ,mime_type="video/mp4").first().download(file_location , filename_prefix = f"{num:03d}" + ' - ')
            except:
                try:
                    y.streams.filter(progressive=True).first().download(file_location , filename_prefix = f"{num:03d}" + ' - ')
                except:
                    print(url)
    # video.filter(progressive=True ,res="360p").first()

print("done")