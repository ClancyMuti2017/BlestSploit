from curses.ascii import isdigit
import os, sys, colorama, subprocess, json, random, time
from colorama import *
init()
database = '/usr/share/blest-framework'
core = '/usr/share/blest-framework/src/data'
modules = core+'/modules'
banners = core+'/core/base/banners/banner.py'
datas = core+'/marketplace/data.json'
marketplace_modules = core+'/src/core/runtime'
try:
    if os.path.exists(marketplace_modules):
        pass
    else:
        os.mkdir(marketplace_modules)
except:
    pass
ignore = ['.txt', '.log', '.yml', '.yaml', '.ini', '.md']
add = ['.py', '.pyw', '.c', '.cpp', '.so', '.pl', '.rb']
installed_modules = []
s = os.listdir(marketplace_modules)
for i in s:
    installed_modules.append(i)
try:
    if os.path.exists(database+'/files/cache'):
        pass
    else:
        os.mkdir(database+'/files/cache')
except:
    pass
types = []
show_commands = '''
Show komutları
========================

    Komutlar                          Tanım
    --------                          --------
    show -a                           Tüm yüklenebilir modülleri, core dosyaları vb. Göster.
'''
commands = '''
Marketplace komutları
========================

    Komutlar                          Tanım
    --------                          --------
    help                              Mevcut komutları göster, yardım
    clear                             Terminal pencere ekranını temizleyin
    show <arg>                        Tüm modülleri, core dosyalar ve s. görüntüler (Daha fazla bilgi için "show" yazın)
    exit                              MarketPlace'ten çıkın, geri dönün

Yükleme/indirme Komutları
========================

    Komutlar                          Tanım
    --------                          --------
    info <name>                       Belirtilen modül, core dosya vb. hakkında bazı bilgiler gösterin
    install <id:name>                 Belirtilen modül, core dosya vb. indirin ve yükleyin
    uninstall <id:name>               Yüklü belirtilen modül, core dosya vb. kaldır
'''
function_print = '''
#                Adı
-                ---------'''
json_script = '''
'''
modules_dict = {}
try:
    if os.path.exists(datas):
        with open(datas, "r") as f:
            json_script = f.read()
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Config dosya yolu yok, ölümcül hata!')
        sys.exit()
except:
    pass
json_data = json.loads(json_script)
for ty in json_data:
    types.append(ty)


