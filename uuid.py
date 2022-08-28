import mojang #mojang API
from mojang import MojangAPI #MojangApi

print('Put your Minecraft Username....') #displays

username = str(input(''))

uuid69 = MojangAPI.get_uuid(username)

print(uuid69)