# insananalitigi

Craig Starbuck'ın R **peopleanalytics** (v0.1.0) veri paketinin — *The Fundamentals of People Analytics: With Applications in R* kitabına eşlik eden veri setlerinin — **Türkçeleştirilmiş** Python sürümü.

12 veri seti; sütun adları ve kategorik değerler (Evet/Hayır, departmanlar, unvanlar vb.) Türkçeye çevrilmiş olarak `pandas.DataFrame` biçiminde sunulur.

## Kurulum

```bash
pip install insananalitigi-0.1.0-py3-none-any.whl
```

## Kullanım

```python
import insananalitigi as ia

ia.veri_setleri()             # 12 veri setinin adları
df = ia.yukle("calisanlar")
df = ia.calisanlar()          # her veri seti için kısayol fonksiyonu
print(ia.acikla("tutum"))     # Türkçe değişken açıklamaları
hepsi = ia.tumunu_yukle()     # {ad: DataFrame}
```

## Veri setleri

| Türkçe ad | Orijinal ad | Boyut | İçerik |
|---|---|---|---|
| `yan_haklar` | benefits | 1471 × 3 | Hisse opsiyonu, eğitim sayısı |
| `demografi` | demographics | 1470 × 7 | Yaş, mesafe, eğitim, cinsiyet, medeni durum |
| `calisanlar` | employees | 1470 × 36 | Birleşik ana tablo |
| `is_bilgileri` | job | 1470 × 6 | Departman, düzey/unvan, fazla mesai, seyahat |
| `bordro` | payroll | 1470 × 6 | Saatlik/günlük/aylık/yıllık ücret |
| `performans` | performance | 1470 × 3 | Maaş artışı %, performans puanı |
| `onceki_istihdam` | prior_employment | 1470 × 2 | Önceki işveren sayısı |
| `tutum` | sentiment | 1470 × 6 | Ortam/iş/ilişki tatmini, bağlılık, denge |
| `durum` | status | 1470 × 2 | Aktiflik (işten ayrılma) |
| `anket_yanitlari` | survey_responses | 400 × 12 | Likert ölçekli anket maddeleri |
| `kidem` | tenure | 1470 × 6 | İş deneyimi, kurum/görev/yönetici kıdemi, son terfi |
| `devir_egilimleri` | turnover_trends | 3000 × 6 | Unvan, düzey ve uzaktan çalışmaya göre aylık devir oranı |

Tablolar (`anket_yanitlari` ve `devir_egilimleri` hariç) `calisan_id` anahtarıyla birleştirilebilir.

Lisans: MIT (orijinal paketle aynı).
