from requests import get as requests_get
from json import dumps
from requests import get
from utils import generate_uuid
import xml.etree.ElementTree as et

steam_openid_url = 'https://steamcommunity.com/openid/login'
steam_profile = "https://steamcommunity.com/profile/"

actived_steam_users = []

class User:
    def __init__(self, steam_id, avatar, nickname):
        self.steam_id = steam_id
        self.avatar = avatar
        self.nickname = nickname
        self.id: str = generate_uuid()

    @staticmethod
    def create_user(steam_id: str) -> str:
        id = f"https://steamcommunity.com/profiles/{steam_id}?xml=1"

        rq = get(id)
        
        myroot = et.fromstring(rq.text)
        avatar = myroot.find("avatarMedium").text
        nickname = myroot.find("realname").text

        user = User(steam_id, avatar, nickname)
        
        actived_steam_users.append(user)
        
        return user.id
    
    @staticmethod
    def check_user(id: str) -> bool:
        for user in actived_steam_users:
            if user.id == id:
                return True
        
        return False
    
    @staticmethod
    def get_user(id: str):
        for user in actived_steam_users:
            if user.id == id:
                return user
        
        return None

