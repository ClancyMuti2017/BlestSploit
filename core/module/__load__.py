import os, sys, subprocess, colorama, random, time, json
from colorama import *
import jsbeautifier
init()
database = '/usr/share/blest-framework'
core = '/usr/share/blest-framework/src/data'
modules = core+'/modules'
banners = core+'/core/base/banners/banner.py'
modules_json = core+'/core/module/data/modules.json'
modules_type = '''
'''
loaded_modules = {}
module_options = {}
ignore = ['.txt', '.log', '.yml', '.yaml', '.ini', '.md', '.json', '.bin']
add = ['.py', '.pyw', '.c', '.cpp', '.so', '.pl', '.rb', '.sh']
module_type = sys.argv[1].capitalize()
usb_device = "false"
if module_type == "Usb":
    usb_device = sys.argv[2]

module_run = sys.argv[3]
module_cmd = sys.argv[4]
commands = '''
Global Komutlar
======================

    Komutlar                        Tanım
    --------                        --------
    help                            Mevcut komutları göster, yardım
    clear                           Terminal pencere ekranını temizleyin
    exit, back                      Blestsploit'ten çıkın, modül kullanımından geri dönün

Modül komutları
======================

    Komutlar                        Tanım
    --------                        --------
    set <option> <value>            Modülde belirtilen değere belirtilen seçeneği ayarlayın
    run, exploit                    Kullanılan modülü yükleyin, Başlatın
    show -o                         Yüklü modülün seçeneklerini göster
    info <option>                   Belirtilen seçenek hakkında bilgileri gösterin
'''
check = module_cmd.split("/")
module_author = ""
module_version = ""
if check[0] == module_type.lower():
    ng = ""
    num = 0
    n = False
    leng = len(check)
    for i in check:
        if num >= leng:
            break
        if n == False:
            if i == module_type.lower():
                n = True
                continue
        num += 1
        if leng - num == 1:
            ng += i
        else:
            ng += i+'/'
    module_cmd = ng

try:
    if os.path.exists(modules_json):
        with open(modules_json, "r") as t:
            modules_type = t.read()
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Hata, modüller veri dosyası yok!')
        sys.exit()
except:
    pass
module_prefix = ""
module_num = ""
modules_data = json.loads(modules_type)
# print(Fore.BLUE+'[i]'+Fore.RESET+f' Modül "{module_cmd}" Seçenekleri Yükleniyor...')
op = []
for i in modules_data:
    if modules_data[i]['name'] in module_cmd:
        module_prefix = modules_data[i]['prefix']
        for c in modules_data[i]:
            op.append(c)
        if module_type.lower() == "payload":
            if "options" in op:
                for option in modules_data[i]['options']:
                    module_options[option] = modules_data[i]['options'][option]
        else:
            for option in modules_data[i]['options']:
                module_options[option] = modules_data[i]['options'][option]
        # module_author = modules_data[i]['author']
        module_version = modules_data[i]['version']
        module_num = i
        break
# print(Fore.YELLOW+'[+]'+Fore.RESET+f' Başarıyla modül "{module_cmd}" yüklendi.')



def run():
    def ex():
        global module_prefix
        num = 0
        md_run = "python3"
        module_prefix_run = ""
        module_prefix_run = module_prefix
        for repl in module_options.keys():
            num += 1
            if "$"+str(num) in module_prefix_run:
                module_prefix_run = module_prefix_run.replace(f"${str(num)}", module_options[repl][1])
        tp = []
        lg = ""
        for i in modules_data[module_num]:
            tp.append(i)
        data = ""
        if "run" in tp:
            md_run = modules_data[module_num]['run']
        if module_type.lower() == "payload":
            name = modules_data[module_num]['name']
            if module_options == {} or module_options == {'\n'}:
                print(Fore.BLUE+'[i]'+Fore.RESET+' "/root/.btf" adresine Payload yazma...')
                time.sleep(2)
                if "type" in tp:
                    lg = modules_data[module_num]['type']
                try:
                    with open(f"/root/.btf/{name}{lg}", "w") as ft:
                        with open(module_run+lg, "r") as t:
                            data = t.read()
                        ft.write(data)
                except:
                    pass
                print(Fore.BLUE+'[i]'+Fore.RESET+f' Payload dosya olarak yazıltı: "/root/.btf/{name}{lg}", Lütfen Payload\'ı en sevdiğiniz editörle açın ve düzenleyin.')
            else:
                try:
                    os.system(f"{md_run} {execute} {module_prefix_run}")
                except:
                    pass
        else:
            try:
                os.system(f"{md_run} {execute} {module_prefix_run}")
            except:
                pass
        print(Fore.BLUE+'[i]'+Fore.RESET+' Modülü yürütme tamamlandı.')
    execute = ""
    not_sp = ""
    found = False
    for n in add:
        try:
            if os.path.exists(module_run+n):
                execute = module_run+n
                found = True
            else:
                continue
        except:
            pass
    if found == False:
        print(Fore.RED+'[-]'+Fore.RESET+' Modül dosyası bulunamıyor ve çalıştırılamıyor, Hata: Modül bulunamıyor.')
        sys.exit()
    for ch in module_options.keys():
        if module_options[ch][1] == "":
            not_sp += ch+', '
    if not_sp == "":
        ex()
    else:
        print(Fore.RED+'[-]'+Fore.RESET+f' Gerekli seçenekler ayarlanmamış: {str(not_sp).lstrip()}')


