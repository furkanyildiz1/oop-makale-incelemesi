# Okuma notları – Lim, Jeong & Schach (2005)

## Künye
- JSS 77(2):131–138, DOI 10.1016/j.jss.2004.11.004
- Yazarlar: Sangmyung Üniv., Kookmin Üniv. (Seul), Vanderbilt Üniv. (ABD)

## Soru tablosu
| Soru | Not |
|---|---|
| Araştırma sorusu | Gerçek görev-kritik sistemde OO, bakım eforunu ve değişiklik hacmini nasıl etkiler? |
| Sistem | Kore'de büyük bir kredi kartı şirketi, kredi onay sistemi; günde ~2,5 milyon işlem, ~20 milyon kart sahibi; Tandem Himalaya |
| Sürümler | NOO: C + TAL, yapısal yöntem. OO: C++, UML + UP |
| Katılımcılar | 12 profesyonel, 6 + 6 |
| Görev | 488 CR arasından rastgele seçilen 4. düzey CR: Kredi Limiti Birleştirme (CLI) |
| Bağımlı değişkenler | Efor (kişi-dakika) ve değişiklik hacmi (sayfa, LOC, test, dosya) |
| Veri toplama | Öz kayıt + görüşme + grup toplantısı + walkthrough/inspection |
| İstatistik | Yok, yalnızca betimsel tablolar |
| Ana bulgu | Toplam efor NOO 3.053, OO 984 kişi-dakika (benim hesabım) |
| Sınırlılıklar (yazarlar) | Tek deney, genellenemez; dosya sayısı arttı; OO daha yavaş |

## Evre bazında efor (kişi-dakika)
| Evre | NOO | OO |
|---|---|---|
| Gereksinim | 240 | 260 |
| Analiz ve tasarım | 1.020 | 310 |
| Gerçekleştirme | 660 | 215 |
| Test | 1.103 | 182 |
| Dağıtım | 30 | 17 |

## Eleştirel notlar
- Paradigma tek değişken değil: dil + süreç + belge + test aracı birlikte farklı.
- OO ekibi sistemi yeni yazmıştı (bilgisi taze), NOO ekibi eski kodla çalışıyordu.
- Test evresindeki 6 katlık fark daha çok CppUnit ve otomatik testten kaynaklanıyor olabilir.
- Bir milyon dolarlık donanım maliyeti, bakım kazancıyla birlikte nicel olarak değerlendirilmemiş.
- Bölüm 5'te gruplar karıştırılmış (NOO, NOO ile karşılaştırılmış).
- Katılımcılardan onam alınmamış (etik).
