import requests, time, platform
from bs4 import BeautifulSoup

# Get the os info
operating_system = platform.system()
os_release = platform.release()
os_version = platform.version()
architecture = platform.machine()
processor = platform.processor()

# Set  user agents and responses 
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
    "DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)",
    "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
    "ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)",
    "A humble bot",
    f"Wget/1.21.1 ({operating_system}-{os_release})", #this replicates a wget call
    f"curl/7.81.0 ({architecture}-{operating_system.lower()}{os_release})", #this replicates a curl call
    "Mozilla/5.0 (Definitely Not a Bot)",
    "Python-requests/2.26.0",
    "AutomatedTool/1.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0; Gecko/20100101; Firefox/93.0; MyCustomData; MoreData; EvenMoreData)",
    "Totally Legitimate Browser/1.0"
]

# Try different urls to see how different websites behave.
#url = "https://www.reddit.com/r/bookshelf/"
#url = "https://www.quora.com/Why-do-websites-ask-us-to-fill-a-CAPTCHA"
url = "https://twitter.com/elonmusk"



# Make a call for each user agent
for i in user_agents:
    headers = {
        "User-Agent": i
    }


    # Send a GET request to the bookshelf subreddit
    r = requests.get(url, headers=headers, timeout=5)

    print (f"\nUser-Agent: {i}")

    # Print error message
    if r.status_code != 200:
        print (f"Request rejected {r.status_code}")
    
    else:
        print (f"Response status: {r.status_code}")

    # Get the first 10 lines of text.
    soup = BeautifulSoup(r.content, "html.parser")
    if soup.find('body'):
        body_content = soup.find('body').get_text(separator='\n')
        lines = body_content.split('\n')
        lines = [line for line in lines if line.strip()]

        for line in lines[:10]:
            print(line)


    else:
        print (r.content)
    print()
    # Wait 3 seconds between requests
    time.sleep(3)
