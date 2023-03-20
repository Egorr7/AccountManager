import shutil
import pandas
import subprocess
import os
import time

from config import Settings, Steam, Config

class Resources:
    @staticmethod
    def copy_cfg_to_directory():
        try:
            shutil.copy2('resources/autoexec.cfg', Config.csgo_cfg_folder_path)
            shutil.copy2('resources/connect.cfg', Config.csgo_cfg_folder_path)
            print('configs installed!')
        except Exception as ex:
            print(ex)

    @staticmethod
    def check_cfg():
        if os.path.isfile(f'{Config.csgo_cfg_folder_path}{Config.csgo_cfg_filename}') and os.path.isfile(f'{Config.csgo_cfg_folder_path}connect.cfg'):
            print('autoexec.cfg exists.')
        else:
            print('autoexec.cfg does not exist.')
            Resources.copy_cfg_to_directory()

class SteamAuth:
    @staticmethod
    def run(accounts: pandas.DataFrame, info: bool):
        print(f'Current server: {Settings.server_ip}')
        for user in accounts.values:
            login, password = user[0], user[1]
            window_position = [0, 0]  # Not working
            args = f'{Steam.steam_path} -login {login} {password} -no-browser -applaunch {Settings.app_id} -low -nohltv -nosound -novid -window -w 640 -h 480 +exec autoexec.cfg -x {window_position[0]} -y {window_position[1]} +connect {Settings.server_ip}'
            if info: print(args)
            subprocess.Popen(args, shell=True)
            time.sleep(Settings.sleep_time)


class AccountManager(Steam, Resources):
    @staticmethod
    def check_cfg():
        Resources.check_cfg()

    @staticmethod
    def login(accounts: pandas.DataFrame, info=False):
        SteamAuth.run(accounts, info)