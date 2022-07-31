rm -rf /var/log/blestsploit/blestsploit-old &>> /usr/share/blest-framework/files/cache/update.log
mv /usr/share/blest-framework/src/data /var/log/blestsploit/blestsploit-old &>> /usr/share/blest-framework/files/cache/update.log
git clone https://github.com/G00Dway/BlestSploit /usr/share/blest-framework/src/data &>> /usr/share/blest-framework/files/cache/update.log
rm -rf /usr/bin/btconsole
rm -rf /root/.btf
mkdir /root/.btf
cp -r /usr/share/blest-framework/src/data/bin/auth/btconsole /usr/bin
chmod +x /usr/bin/btconsole
bash /usr/share/blest-framework/src/data/src/install/pip-install.sh &>> /usr/share/blest-framework/files/cache/update.log
