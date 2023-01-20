from pytube import Search, YouTube
import unicodedata
import re


s = Search('scalping strategy')
print(len(s.results))
s.get_next_results()
print(len(s.results))
s.get_next_results()
print(len(s.results))



for res in s.results:
    
    try:
        res.streams.filter(progressive=True ,res="720p").first().download()
    except:
        try:
            res.streams.filter(progressive=True ,res="360p").first().download()
        except:
            try:
                res.streams.filter(progressive=True).first().download()
            except:
                print(res.streams)
                