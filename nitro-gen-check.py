import requests, random, string
from colorama import init, Fore, Style
#----------------------
def g(n):
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
        return ''.join(randlst)
init()
#------------------
print(
    """
    
█▄░█ █ ▀█▀ █▀█ █▀█ ▄▄ █▀▀ █░█ █▀▀ █▀▀ █▄▀ █▀▀ █▀█
█░▀█ █ ░█░ █▀▄ █▄█ ░░ █▄▄ █▀█ ██▄ █▄▄ █░█ ██▄ █▀▄
Generator .kap210\n
    """
)

header = {
    'User-Agent': 'Mozilla/5.0 Chrome/109.0.0.0 Safari/537.36',
    'content-type': 'application/json'
}

while True:
    code = g(16)
    r = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{code}?country_code=JP&with_application=false&with_subscription_plan=true")
    if r.status_code == 202:
        print(Fore.CYAN +  f"有効: https://discord.com/gifts/{format(code)}")
    else:
        print(Fore.RED + f"無効: https://discord.com/gifts/{format(code)}")
