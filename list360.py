from pytube import YouTube, Playlist

print('start')

url_list = [
 #   enter your urls here

]


for i in url_list:

    p = Playlist(i)
    print('start', p.title, '  ', len(p.video_urls))
    num = 0
    # file_location = p.title + '/'
    for url in p.video_urls:
        num = num + 1
        # if num < 90:
        #      continue
        y = YouTube(url)
        file_location = p.title + '/'
        # print(y.title)
        # print(y.streams.filter(progressive=True,mime_type="video/mp4",res="720p"))
        # for stream in y.streams:
        # .filter(progressive=True ,res="720"):
        # print (stream)
        try:
            y.streams.filter(progressive=True, mime_type="video/mp4", res="320p").first(
            ).download(file_location, filename_prefix=f"{num:03d}" + ' - ')
        except:
            try:
                y.streams.filter(progressive=True, mime_type="video/mp4", res="720p").first(
                ).download(file_location, filename_prefix=f"{num:03d}" + ' - ')
            except:
                try:
                    y.streams.filter(progressive=True, mime_type="video/mp4").first().download(
                        file_location, filename_prefix=f"{num:03d}" + ' - ')
                except:
                    try:
                        y.streams.filter(progressive=True, res="320p").first().download(
                            file_location, filename_prefix=f"{num:03d}" + ' - ')
                    except:
                        print(url)
        # video.filter(progressive=True ,res="360p").first()

print("done")