if module_type.lower() == "payload":
    print(Fore.BLUE+'[i]'+Fore.RESET+f' Yükleme işleyicisi (Handler) Payload "{module_cmd}" İcin yükleniyor...')
def main():
    while True:
        try:
            btf = input(f'\033[4mbtf\033[0m {module_type}-({Fore.RED}{module_cmd}{Fore.RESET}) > ').strip(" ")
        except KeyboardInterrupt:
            # print(Fore.RED+"\n[-]"+Fore.RESET+' CTRL + C alındı, çıkılıyor...')
            time.sleep(0.2)
            sys.exit()
        btf = btf.split()
        if btf == []:
            pass
        elif btf[0] == 'help':
            print(commands)
        elif btf[0] == 'clear':
            os.system('clear')
        elif btf[0] == 'exit' or btf[0] == 'quit' or btf[0] == 'back':
            sys.exit()
        elif btf[0] == 'show':
            if len(btf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Kullanım: show <-o>')
            else:
                try:
                    if btf[1] == '-o':
                        def show_options():
                            options = f'''
Modül ({Fore.RED}{module_cmd}{Fore.RESET}) seçenekleri
==========================================================================
                        
Ad / değeri
----------------------
'''
                            for op in module_options.keys():
                                options += op+" : "+Fore.LIGHTGREEN_EX+str(module_options[op][1])+Fore.RESET+"\n"
                            print(options)
                        if module_type.lower() == "payload":
                            if module_options == {} or module_options == {'\n'}:
                                print(Fore.BLUE+'[i]'+Fore.RESET+' Bu Payload\'ın seçeneği yoktur.')
                            else:
                                show_options()
                        else:
                            show_options()
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz komut: "'+btf[1]+'"')
                except:
                    pass
        elif btf[0] == 'set':
            if len(btf) < 3:
                print(Fore.RED+'[-]'+Fore.RESET+' Kullanım: set <option> <value>')
            else:
                try:
                    if btf[1].upper() in module_options.keys():
                        module_options[btf[1].upper()][1] = btf[2]
                        print(Fore.BLUE+'[i]'+Fore.RESET+f' {btf[1].upper()} ==> {btf[2]}')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz seçenek: "'+btf[1].upper()+'"')
                except:
                    pass
        elif btf[0] == 'info':
            if len(btf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Kullanım: info <option>')
            else:
                try:
                    if btf[1].upper() in module_options.keys():
                        print(Fore.BLUE+'[i]'+Fore.RESET+f' {btf[1].upper()}: {Fore.LIGHTGREEN_EX}{module_options[btf[1].upper()][0]}{Fore.RESET}')
                        print('---------------------------------------------------------------------------------------------------------------')
                        print(Fore.BLUE+'[i]'+Fore.RESET+f' Modül versiyonu: {Fore.LIGHTGREEN_EX}{module_version}{Fore.RESET}')
                        # print(Fore.BLUE+'[i]'+Fore.RESET+f' Modülü Yazan(lar): {Fore.LIGHTGREEN_EX}{module_author}{Fore.RESET}')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz seçenek: "'+btf[1].upper()+'"')
                except:
                    pass
        elif btf[0] == 'run' or btf[0] == 'exploit':
            run()
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Bilinmeyen komut: "'+btf[0]+'"')

main()
