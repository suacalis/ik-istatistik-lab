# İK için İstatistik · Etkileşimli Uygulamalar Portalı

İnsan kaynakları yönetimi öğrencileri ve profesyonelleri için, İK verileriyle çalışan **13 etkileşimli, tamamen Türkçe** istatistik uygulaması ve bunları bir araya getiren portal. Kurulum, sunucu ya da programlama bilgisi gerektirmez; saf HTML + CSS + JavaScript ile yazılmıştır ve GitHub Pages üzerinde doğrudan yayımlanabilir.

## Uygulamalar

| No | Uygulama | Modül | Dosya |
|----|----------|-------|-------|
| 01 | Popülasyon ve Örneklem | A · Veri toplama ve betimsel istatistik | `uygulamalar/01-populasyon-orneklem.html` |
| 02 | Örnekleme Yöntemleri ve Yanlılık | A | `uygulamalar/02-orneklem-yontemleri.html` |
| 03 | Kategorik Verileri Keşfet | A | `uygulamalar/03-kategorik-veriler.html` |
| 04 | Sayısal Verileri Keşfet | A | `uygulamalar/04-sayisal-veriler.html` |
| 05 | Çapraz Tablolar ve Simpson Paradoksu | B · İlişkiler ve modelleme | `uygulamalar/05-capraz-tablolar.html` |
| 06 | Dağılımları Karşılaştırma | B | `uygulamalar/06-dagilimlari-karsilastirma.html` |
| 07 | Normal Model ve Ampirik Kural | B | `uygulamalar/07-normal-model.html` |
| 08 | Korelasyon ve Saçılım Grafiği | B | `uygulamalar/08-korelasyon.html` |
| 09 | Regresyon ve Eğri Uydurma | B | `uygulamalar/09-regresyon.html` |
| 10 | Büyük Sayılar Yasası Simülatörü | C · Olasılığın temelleri | `uygulamalar/10-buyuk-sayilar-yasasi.html` |
| 11 | Örnekleme Dağılımı ve Güven Aralığı | D · Çıkarımsal istatistik | `uygulamalar/11-guven-araligi.html` |
| 12 | Merkezi Limit Teoremi ve Student t | D | `uygulamalar/12-merkezi-limit-teoremi.html` |
| 13 | Hipotez Testleri ve Karar Hataları | D | `uygulamalar/13-hipotez-testleri.html` |

## Klasör yapısı

```
istatistik-uygulamalari/
├── index.html            ← portal (Ana Sayfa · Ders Bilgisi · Tüm Uygulamalar · Eğitmen Rehberi)
├── .nojekyll             ← GitHub Pages'in dosyaları olduğu gibi sunması için
├── assets/
│   ├── ortak.css         ← ortak görünüm
│   └── istat.js          ← ortak istatistik kütüphanesi (normal/t dağılımı, kantiller, CSV okuma, SVG dışa aktarma…)
└── uygulamalar/
    └── 01…13-*.html      ← uygulamalar
```

01 ve 13 numaralı uygulamalar tamamen tek dosyalıktır; diğerleri `assets/` klasöründeki ortak dosyaları kullanır.

## GitHub Pages'te yayımlama

1. GitHub'da yeni bir depo oluşturun (ör. `istatistik-uygulamalari`).
2. Bu klasörün **içeriğini** deponun köküne yükleyin (`index.html` kökte olmalı).
   ```bash
   cd istatistik-uygulamalari
   git init && git add . && git commit -m "İK için istatistik uygulamaları portalı"
   git branch -M main
   git remote add origin https://github.com/KULLANICI_ADI/istatistik-uygulamalari.git
   git push -u origin main
   ```
3. Depoda **Settings → Pages → Build and deployment → Source: Deploy from a branch**, dal olarak `main` ve klasör olarak `/ (root)` seçin.
4. Birkaç dakika sonra site `https://KULLANICI_ADI.github.io/istatistik-uygulamalari/` adresinde yayında olur.

