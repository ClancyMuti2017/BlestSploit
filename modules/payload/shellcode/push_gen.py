from colorama import Fore
import sys


def print_word(word):
    print(Fore.BLUE+'[i]'+Fore.RESET+' 0x' + word[::-1].encode('hex'))

if len(sys.argv) != 2:
    print('usage: <program> text')
    sys.exit()

if len(sys.argv[1]) % 4 != 0:
    # print len(sys.argv[1])
    print(Fore.RED+"[-]"+Fore.RESET+" Metnin (kodun) 4 katı olmalıdır.")
    sys.exit()
print(Fore.BLUE+'[i]'+Fore.RESET+' Shellcode oluşturma...')
chunks = map(lambda x: sys.argv[1][x:x+4], range(0, len(sys.argv[1]), 4))[::-1]
map(print_word, chunks)
