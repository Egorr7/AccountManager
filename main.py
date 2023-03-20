import pandas as pd
from config import Steam
from core import AccountManager

user_pool = pd.read_excel(Steam.accounts_path)

AccountManager.check_cfg()
AccountManager.login(user_pool)