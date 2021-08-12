from urllib.request import Request, urlopen

url="https://www.ptt.cc/bbs/movie/index.html"

# Build a request item, with Request Headers informations
req = Request(url, headers={
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
})

# Get the page source code then decode
web_byte = urlopen(req).read()
webpage = web_byte.decode("utf-8")

# Analyze the code with bs4, then get the information we need
import bs4
root=bs4.BeautifulSoup(webpage, "html.parser")
titles=root.find_all("div", class_="title")

# write the result into titles.txt
with open("titles.txt", "w", encoding="utf-8") as file:
    for title in titles:
        if title != None:
            file.write(title.a.string + "\n")
            print(title.a.string)

