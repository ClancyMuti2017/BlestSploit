# from curses.ascii import isdigit
# from genericpath import isdir
import json
import importlib
def load_module_data(name):
    load_module = importlib.import_module(name)
    return load_module
import configparser
import os, subprocess, time, random, socket, colorama, sys, platform, shutil
from colorama import *
# from flask import current_app
from banners.banner import banner
from banners.official import banner_official
from db.cache import cache
init()
Cache = cache()
Cache.generate()
database = '/usr/share/blest-framework'
core = '/usr/share/blest-framework/src/data'
modules = core+'/modules'
banners = core+'/core/base/banners/banner.py'
banners_config = core+'/config.ini'
read_config_banners = configparser.RawConfigParser()
read_config_banners.read(banners_config)
unofficial_banners = None
official_banners = None
bn = 0
if read_config_banners['banners']['unofficial'] == "true":
    unofficial_banners = True
else:
    unofficial_banners = False
if read_config_banners['banners']['official'] == "true":
    official_banners = True
else:
    official_banners = False
ignore = ['.txt', '.log', '.yml', '.yaml', '.ini', '.md', '.json', '.bin']
add = ['.py', '.pyw', '.c', '.cpp', '.so', '.pl', '.rb', '.sh']
loaded_modules = []
broken_modules = []
loaded_modules_all = {}
loaded_modules_exploits = {}
loaded_modules_payloads = {}
loaded_modules_posts = {}
loaded_modules_usbs = {}
unknown_modules = []
version = ""
try:
    with open(core+'/VERSION', 'r') as v:
        version = v.read()
except:
    pass
if version == "":
    version = "???"
exploits = 0
payloads = 0
posts = 0
usbs = 0
usb_device = "USB cihazı yok"
broken_modules_int = 0
check_module_type = [
    'exploit',
    # 'exploits',
    'usb',
    # 'usbs',
    'payload',
    # 'payloads',
    'post'
    # 'posts'
]
Banner = banner()
Official_Banner = banner_official()
normals = 0
usb_checker_code = '''
REMOVABLE_DRIVES=""
for _device in /sys/block/*/device; do
    if echo $(readlink -f "$_device")|egrep -q "usb"; then
        _disk=$(echo "$_device" | cut -f4 -d/)
        REMOVABLE_DRIVES="$REMOVABLE_DRIVES $_disk"
    fi
done
echo "$REMOVABLE_DRIVES"
# is_usb_device() {
#     local device_path=$1 
#     for devlink in /dev/disk/by-id/usb*; do
#         if [ "$(readlink -f "$devlink")" = "$device_path" ]; then
#             return 0
#         fi
#     done
#     return 1
# }
# if is_usb_device "/dev/sdg"; then
#     echo "'/dev/sdg' bir USB cihazıdır"
# else
#     echo "'/dev/sdg' bir USB cihazı değil"
# fi
'''
root = os.listdir("/root/.btf")
if root == [] or root == ['\n'] or root == False:
    pass
else:
    for files in root:
        try:
            if ".yml" in files or files == "settings" or files == "database" or files == "files" or ".conf" in files:
                continue
            else:
                os.remove("/root/.btf/"+files)
        except:
            pass
