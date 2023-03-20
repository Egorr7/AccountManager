from configparser import ConfigParser

parser = ConfigParser()
parser.read(r'config.ini')

def set_value(section, key, value):
    parser.set(section, key, value)
    with open('config.ini', 'w') as configfile:
        parser.write(configfile)


class Steam:
    section = 'steam'
    steam_path = parser.get(section, 'steam_path')
    accounts_path = parser.get(section, 'accounts_path')

class Config:
    section = 'cfg'
    csgo_cfg_filename = parser.get(section, 'csgo_cfg_filename')
    csgo_cfg_folder_path = parser.get(section, 'csgo_cfg_folder_path')

class Settings:
    section = 'settings'
    resolution = parser.get(section, 'resolution')
    server_ip = parser.get(section, 'server_ip')
    app_id = parser.get(section, 'app_id')
    game_resolution = parser.get(section, 'game_resolution')
    sleep_time = parser.getfloat(section, 'sleep_time')

