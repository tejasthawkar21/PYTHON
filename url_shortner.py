import pyshorteners

def url_shortner(url):
    shortener=pyshorteners.Shortener()
    shortened_url=shortener.tinyurl.short(url)
    return shortened_url

def main():
    original_url=input("enter the url: ")
    short_url=url_shortner(original_url)
    print(f'shortened url : {short_url}')
    
if __name__=='__main__':
    main()