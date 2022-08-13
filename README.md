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
# Screenshotlar (V.1.3)
![image](https://user-images.githubusercontent.com/80381071/182795041-580c18f2-f84e-486d-9764-f35093b7ea13.png)
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
            "prefix": "modulun prefixleri, mesalan: -t $1 -p $2", # $1 - AYAR1, $2 - AYAR2, $2-ni $3 etseniz AYAR2 yinede seçilecek AYAR3 olsada
            "options": { # modulun ayarları
                  "AYAR1": ["AYAR HAKKINDA", ""],
                  "AYAR2": ["AYAR HAKKINDA", ""],
                  "AYAR3": ["AYAR HAKKINDA", ""] # sonsuz ayar koyabilirsiniz
            }
 }
 ```
 * ve modülünüzü "/usr/share/best-framework/src/data/modules/exploits" dizinine eklemeyi unutmayın!
# Uyarı
BlestSploit ile yaptığınız işlemlerden sorumlu DEĞİLİZ, lütfen bu aracı yalnızca eğitim amaçlı kimi kullanın!
