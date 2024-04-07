import requests
import time  # Importar o módulo time

# Defina o URL para o qual a requisição será enviada
url = 'https://ngl.link/api/submit'

# Defina os cabeçalhos da requisição
headers = {
    'Host': 'ngl.link',
    'Cookie': '< All Cookies here >' // YOU MAY EDIT THIS PART
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
    'Referer': 'https://ngl.link/< USERNAME >', // YOU MAY EDIT THIS PART
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Priority': 'u=1, i'
}

data = {
    'username': '< User to flood >', // YOU MAY EDIT THIS PART
    'question': 'L3ster floodou isso aqui :)',
    'deviceId': '<Device Id, check your request>', // YOU MAY EDIT THIS PART
    'gameSlug': '',
    'referrer': ''
}

for i in range(1000):
    response = requests.post(url, headers=headers, data=data)
    print(f'Request {i+1}: Status Code {response.status_code}')

    time.sleep(10)
