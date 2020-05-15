import feedparser

k_dev_url = "https://groups.google.com/forum/feed/kubernetes-dev/msgs/rss.xml"

def get_latest_post():
    url = k_dev_url + "?num=1"
    parse = feedparser.parse(url)
    entry = parse['entries'][0]
    # print(entry)
    print("Title: ", entry['title'])
    print("Published on: ", entry['published'])
    print("Author: ", entry['author'])
    print("Subject: ", entry['summary'])
    print("Link to discussion: ", entry['links'][0]['href'])

def parse_entry(parse, n):
    entry = parse['entries'][n]
    # print(entry)
    print("Title: ", entry['title'])
    print("Published on: ", entry['published'])
    print("Author: ", entry['author'])
    print("Subject: ", entry['summary'])
    print("Link to discussion: ", entry['links'][0]['href'])

def get_last_n_post(n):
    url = k_dev_url + "?num="+ str(n)
    # print(url)
    parse = feedparser.parse(url)
    for i in range(0, n):
        parse_entry(parse, i)
        print("\n")

# get_latest_post()
get_last_n_post(4)

