cd /usr/share/blest-framework/src/data
echo -e "\033[1;34m[i] \033[0mGüncellemeler kontrol ediliyor..."
BRANCH="main"
LAST_UPDATE=`git show --no-notes --format=format:"%H" $BRANCH | head -n 1`
LAST_COMMIT=`git show --no-notes --format=format:"%H" origin/$BRANCH | head -n 1`

git remote update > /dev/null 2>&1
if [ $LAST_COMMIT != $LAST_UPDATE ]; then
        echo -e "\033[1;34m[i] \033[0mBlestSploit Güncelleniyor... (Bağlantınızı kapatmayın, BlestSploit'i bozabilirsiniz, Ve iyi olduğundan emin olun)"
        bash /usr/share/blest-framework/src/data/src/update/lib/__update__.sh
        echo -e "\033[1;34m[i] \033[0mKaydedilen log'lar: '/usr/share/blest-framework/files/cache/update.log'"
        echo -e "\033[1;34m[i] \033[0mGüncelleme tamamlandı, BlestSploit'i yeniden başlatmanız önerilir."
else
        echo -e "\033[1;32m[+] \033[0mGüncelleme tespit edilmedi, en son sürümü kullanıyorsunuz."
fi