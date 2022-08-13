rm -rf /usr/share/blest-framework/db.old &>> /usr/share/blest-framework/files/cache/update.log
rm -rf /var/log/blestsploit &>> /usr/share/blest-framework/files/cache/update.log
mkdir /var/log/blestsploit &>> /usr/share/blest-framework/files/cache/update.log
mv /usr/share/blest-framework/src/data/config.ini /var/log/blestsploit &>> /usr/share/blest-framework/files/cache/update.log
mv /usr/share/blest-framework/src/data /usr/share/blest-framework/db.old &>> /usr/share/blest-framework/files/cache/update.log
git clone https://github.com/G00Dway/BlestSploit /usr/share/blest-framework/src/data &>> /usr/share/blest-framework/files/cache/update.log
rm -rf /usr/bin/btconsole &>> /usr/share/blest-framework/files/cache/update.log
rm -rf /root/.btf &>> /usr/share/blest-framework/files/cache/update.log
rm -rf /usr/share/blest-framework/src/data/config.ini &>> /usr/share/blest-framework/files/cache/update.log
mv /var/log/blestsploit/config.ini /usr/share/blest-framework/src/data &>> /usr/share/blest-framework/files/cache/update.log
mkdir /root/.btf &>> /usr/share/blest-framework/files/cache/update.log
cp -r /usr/share/blest-framework/src/data/bin/auth/btconsole /usr/bin &>> /usr/share/blest-framework/files/cache/update.log
chmod +x /usr/bin/btconsole &>> /usr/share/blest-framework/files/cache/update.log
bash /usr/share/blest-framework/src/data/src/install/pip-install.sh &>> /usr/share/blest-framework/files/cache/update.log
# echo -e "\033[1;77m[i] \033[0mDosyalar temizleniyor..."
rm -rf /usr/share/blest-framework/src/data/install-framework.sh /usr/share/blest-framework/src/data/uninstall-framework.sh /usr/share/blest-framework/src/data/LICENSE /usr/share/blest-framework/src/data/*.md &>> /usr/share/blest-framework/files/cache/update.log
sleep 1