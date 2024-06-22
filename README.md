# YZ Destekli Fiyat Takip Uygulamasi
Veriler arasindaki korelasyonu takip eden bir Python uygulamasi. Ana amaci, kriptoparalar arasindaki korele (birbirini tetikleyen) fiyat hareketlerini yakalamaktir.
Demo kolunda yalnizca STX-BB-1000SATS-ORDI sembollerini takip eder.


## Veritabani Yapisi
![image](https://github.com/BurakDorman/correlation_tracker/assets/47524842/9370388c-b539-41d2-b3d9-3a7ef14fa1c9)


## Kullanimi
Proje dosyalari indirilebilir ve yerel sistemde baslatilabilir. Baslatmadan once config.py duzenlenip gerekli bilgiler (token ve chat_id) saglanmalidir.
Veya Telegram'da https://t.me/dorast_bot ile sohbet baslatmak icin /start komutu kullanilabilir. Devaminda bot, kullaniciyi yonlendirir. 


## Ozellikler
- Ilk tanismada kullanicidan bazi bilgiler isteyip veritabanina kaydetme.
- Daha sonraki etkilesimlerde tanidigi kullaniciya /bvol, /jgroup, /getmi, /tracklist komutlarini sunar.
- Adminlere, User komutlarina ek olarak /add, /remove komutlarini sunar.
- Binance API kullanarak takip listesindeki sembollerin fiyat degisimlerini alir (fetching) ve zaman damgasi (timestamp) vurarak veritabanina kaydeder.
- Kaydedilen fiyat degisimlerini takip eder ve <1m 5%> sartini saglayan yukselislerde send_notification(message, chat_id=GROUP_ID) metodunu cagirir.

  
## Servis Surumunde Gelecek Ozellikler
- Bot komutlarinda EN ve TR dil destegi.
- Bot bildirimlerinde EN ve TR dil destegi.
