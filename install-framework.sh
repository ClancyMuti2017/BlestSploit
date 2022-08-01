COMMAND="$(cat src/install/scripts.yml)"
$COMMAND
cat src/install/banner.txt
mkdir logs
mkdir cache
sleep 1
mkdir /usr/share/blest-framework
mkdir /usr/share/blest-framework/devices
mkdir /usr/share/blest-framework/devices/USB
echo ""
echo "[i] Python Kontrol etiliyor ve yükleniyor (Python3)..."
apt install python-is-python3 python3-pip -y &>> cache/apt-log.log
apt install python2 -y &>> cache/apt-log.log
mkdir /usr/share/blest-framework/files
mkdir /usr/share/blest-framework/src
echo "[i] Dosyalar kopyalanıyor... (/usr/share/blest-framework)"
cp -r logs /usr/share/blest-framework/files
cp -r cache /usr/share/blest-framework/files
mkdir /var/log/blestsploit
# mkdir /usr/share/blest-framework/db.old
mkdir /usr/var/blestsploit.old
echo "[i] PIP (Python3) Paketleri Yükleniyor (Uzun sürebilir)..."
bash src/install/pip-install.sh
echo "[i] Depodan Datalar İndiriliyor (Uzun sürebilir, WiFi Hızından asılı)..."
touch /usr/share/blest-framework/config.yml
touch /usr/share/blest-framework/files/logs/blestsploit.log
mkdir /usr/share/blest-framework/network
mkdir /usr/share/blest-framework/network/registry
touch /usr/share/blest-framework/network/registry/hci.ini
touch /usr/share/blest-framework/network/registry/wlan.ini
touch /usr/share/blest-framework/network/registry/config.ini
echo "[settings]" >> /usr/share/blest-framework/network/registry/hci.ini
echo "device = hci0" >> /usr/share/blest-framework/network/registry/hci.ini
echo "[settings]" >> /usr/share/blest-framework/network/registry/wlan.ini
echo "device = wlan0" >> /usr/share/blest-framework/network/registry/wlan.ini
mkdir /usr/share/blest-framework/.update
mkdir /usr/share/blest-framework/.install
git clone https://github.com/G00Dway/BlestSploit /usr/share/blest-framework/src/data &>> /usr/share/blest-framework/files/cache/database-download.txt
sleep 1
echo "[i] Datalar kurulumu başarıyla bitti."
echo "[i] Yürütme dosyaları kopyalanıyor..."
cp -r /usr/share/blest-framework/src/data/bin/auth/btconsole /usr/bin
chmod +x /usr/bin/btconsole
mkdir /usr/share/blest-framework/src/modules.old
mkdir /usr/share/blest-framework/src/modules.depr
sleep 3
echo "[i] BlestSploit başarıyla kuruldu! Dosyalar temizleniyor..."
rm -rf /usr/share/blest-framework/src/data/LICENSE
mkdir /root/.btf
rm -rf /usr/share/blest-framework/src/data/*.md
mv /usr/share/blest-framework/src/data/install-framework.sh /usr/share/blest-framework/.install
mv /usr/share/blest-framework/src/data/uninstall-framework.sh /usr/share/blest-framework/.install
sleep 1
cat src/install/banner.txt
echo ""
echo '[i] Bitti, terminalde "btconsole" yazarak BlestSploiti çalıştırabilirsiniz!'
echo "---------------------------------------------------------------------------"
echo "BlestSploit By   : Marcus Walker (Ənvər) veya G00Dway"
echo "Bizim Patronumuz : Fux Walker"
echo "Discordumuz      : https://discord.gg/2qr6U6ggUN"
echo "Krediler gider   : Nemesis, Rotasız, Dilax, Cyrus, Yakuza, Diğerleri..."
echo ""
# /usr/share/blest-framework/src/data/
#\033[1;77m[i] \033[0m
#\033[1;77m[?] \033[0m
#\033[1;32m[+] \033[0m
#\033[1;33m[!] \033[0m
#\033[1;31m[-] \033[0m
#\033[1;34m[*] \033[0m