about = '''
BlestSploit hakkında
======================
Yazan                  : Marcus Walker (Ənvər) veya G00Dway
Bizim Takım            : Blest Boyz
Bizim Patronumuz       : Fux Walker
Üyelerimiz (Krediler)  : Nemesis, Rotasız, Dilax, Cyrus, Yakuza, Diğerleri...

Sosyal Hesaplar
======================
Discord                : https://discord.gg/2qr6U6ggUN
'''
commands = '''
Global Komutlar
======================

    Komutlar                        Tanım
    --------                        --------
    help                            Mevcut komutları göster, yardım
    clear                           Terminal pencere ekranını temizleyin
    exit, back                      Blestsploit'ten çıkın, modül kullanımından geri dönün

Ana Menü Komutları
======================

    Komutlar                        Tanım
    --------                        --------
    help                            Mevcut komutları göster, yardım
    show <arg>                      Verilen tipte modülleri veya tüm modülleri görüntüler (Daha fazla bilgi için "show" yazın)
    use <type> <module>             Belirtilen modülü veya numarasını kullanın (Mes: "use exploit exploit/myexploit" veya "use exploit 1")
    update                          En son güncellemeleri kontrol et ve varsa güncelle
    about                           Geliştiriciler Hakkında Göster, ve s.
    banner                          Banner'ı Göster
    info <name>                     Belirtilen modül hakkında bazı bilgileri gösterin
    edit <name>                     Belirtilen modülü düzenleyin (belirtilen modülde Shellcode kodunu veya Payload'ı değiştirmek istiyorsanız önerilir)
    usb <dev>                       USB modülleri için belirli bir USB cihazı "/dev/sdaX" kullanın (cihazları/sürücüleri görmek için "usb" yazın)
    marketplace                     Global Modüller Marketplace'i (Modül İndir/Yükle)

Database Komutları
======================

    Komutlar                        Tanım
    --------                        --------
    update                          En son güncellemeleri kontrol et ve varsa güncelle

Modül komutları
======================

    Komutlar                        Tanım
    --------                        --------
    set <option> <value>            Modülde belirtilen değere belirtilen seçeneği ayarlayın
    run, exploit                    Kullanılan modülü yükleyin, Başlatın
'''
show_commands = '''
Show Komutları
======================

    Komutlar                        Tanım
    --------                        --------
    show -a                         Mevcut tüm Modülleri göster
    show -e                         Mevcut tüm Exploitler'i göster
    show -p                         Mevcut tüm Payloadlar'ı göster
    show -ps                        Mevcut tüm POSTlar'ı göster
    show -u                         Mevcut tüm USB Exploitler'i göster

Show Modül komutları
======================

    Komutlar                        Tanım
    --------                        --------
    show -o                         Yüklü modülün seçeneklerini göster
'''
json_script = '''
'''
try:
    if os.path.exists(core+'/core/module/data.json'):
        with open(core+'/core/module/data.json', 'r') as f:
            json_script = f.read()
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Açıklama Veri yolu yok, açıklamalar gösterilmeyecek!')
except:
    pass
json_data = json.loads(json_script)
def show_banner():
    Banner.generate()
    print(Fore.RESET+welcome)

def show_official_banner():
    Official_Banner.generate()
    print(Fore.RESET+welcome)

module_descriptions = {}
mod = {}

