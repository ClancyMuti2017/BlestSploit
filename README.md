# BlestSploit Framework
BlestSploit Framework, Exploits, Payloads, Posts ve Daha Fazlası gibi yayınlanmış modüllerle bir framework!
# Kurulum / Kaldırma
### Kurulum
```
git clone https://github.com/G00Dway/BlestSploit
cd BlestSploit
bash install-framework.sh
```
### Kaldırma
BlestSploit'i sisteminizden kaldırmak için sadece çalıştırın: `bash uninstall-framework.sh`
# Screenshotlar (V.1.4)
![2022-09-01 (2)](https://user-images.githubusercontent.com/80381071/187851206-b950e4e4-cd19-4de7-a9b2-ba01766897be.png)
# Credits
Krediler gider: `Leatrix`, `Fux Walker`, `Kenn`
# Sorunlar, hatalar
Herhangi bir hata bulduysanız, lütfen bunları şu adrese bildirin: <a href="https://github.com/G00Dway/BlestSploit/issues">Bug Reports, Issues</a>
# Kendi modülü nasıl eklenir?
* İlk olarak, "/usr/share/blest-framework/src/data/core/module/data/" adresine gidin ve "modules.json" adlı bir dosya göreceksiniz, onu favori düzenleyicinizle açın
ardından belirtilen kodu dosyanın sonuna ekleyin
```
"bir say":{
            "author": "Ad",
            "name": "modulun dosya adı ama .py, .sh, ve.s olmasın",
            "prefix": "modulun prefixleri, E.x: -t $1 -p $2", # $1 - AYAR1, $2 - AYAR2, $2-ni $3 etseniz AYAR2 yinede seçilecek AYAR3 olsada
            "options": { # modulun ayarları
                  "AYAR1": ["AYAR HAKKINDA", ""],
                  "AYAR2": ["AYAR HAKKINDA", ""],
                  "AYAR3": ["AYAR HAKKINDA", ""] # sonsuz ayar koyabilirsiniz
            }
 }
 ```
 * ve modülünüzü "/usr/share/blest-framework/src/data/modules/exploits" dizinine eklemeyi unutmayın!
# Başlıklar
* bu arada "blestsploit" gibi başlıklar istiyorsanız "config.ini"deki "official"yi "true" olarak değiştirin, ve "unofficial" ifadesini "false" olarak değiştirin
# Uyarı
BlestSploit ile yaptığınız işlemlerden sorumlu DEĞİLİZ, lütfen bu aracı yalnızca eğitim amaçlı kimi kullanın!
