# Makale İncelemesi – Nesneye Dayalı Paradigma ve Bakım Edilebilirlik

**Ders:** Nesneye Dayalı Programlama – Proje Ödevi, Seçenek B (Akademik Makale İncelemesi)
**Hazırlayan:** _Ad Soyad – Öğrenci No_

## İncelenen makale
Lim, J. S., Jeong, S. R., & Schach, S. R. (2005). *An empirical investigation of the impact of the object-oriented paradigm on the maintainability of real-world mission-critical software.* The Journal of Systems and Software, 77(2), 131–138. https://doi.org/10.1016/j.jss.2004.11.004

## Kısa özet
Makale, bir kredi kartı şirketinin görev-kritik kredi onay sisteminin aynı işlevi gören iki sürümünü (C++ ile OO ve C/TAL ile yapısal) gerçek bir değişiklik talebi üzerinden 12 profesyonelle karşılaştırır. OO grubu toplamda yaklaşık 984 kişi-dakika, NOO grubu ise 3.053 kişi-dakika efor harcamıştır. Buna karşılık OO sürümde dosya sayısı artmış ve performans düşmüştür. Raporda bu bulgular NDP kavramlarıyla (kapsülleme, soyutlama, çok biçimlilik, SOLID) ilişkilendirilmiş, alanın gelişimi makalenin temel kaynakları üzerinden özetlenmiş ve geliştirme önerileri sunulmuştur.

## Depo yapısı
```
rapor/        Raporun son hali (Word, PDF) ve Markdown sürümü
notlar/       Okuma notları ve temel kaynak özetleri
gorseller/    Rapordaki şekiller ve onları üreten Python betiği
ornek-kod/    Bölüm 5.5'teki Java örneği: prosedürel ve nesneye dayalı (v1 → v2)
```

## Örnek kodu çalıştırma
```bash
cd ornek-kod/nesneye-dayali/v2
javac -d out *.java && java -cp out BankaSistemi
```

## Şekilleri yeniden üretme
```bash
pip install matplotlib numpy
python gorseller/sekilleri_uret.py gorseller
```

> Not: Makalenin tam metni telif hakkı nedeniyle bu depoya eklenmemiştir.