Yerel olarak denemek için `index.html` dosyasını tarayıcıda açmanız yeterlidir.

## Veri yükleme

Uygulama 03, 04, 06 ve 09 kendi verinizle de çalışır (CSV; ayırıcı virgül, noktalı virgül veya sekme olabilir). XLSX/XLS dosyaları için ilk kullanımda SheetJS kütüphanesi CDN'den yüklenir; bu yüzden Excel okuma internet bağlantısı gerektirir. Veriler tarayıcıdan dışarı gönderilmez.

## İK vaka çalışmaları ve veriler

Tüm uygulamalar insan kaynakları yönetimi (İKY) alanından senaryolar kullanır. Veriler **öğretim amaçlı kurgusaldır**; gerçek kurum verisi değildir.

| No | İK senaryosu / veri |
|----|---------------------|
| 01 | 500 çalışanlık şirkette performans puanı, yıllık izin kullanım oranı, aylık fazla mesai |
| 02 | 1000 çalışanlık şirkette iş memnuniyeti anketi; departman tabakaları, ekip kümeleri, İK ofisi (kolayda), şikâyetçi çalışanlar (gönüllü yanıt) |
| 03 | Personel yapısı (departman × unvan kademesi), çıkış mülakatları (ayrılma nedeni × kıdem), işe alım kaynakları (kanal × eğitim düzeyi) |
| 04 | 30 açık pozisyonun doldurulma süresi (time-to-fill, gün); dağılım şekillerinde İK örnekleri |
| 05 | Departmanlara göre işten ayrılma (devir hızı); Ankara–İstanbul şube karşılaştırmasında pozisyon tipi (saha/ofis) ile Simpson paradoksu |
| 06 | 150 çalışanlık ücret–performans veri seti (departman, unvan, cinsiyet, ücret, performans, kıdem, eğitim saati, devamsızlık); 96 katılımcılı eğitim programı etkinliği (ön/son test) |
| 07 | Farklı ölçekli testlerden gelen adayları z-puanıyla karşılaştırma; performans primi eşiği |
| 08 | Yetkinlik–performans, bağlılık–ayrılma niyeti, stres–performans (ters U) vb. değişken çiftleri |
| 09 | Deneyim–ücret (eğrisel), mülakat puanı–ilk yıl performansı (ölçüt geçerliği), eğitim saati–satış hedefi gerçekleşme |
| 10 | İş teklifi kabul oranı (Bernoulli) ve vardiyada günlük devamsız çalışan sayısı (kesikli dağılım, E[X] = 2,46) |
| 11 | Bağlılık anketinde memnuniyet oranı (p) ve ücret araştırmasında ortalama ücret (μ) için güven aralıkları |
| 12 | Performans puanı (normal), aylık fazla mesai (sağa çarpık), görev süresi (iki tepeli); küçük pilot uygulamalar için t-dağılımı |
| 13 | Hibrit çalışma tercihi için tek oran z-testi; yeni seçme testinin etkinliği üzerinden I./II. tip hata ve güç |

Kendi kurum verinizle çalışmak için Uygulama 03, 04, 06 ve 09'a CSV/Excel dosyası yükleyebilirsiniz.

## Kaynak ve teşekkür

Bu portal, University of Dayton *MTH 207 Statistics App Portal*'daki uygulamalardan esinlenerek Türkçeye uyarlanmış ve sıfırdan yeniden yazılmıştır. Tüm vaka verileri İKY alanına uyarlanmıştır. Orijinal uygulamalara ek olarak tekrarlı örnekleme karşılaştırması (02), keman grafiği ve özet tablosu (06), aralık olasılığı hesaplayıcısı ve z-puanıyla aday karşılaştırma (07), tahmin aracı (09), örnekleme dağılımı histogramları (10, 11) ve 2×2 karar tablosu ve İK senaryoları (13) gibi özellikler eklenmiştir.

Kişisel bilgilerinizi (ad, kurum, iletişim) eklemek için `index.html` dosyasının sonundaki `<footer>` bölümünü düzenleyebilirsiniz.
