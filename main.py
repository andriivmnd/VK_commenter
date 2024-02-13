import vk_api
import random
import time

MESSAGES = []

def Obfuscate(msg):
    if random.getrandbits(1)):
        msg = msg.replace('о', 'o')
    if random.getrandbits(1)):
        msg = msg.replace('е', 'e')
    
    return msg

def GetMessage():
    return Obfuscate(random.choice(MESSAGES))

def LinkToID(link):
    return link.split("wall")[-1].split('_')

def GetToken(login, password):
    vk = vk_api.VkApi(login, password)
    vk.auth()
    time.sleep(3)
    vk = vk.get_api()
    
    user = vk.users.get()
    
    import json
    with open('vk_config.v2.json', 'r') as data_file:
        data = json.load(data_file)

    for xxx in data[login]['token'].keys():
        for yyy in data[login]['token'][xxx].keys():
            accessToken = data[login]['token'][xxx][yyy]['access_token']
    
    return accessToken

def SolveCaptcha(c):
    print("[!] Captcha needed:", c.get_url())
    key = input("[>] Please enter the code: ")
    return c.try_again(key)

def main():
    ...

if __name__ == "__main__": main()