def load_modules():
    def desc_module():
        global module_descriptions, loaded_modules, mod
        # mod = {}
        for check in json_data:
            for typ in add:
                if typ in check:
                    mod[str(check).replace(typ, "")] = check
                    break
        for module_name in loaded_modules:
            for val in mod.keys():
                if val in module_name:
                    module_descriptions[mod[val]] = json_data[mod[val]]
                    break
                
    global exploits, payloads, usbs, posts, loaded_modules, broken_modules, broken_modules_int, normals
    # exploits, payloads, usbs, posts, loaded_modules, broken_modules, broken_modules_int, normals = 0, 0
    get = os.listdir(modules)
    def sort_all():
        global exploits, payloads, usbs, posts, loaded_modules, broken_modules, broken_modules_int, normals, loaded_modules_all, loaded_modules_exploits, loaded_modules_payloads, loaded_modules_posts, loaded_modules_usbs, unknown_modules
        num_all = 0
        num_ex = 0
        num_pl = 0
        num_ub = 0
        num_ps = 0
        loaded_modules_all.clear()
        for i in loaded_modules:
            num_all+=1
            loaded_modules_all[str(num_all)] = i
            current_module = str(i).split("/")
            current_module = current_module[0]
            if current_module == "exploit" or current_module == "exploits":
                num_ex += 1
                loaded_modules_exploits[str(num_ex)] = i
            elif current_module == "payload" or current_module == "payloads":
                num_pl += 1
                loaded_modules_payloads[str(num_pl)] = i
            elif current_module == "post" or current_module == "posts":
                num_ps += 1
                loaded_modules_posts[str(num_ps)] = i 
            elif current_module == "usb" or current_module == "usbs":
                num_ub += 1
                loaded_modules_usbs[str(num_ub)] = i 
            else:
                unknown_modules.append(i)
    def add_module(dir, module_type):
        global exploits, payloads, usbs, posts, loaded_modules, broken_modules, broken_modules_int, normals
        if module_type == "exploit" or module_type == "exploits":
            exploits += 1
        elif module_type == "payload" or module_type == "payloads":
            payloads += 1
        elif module_type == "usb" or module_type == "usbs":
            usbs += 1
        elif module_type == "post" or module_type == "posts":
            posts += 1
        elif module_type == "module" or module_type == "modules":
            normals += 1
        else:
            broken_modules_int += 1
        loaded_modules.append(dir)
    use = ""
    current = ""
    for module in get:
        current = ""
        if os.path.isdir(modules+'/'+module):
            get_dir = os.listdir(modules+'/'+module)
            for module_second in get_dir:
                if os.path.isdir(modules+'/'+module+'/'+module_second):
                    get_dir_second = os.listdir(modules+'/'+module+'/'+module_second)
                    for module_third in get_dir_second:
                        if os.path.isdir(modules+'/'+module+'/'+module_second+'/'+module_third):
                            get_dir_fourth = os.listdir(modules+'/'+module+'/'+module_second+'/'+module_third)
                            for module_fourth in get_dir_fourth:
                                if os.path.isdir(modules+'/'+module+'/'+module_second+'/'+module_third+'/'+module_fourth):
                                    # print(Fore.MAGENTA+'[!]'+Fore.RESET+f' "{module_fourth}" Modüllü dizin yüklenecek ancak iptal olunacak sonra, maksimum modül dizin yükü - 4')
                                    get_dir_five = os.listdir(modules+'/'+module+'/'+module_second+'/'+module_third+'/'+module_fourth)
                                    for module_five in get_dir_five:
                                        if os.path.isdir(modules+'/'+module+'/'+module_second+'/'+module_third+'/'+module_fourth+'/'+module_five):
                                            print(Fore.MAGENTA+'[!]'+Fore.RESET+' Çok fazla dizin, dizin veya modül geçildi: "'+module_five+'"')
                                            break
                                else:
                                    use = module+'/'+module_second+'/'+module_third+'/'+module_fourth
                                    for g in ignore:
                                        if g in use:
                                            print(Fore.MAGENTA+'[!]'+Fore.RESET+' Kırık veya bilinmeyen bir modül tipi tespit edildi, ancak yine de elave ediliyor...')
                                            break
                                    for n in add:
                                        if n in use:
                                            use = use.replace(n, "")
                                            break
                                    add_module(use, module)
                        else:
                            use = module+'/'+module_second+'/'+module_third
                            for g in ignore:
                                if g in use:
                                    print(Fore.MAGENTA+'[!]'+Fore.RESET+' Kırık veya bilinmeyen bir modül tipi tespit edildi, ancak yine de elave ediliyor...')
                                    break
                            for n in add:
                                if n in use:
                                    use = use.replace(n, "")
                                    break
                            add_module(use, module)
                else:
                    use = module+'/'+module_second
                    for g in ignore:
                        if g in use:
                            print(Fore.MAGENTA+'[!]'+Fore.RESET+' Kırık veya bilinmeyen bir modül tipi tespit edildi, ancak yine de elave ediliyor...')
                            break
                    for n in add:
                        if n in use:
                            use = use.replace(n, "")
                            break
                    add_module(use, module)
        else:
            use = modules+'/'+module
            for g in ignore:
                if g in use:
                    print(Fore.MAGENTA+'[!]'+Fore.RESET+' Kırık veya bilinmeyen bir modül tipi tespit edildi, ancak yine de elave ediliyor...')
                    break
            for n in add:
                if n in use:
                    use = use.replace(n, "")
                    break
            add_module(use, modules)
    sort_all()
    desc_module()

