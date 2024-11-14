import requests
from requests import Response,RequestException
from requests.structures import CaseInsensitiveDict

def check_status(url):
    try:
        response:Response=requests.get(url)
        status_code=response.status_code
        headers:CaseInsensitiveDict[str] = response.headers
        content_type:str = headers.get('Content-type','Unknown')
        servers:str= headers.get('Server','Unknown')
        response_time:float = response.elapsed.total_seconds()
        
        print(f'URL : {url}')
        print(f'status_code : {status_code}')
        print(f'Content type : {content_type}')
        print(f'Server : {servers}')
        print(f'Response_Time : {response_time}')

    except RequestException as e:
        print(f'ERROR:{e}')

def main():
    url_to_check:str = 'https://www.apple.com'
    check_status(url_to_check)
    
if __name__=='__main__':
    main()