def install_module(module):
    accept = False
    invalid = False
    def install(url, manager, path, zip_name, prefix, module_type, file_ext, module_name):
        m = module_name
        print(Fore.BLUE+'[i]'+Fore.RESET+f' "{m}" yükleniyor...')
        def install_main():
            try:
                os.system(f"{manager} {url} {prefix} {path}")
            except:
                pass
        install_main()
        try:
            if os.path.exists(path+'/'+zip_name):
                pass
            else:
                print(Fore.RED+'[-]'+Fore.RESET+' Kurulum başarısız oldu, internetiniz var mı? Tekrar deneniyor...')
                install_main()
        except Exception:
            pass
        print(Fore.BLUE+'[i]'+Fore.RESET+' İndirme başarılı oldu, kuruluyor...')
        time.sleep(1)
        ch = subprocess.getoutput("unrar")
        if "command not found" in ch or "command not found".upper() in ch or "command not found".capitalize() in ch:
            print(Fore.BLUE+'[i]'+Fore.RESET+' Lütfen "UNRAR" Programının Yüklemeyin Bekleyin...')
        dw = subprocess.getoutput("apt install unrar -y")
        os.system(f"unrar x {path}/{zip_name} {marketplace_modules} > /dev/null 2>&1")
        time.sleep(1)
        # os.system(f"cp -r {marketplace_modules}/{file_ext} {marketplace_modules}/{module_type} &>> {path}/{file_ext}.log")
        print(Fore.YELLOW+'[+]'+Fore.RESET+f' "{m}" başarıyla yüklendi!')
        print(Fore.BLUE+'[i]'+Fore.RESET+f" \"{m}\" Yüklemek için Blestsploit'i yeniden başlatmanız öneririz....")
        # print(Fore.BLUE+'[i]'+Fore.RESET+" Eger modül BlestSploit'e yüklenmezse, lütfen BlestSploit'i yeniden başlatın!")
    if module.isdigit():
        for ty in json_data:
            if accept:
                break
            for num in json_data[ty]:
                if json_data[ty][num]['ext_filename'] in installed_modules:
                    n = json_data[ty][num]['lookup_name']
                    print(Fore.BLUE+'[i]'+Fore.RESET+f' "{n}" zaten kurulu!')
                    accept = True
                    invalid = True
                    break
                else:
                    if num == module:
                        install(json_data[ty][num]['url'], json_data[ty][num]['download_manager'], json_data[ty][num]['save_path'], json_data[ty][num]['filename'], json_data[ty][num]['prefix'], json_data[ty][num]['type'][0], json_data[ty][num]['ext_filename'], json_data[ty][num]['lookup_name'])
                        accept = True
                        invalid = True
                        break
                    else:
                        invalid = False
    else:
        installed = True
        for ty in json_data:
            if accept:
                break
            for num in json_data[ty]:
                if json_data[ty][num]['lookup_name'] == module:
                    if json_data[ty][num]['ext_filename'] in installed_modules:
                        n = json_data[ty][num]['lookup_name']
                        print(Fore.BLUE+'[i]'+Fore.RESET+f' "{n}" zaten kurulu!')
                        accept = True
                        invalid = True
                        installed = True
                        break
                    else:
                        installed = False
        if installed == False:
            for ty in json_data:
                if accept:
                    break
                for num in json_data[ty]:
                    for name in json_data[ty][num]["lookup_name"]:
                        if name == module:
                            install(json_data[ty][num]['url'], json_data[ty][num]['download_manager'], json_data[ty][num]['save_path'], json_data[ty][num]['filename'], json_data[ty][num]['prefix'], json_data[ty][num]['type'][0], json_data[ty][num]['ext_filename'], json_data[ty][num]['lookup_name'])
                            accept = True
                            invalid = True
                            break
                        else:
                            invalid = False
    if invalid:
        pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz ID/Ad: "'+module+'"')


def remove_module(module):
    accept = False
    invalid = False
    def remove(filename, module_type):
        try:
            if os.path.exists(marketplace_modules+'/'+filename):
                os.remove(marketplace_modules+'/'+filename)
            if os.path.exists(marketplace_modules+'/'+module_type+'/'+filename):
                os.remove(marketplace_modules+'/'+module_type+'/'+filename)
        except:
            pass
    if module.isdigit():
        for ty in json_data:
            if accept:
                break
            for n in json_data[ty]:
                if n == module:
                    m = json_data[ty][n]['lookup_name']
                    if json_data[ty][n]['ext_filename'] in installed_modules:
                        print(Fore.BLUE+'[i]'+Fore.RESET+f' "{m}" Kaldırılıyor...')
                        remove(json_data[ty][n]['ext_filename'], json_data[ty][n]['type'][0])
                        time.sleep(1)
                        print(Fore.RED+'[-]'+Fore.RESET+f' "{m}" başarıyla kaldırıldı!')
                        accept = True
                        invalid = True
                        break
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+f' "{m}" zaten kurulmamış!')
                        accept = True
                        invalid = True
                        break
                else:
                    invalid = False
    else:
        for ty in json_data:
            for m in json_data[ty]:
                if json_data[ty][m]['lookup_name'] == module:
                    l = json_data[ty][m]['lookup_name']
                    if json_data[ty][m]['ext_filename'] in installed_modules:
                        print(Fore.BLUE+'[i]'+Fore.RESET+f' "{l}" Kaldırılıyor...')
                        remove(json_data[ty][m]['ext_filename'], json_data[ty][m]['type'][0])
                        time.sleep(1)
                        print(Fore.RED+'[-]'+Fore.RESET+f' "{l}" başarıyla kaldırıldı!')
                        accept = True
                        invalid = True
                        break
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+f' "{l}" zaten kurulmamış!')
                        accept = True
                        invalid = True
                        break
                else:
                    invalid = False

    if invalid:
        pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz modül, core dosya vb.: "'+module+'"')