def main():
    global usb_device
    while True:
        try:
            btf = input('\033[4mbtf\033[0m > ').strip(" ")
        except KeyboardInterrupt:
            print(Fore.RED+"\n[-]"+Fore.RESET+' CTRL + C alındı, çıkılıyor...')
            time.sleep(0.2)
            sys.exit()
        btf = btf.split()
        if btf == []:
            pass
        elif btf[0] == 'help' or btf[0] == '?':
            print(commands)
        elif btf[0] == 'clear':
            os.system("clear")
        elif btf[0] == 'exit' or btf[0] == 'quit':
            sys.exit()
        elif btf[0] == 'back':
            pass
        elif btf[0] == 'edit':
            if len(btf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Kullanım: edit <name>')
            else:
                try:
                    if btf[1] in loaded_modules:
                        try:
                            for g in add:
                                if os.path.exists(modules+"/"+btf[1]+g):
                                    os.system(f"nano {modules}/{btf[1]}{g}")
                                    break
                        except:
                            pass
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz Modül: "'+btf[1]+'"')
                except:
                    pass
        elif btf[0] == 'show':
            if len(btf) < 2:
                print(show_commands)
            else:
                try:
                    see = ""
                    expl = f'''
Modüller
-----------'''
                    if btf[1] == '-e':
                        num = 0
                        see = "Exploitler"
                        if loaded_modules_exploits == {} or loaded_modules_exploits == {'\n'}:
                            print(Fore.RED+'[-]'+Fore.RESET+' Exploitler yok.')
                        else:
                            for exploit in loaded_modules_exploits.keys():
                                num+=int(exploit)
                                expl += "\n"+loaded_modules_exploits[exploit]
                            print(f"\n{expl}\n")
                    elif btf[1] == '-p':
                        num = 0
                        see = "Payloadlar"
                        if loaded_modules_payloads == {} or loaded_modules_payloads == {'\n'}:
                            print(Fore.RED+'[-]'+Fore.RESET+' Payloadlar yok.')
                        else:
                            for payload in loaded_modules_payloads.keys():
                                num+=int(payload)
                                expl += "\n"+loaded_modules_payloads[payload]
                            print(f"\n{expl}\n")
                    elif btf[1] == '-ps':
                        num = 0
                        see = "POSTlar"
                        if loaded_modules_posts == {} or loaded_modules_posts == {'\n'}:
                            print(Fore.RED+'[-]'+Fore.RESET+' POSTlar yok.')
                        else:
                            for post in loaded_modules_posts.keys():
                                num+=int(post)
                                expl += "\n"+loaded_modules_posts[post]
                            print(f"\n{expl}\n")
                    elif btf[1] == '-u':
                        num = 0
                        see = "USB Exploitler"
                        if loaded_modules_usbs == {} or loaded_modules_usbs == {'\n'}:
                            print(Fore.RED+'[-]'+Fore.RESET+' USB Exploitler yok.')
                        else:
                            for usb in loaded_modules_usbs.keys():
                                num+=int(usb)
                                expl += "\n"+loaded_modules_usbs[usb]
                            print(f"\n{expl}\n")
                    elif btf[1] == '-a':
                        num = 0
                        see = "Tüm Modüller"
                        if loaded_modules_all == {} or loaded_modules_all == {'\n'}:
                            print(Fore.RED+'[-]'+Fore.RESET+' Modüllar yok!.')
                        else:
                            for all in loaded_modules_all.keys():
                                num+=int(all)
                                expl += "\n"+loaded_modules_all[all]
                            print(f"\n{expl}\n")
                    elif btf[1] == '-o':
                        print(Fore.RED+'[-]'+Fore.RESET+' Lütfen bu komutu kullanmadan önce bir modül kullanın!')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Bilinmeyen argument: "'+btf[1]+'"')
                except:
                    pass
        elif btf[0] == 'use':
            if len(btf) < 3:
                print(Fore.RED+'[-]'+Fore.RESET+' Kullanım: use <type> <module>')
            else:
                try:
                    accept = False
                    load = ""
                    if btf[1] in check_module_type:
                        if btf[1] == "exploit":
                            if btf[2] in loaded_modules_exploits.keys():
                                accept = True
                            else:
                                for check in loaded_modules_exploits.keys():
                                    if loaded_modules_exploits[check] == btf[2]:
                                        accept = True
                                        break
                            if accept:
                                # print(Fore.BLUE+'[i]'+Fore.RESET+' Modül "'+btf[2]+'" Yükleniyor...')
                                load = "exploit"
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz Modül: "'+btf[2]+'"')
                        elif btf[1] == "payload":
                            if btf[2] in loaded_modules_payloads.keys():
                                accept = True
                            else:
                                for check in loaded_modules_payloads.keys():
                                    if loaded_modules_payloads[check] == btf[2]:
                                        accept = True
                                        break
                            if accept:
                                # print(Fore.BLUE+'[i]'+Fore.RESET+' Modül "'+btf[2]+'" Yükleniyor...')
                                load = "payload"
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz Modül: "'+btf[2]+'"')
                        elif btf[1] == "post":
                            if btf[2] in loaded_modules_posts.keys():
                                accept = True
                            else:
                                for check in loaded_modules_posts.keys():
                                    if loaded_modules_posts[check] == btf[2]:
                                        accept = True
                                        break
                            if accept:
                                # print(Fore.BLUE+'[i]'+Fore.RESET+' Modül "'+btf[2]+'" Yükleniyor...')
                                load = "post"
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz Modül: "'+btf[2]+'"')
                        elif btf[1] == "usb":
                            if btf[2] in loaded_modules_usbs.keys():
                                accept = True
                            else:
                                for check in loaded_modules_usbs.keys():
                                    if loaded_modules_usbs[check] == btf[2]:
                                        accept = True
                                        break
                            if accept:
                                # print(Fore.BLUE+'[i]'+Fore.RESET+' Modül "'+btf[2]+'" Yükleniyor...')
                                load = "usb"
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz Modül: "'+btf[2]+'"')
                        else:
                            pass
                        if accept:
                            cr = btf[2]
                            if cr.isdigit():
                                if load == "exploit":
                                    cr = loaded_modules_exploits[cr]
                                elif load == "payload":
                                    cr = loaded_modules_payloads[cr]
                                elif load == "post":
                                    cr = loaded_modules_posts[cr]
                                elif load == "usb":
                                    cr = loaded_modules_usbs[cr]
                                else:
                                    pass
                            if load == "usb":
                                if usb_device == "USB cihazı yok" or usb_device == "" or usb_device == []:
                                    print(Fore.RED+'[-]'+Fore.RESET+' Lütfen bir USB modülü yüklemeden önce bir USB cihazı seçin!')
                                else:
                                    print(Fore.BLUE+'[i]'+Fore.RESET+' USB Cihazı Kullanılıyor: "'+usb_device+'"...')
                                    umount = subprocess.getoutput("umount "+usb_device) 
                                    time.sleep(1)
                                    mount = subprocess.getoutput("mount "+usb_device+" "+database+"/devices/USB")
                                    if "error" in mount or "Error" in mount or "error" in umount or "Error" in umount:
                                        print(Fore.RED+'[-]'+Fore.RESET+' USB Cihaz Kullanılamıyor: "'+usb_device+'"...')
                                    else:
                                        os.system(f"python3 {core}/core/module/__load__.py {load} {usb_device} {core}/modules/{cr} {cr}")
                            else:
                                os.system(f"python3 {core}/core/module/__load__.py {load} false {core}/modules/{cr} {cr}")
                        else:
                            pass
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz Modül Tipi: "'+btf[1]+'"')
                except:
                    pass
        elif btf[0] == 'about':
            print(about)
        elif btf[0] == 'banner':
            if bn == 0:
                show_official_banner()
            elif bn == 1:
                show_banner()
            else:
                show_banner()
        elif btf[0] == 'info':
            if len(btf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Kullanım: info <name>')
            else:
                try:
                    ch = ""
                    current = ""
                    info = '''
    '''
                    to_break = False
                    if "/" in btf[1]:
                        if str(btf[1]) in loaded_modules:
                            for desc in module_descriptions.keys():
                                if to_break:
                                    break
                                for typ in add:
                                    if typ in desc:
                                        ch = str(desc).replace(typ, "")
                                        current = desc
                                        if ch in btf[1]:
                                            print(Fore.BLUE+'[i]'+Fore.RESET+' Modül Açıklaması: "'+module_descriptions[desc]+'"')
                                            print('------------------------------------------------------------------------------------------------------------------------------')
                                            print(Fore.BLUE+'[i]'+Fore.RESET+' Modül Tam dosya adı: "'+desc+'"')
                                            print(Fore.BLUE+'[i]'+Fore.RESET+' Modül Adı: "'+btf[1]+'"')
                                            # print(Fore.BLUE+'[i]'+Fore.RESET+' Modülü yazan: Blest Boyz Team')
                                            # print(Fore.BLUE+'[i]'+Fore.RESET+' Modül versiyonu: Tüm sürümler?')
                                            to_break = True
                                            break
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+' Modül yok: "'+btf[1]+'"')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz Modül Adı: "'+btf[1]+'"')
                except:
                    pass
        elif btf[0] == 'usb':
            if usb_device == "" or usb_device == []:
                print(Fore.RED+'[-]'+Fore.RESET+' USB cihazı yok! lütfen birini seçin!')
            if len(btf) < 2:
                print(Fore.BLUE+'[i]'+Fore.RESET+' Bağlı cihazlar listeleniyor...')
                execute = subprocess.getoutput(f"bash {core}/src/usb.sh")
                execute = execute.split()
                devices = []
                time.sleep(1)
                if execute == [] or execute == ['\n'] or execute == {} or execute == ['']:
                    print(Fore.RED+'[-]'+Fore.RESET+' USB cihazları bulunamadı!')
                else:
                    usb_num = 0
                    for i in execute:
                        usb_num += 1
                        devices.append("/dev/"+i)
                        print(Fore.BLUE+'[i]'+Fore.RESET+f' USB Cihaz {usb_num}: "/dev/{i}"')
                print(Fore.RED+'[-]'+Fore.RESET+' Kullanım: usb </dev/sdaX>')
            else:
                try:
                    devices = []
                    if btf[1] in devices:
                        usb_device = btf[1]
                        print(Fore.BLUE+'[i]'+Fore.RESET+f' USB cihazı başarıyla ayarlandı ==> "{usb_device}"')
                    else:
                        if "/" in btf[1] or "/dev" in btf[1]:
                            usb_device = btf[1]
                            print(Fore.BLUE+'[i]'+Fore.RESET+f' USB cihazı başarıyla ayarlandı, Ama tanınmadı ==> "{usb_device}"')
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz USB cihaz yolu: "'+btf[1]+'"')
                except:
                    pass
        elif btf[0] == 'marketplace':
            # print(Fore.BLUE+'[i]'+Fore.RESET+' MarketPlace yükleniyor...')
            print(Fore.BLUE+'[i]'+Fore.RESET+' MarketPlace şu anda mevcut değil, ancak yakında açilacak!')
            # os.system(f"python3 {core}/core/marketplace/__base__.py")
        elif btf[0] == 'update':
            os.system(f"bash {core}/src/update/__update__.sh")
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Bilinmeyen komut: "'+btf[0]+'"')

load_modules()
# exploits = 0
# payloads = 0
# posts = 0
# usbs = 0
# for i in loaded_modules_exploits.keys():
#     exploits += 1
# for n in loaded_modules_payloads.keys():
#     payloads += 1
# for k in loaded_modules_posts.keys():
#     posts += 1
# for l in loaded_modules_usbs.keys():
#     usbs += 1
welcome = '''
+ -- ---={ '''+Fore.YELLOW+'''BlestSploit Framework V.'''+str(version)+Fore.RESET+'''
- -- ---={ Tüm Exploitler : '''+str(exploits)+''', Tüm Payloadlar : '''+str(payloads)+''',   
- -- ---={ Tüm USB Exploitler : '''+str(usbs)+''', Tüm POSTlar : '''+str(posts)+'''
'''
if official_banners:
    show_official_banner()
    bn = 0
else:
    if unofficial_banners:
        show_banner()
        bn = 1
    else:
        show_banner()
        bn = 1
main()
