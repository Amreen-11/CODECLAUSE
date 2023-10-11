import pyshorteners
link = input("Enter the link: ")
shortener = pyshorteners.Shortener()
shorturl = shortener.tinyurl.short(link)
print(shorturl)