def info_module(value, module):
    accept = False
    to_break = False
    if value == "str":
        for ch in json_data:
            if to_break:
                break
            for name in json_data[ch]:
                if to_break:
                    break
                for lookup in json_data[ch][name]:
                    if module == json_data[ch][name]['lookup_name']:
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Adı: "'+module+'"')
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Başlığı: "'+json_data[ch][name]['name']+'"')
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Açıklaması: "'+json_data[ch][name]['description']+'"')
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Yazan: "'+json_data[ch][name]['author']+'"')
                        # print(Fore.BLUE+'[i]'+Fore.RESET+' Tipi: "'+json_data[ch][name]['type'][0]+', "'+ch+'"')
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Versiyonu: '+json_data[ch][name]['version'])
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Kod Dili: "'+json_data[ch][name]['language']+'"')
                        # print(Fore.BLUE+'[i]'+Fore.RESET+' Kod Dili "'+json_data[ch][name]['language']+'" bağımlılıkları: "'+str(json_data[ch][name]['pip_depends'])+'"')
                        to_break = True
                        accept = True
                        break
                    else:
                        accept = False
    if accept:
        pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz Modül: "'+module+'"')


def load_modules():
    global modules_dict, json_data, function_print
    num = 0
    for ty in json_data:
        for number in json_data[ty]:
            num += int(number)
            if num < 10:
                function_print += f"\n{number}                {json_data[ty][number]['lookup_name']}"
            elif num > 10:
                function_print += f"\n{number}               {json_data[ty][number]['lookup_name']}"
            # this line is not required but just added if something happens :)
            # for dict in json_data[ty][number]:
            #     modules_dict[ty][number] = dict


def main():
    while True:
        s = os.listdir(marketplace_modules)
        for i in s:
            installed_modules.append(i)
        try:
            mkf = input(f'\033[4mbtf\033[0m [{Fore.RED}MarketPlace{Fore.RESET}] > ').strip(" ")
        except KeyboardInterrupt:
            print('')
            sys.exit()
        mkf = mkf.split()
        if mkf == []:
            pass
        elif mkf[0] == 'help':
            print(commands)
        elif mkf[0] == 'clear':
            os.system('clear')
        # elif mkf[0] == 'types':
        #     print('')
        #     print("Mevcut Modül Tipleri")
        #     print('-----------------------')
        #     for type in types:
        #         print(str(type).upper())
        #     print('')
        elif mkf[0] == 'show':
            if len(mkf) < 2:
                print(show_commands)
            else:
                try:
                    if mkf[1] == '-a':
                        print(function_print+'\n')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz komut: "'+mkf[1]+'"')
                except:
                    pass
        elif mkf[0] == 'exit' or mkf[0] == 'quit':
            sys.exit()
        elif mkf[0] == 'info':
            if len(mkf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Kullanım: info <name>')
            else:
                try:
                    accept = False
                    if mkf[1].isdigit():
                        for ty in json_data:
                            for number in json_data[ty]:
                                if mkf[1] == str(number):
                                    accept = True
                                    info_module("int", mkf[1])
                                    break
                    else:
                        for ty in json_data:
                            for lookup in json_data[ty]:
                                if mkf[1] == json_data[ty][lookup]['lookup_name']:
                                    accept = True
                                    info_module("str", mkf[1])
                                    break
                    if accept:
                        pass
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz modül, core dosya vb. Adı: "'+mkf[1]+'"')
                except:
                    pass
        elif mkf[0] == 'install':
            if len(mkf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Kullanım: install <name> veya <id>')
            else:
                try:
                    install_module(mkf[1])
                except:
                    pass
        elif mkf[0] == 'uninstall':
            if len(mkf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Kullanım: uninstall <name> veya <id>')
            else:
                try:
                    remove_module(mkf[1])
                except:
                    pass
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Bilinmeyen komut: "'+mkf[0]+'"')
load_modules()
main()