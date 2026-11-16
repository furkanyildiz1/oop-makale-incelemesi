**T.C.**

**SAKARYA ÜNİVERSİTESİ**

**<span class="mark">Ders adı – Nesneye Dayalı Programlama Dilleri</span>**

**PROJE ÖDEVİ – SEÇENEK B: AKADEMİK MAKALE İNCELEMESİ**

*Nesneye Dayalı Paradigmanın Gerçek Dünyadaki Görev-Kritik Yazılımların
Bakım Edilebilirliğine Etkisi Üzerine Bir Makale İncelemesi*

**İncelenen makale:**

Lim, J. S., Jeong, S. R., & Schach, S. R. (2005). An empirical
investigation of the impact of the object-oriented paradigm on the
maintainability of real-world mission-critical software. The Journal of
Systems and Software, 77(2), 131–138.

Hazırlayan: <span class="mark">Ad Soyad</span> –
<span class="mark">Öğrenci No</span>

Ders Sorumlusu: <span class="mark">Unvan Ad Soyad</span>

GitHub:
<span class="mark">https://github.com/kullanici-adi/oop-makale-incelemesi</span>

Kasım 2026

# İçindekiler

1\. Makale Seçimi ve Künye Bilgileri

2\. Makalenin Temel Konusu, Amacı ve Araştırma Soruları

3\. Kullanılan Yöntemin Özeti

4\. Bulguların ve Sonuçların Değerlendirilmesi

5\. Makaledeki Fikirlerin Nesneye Dayalı Programlama Kavramlarıyla
İlişkisi

6\. Temel Kaynaklar Üzerinden Alanın Gelişim Süreci

7\. Kendi Yorumlarım ve Geliştirme Önerileri

8\. Sonuç

Kaynakça

Ek: GitHub Deposu ve Örnek Kod

# 1. Makale Seçimi ve Künye Bilgileri

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Alan</strong></th>
<th><strong>Bilgi</strong></th>
</tr>
<tr class="odd">
<th>Başlık</th>
<th>An empirical investigation of the impact of the object-oriented
paradigm on the maintainability of real-world mission-critical
software</th>
</tr>
<tr class="header">
<th>Yazarlar</th>
<th><p>Joa Sang Lim (Sangmyung Üniv., Seul)</p>
<p>Seung Ryul Jeong (Kookmin Üniv., Seul)</p>
<p>Stephen R. Schach (Vanderbilt Üniv., ABD)</p></th>
</tr>
<tr class="odd">
<th>Dergi</th>
<th>The Journal of Systems and Software (Elsevier)</th>
</tr>
<tr class="header">
<th>Cilt / Sayı / Sayfa</th>
<th>77(2), s. 131–138, 2005</th>
</tr>
<tr class="odd">
<th>DOI</th>
<th>10.1016/j.jss.2004.11.004</th>
</tr>
<tr class="header">
<th>Süreç</th>
<th>Geliş: 9 Eylül 2004 – Kabul: 4 Kasım 2004 – Çevrim içi: 18 Aralık
2004</th>
</tr>
<tr class="odd">
<th>İndeks</th>
<th>Science Citation Index (SCI) kapsamında bir dergi</th>
</tr>
<tr class="header">
<th>Erişim</th>
<th>Sakarya Üniversitesi Kütüphanesi – ScienceDirect aboneliği</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Makale, Web of Science (WoS) Smart Search üzerinden aranarak bulunmuş,
tam metnine Sakarya Üniversitesi kütüphanesinin ScienceDirect aboneliği
ile erişilmiştir. Yayımlandığı *The Journal of Systems and Software*
dergisi, yazılım mühendisliği alanında SCI kapsamında taranan köklü
dergilerden biridir. <span class="mark">Buraya WoS arama sonucunun ekran
görüntüsü eklenebilir.</span>

Bu makaleyi seçmemin üç nedeni vardır. Birincisi, nesneye dayalı
programlamanın (NDP) en çok dile getirilen vaadi olan **bakımın
kolaylaşmasını** doğrudan sınamaktadır. İkincisi, literatürdeki
çalışmaların çoğu öğrencilerle ve laboratuvar için yazılmış küçük
programlarla yapılmışken, bu çalışma **gerçek, çalışır durumdaki
görev-kritik bir sistemi** ve **profesyonel geliştiricileri**
incelemektedir. Üçüncüsü, sonuçları yalnızca sayısal değil, UML,
kapsülleme, kod yeniden kullanımı ve global değişkenler gibi ders
kapsamındaki kavramlarla doğrudan ilişkilendirilebilecek nitel gözlemler
de içermektedir.

# 2. Makalenin Temel Konusu, Amacı ve Araştırma Soruları

## 2.1. Temel konu

Makalenin konusu, nesneye dayalı (OO – *object-oriented*) paradigmanın
yazılımın **bakım edilebilirliğine** (*maintainability*) etkisidir.
Yazarlar bakımı ISO/IEC 12207 standardına dayanarak tanımlar: Bir
hatanın düzeltilmesi ya da gereksinimin değişmesi nedeniyle kodda ve
ilgili belgelerde yapılan her değişiklik bakımdır. Bu değişikliğin ürün
teslim edilmeden önce mi sonra mı yapıldığı önemli değildir. Buna göre
bakım edilebilirlik, bir yazılımın bir hatayı düzeltmek ya da değişen
gereksinimlere uymak için ne kadar kolay değiştirilebildiğidir.

## 2.2. Problem ve amaç

Yazarlara göre NDP'nin bakımı kolaylaştırdığı yaygın bir kabul olsa da
bu kabul deneysel olarak doğrulanmamıştır. Mevcut çalışmalar iki açıdan
zayıftır:

- **Çelişkili sonuçlar:** Özellikle kalıtım derinliğinin bakıma etkisi
  konusunda bazı deneyler olumlu, bazıları olumsuz sonuç vermiştir (bkz.
  Bölüm 6).

- **Temsil yeteneği düşük deney ortamları:** Deneylerin büyük çoğunluğu
  öğrencilerle, birkaç yüz ila birkaç bin satırlık, deney için özel
  yazılmış programlarla ve yapay bakım görevleriyle yapılmıştır.
  Katılımcılar deneyde olduklarını bildiği için sonuçlar Hawthorne
  etkisiyle de bozulmuş olabilir.

Makalenin amacı bu boşluğu doldurmaktır. Yazarlar, gerçek bir değişiklik
talebini, aynı işlevi gören iki gerçek sistem sürümü üzerinde,
profesyonel ekiplerin nasıl uyguladığını gözlemlemeyi hedefler. Yazarlar
bu tek deneyin genellenemeyeceğini açıkça kabul eder. Asıl hedeflerinin,
gelecekte farklı araştırmacıların yapacağı benzer saha deneyleriyle
birleştirilebilecek kadar ayrıntılı veri sunmak olduğunu belirtirler.

## 2.3. Araştırma soruları

Makale araştırma sorularını numaralı olarak vermez. Ancak giriş ve
yöntem bölümlerinden şu sorular çıkarılabilir:

1.  **AS1:** Gerçek bir görev-kritik sistemde aynı değişiklik talebini
    uygulamak için OO sürümün bakımı, OO olmayan (NOO) sürüme göre daha
    az **efor** gerektirir mi?

2.  **AS2:** İki sürüm arasında yazılım öğelerindeki (belge, kod, test,
    dosya) **değişiklik hacmi** nasıl farklılaşır?

3.  **AS3:** Bu farklar yazılım yaşam döngüsünün hangi evrelerinde
    (gereksinim, analiz/tasarım, gerçekleştirme, test, dağıtım) ortaya
    çıkar?

4.  **AS4:** Farkların arkasındaki nedenler nelerdir: UML ve belgeleme,
    kapsülleme, yeniden kullanım, global değişkenler, dosya sayısı,
    araçlar?

# 3. Kullanılan Yöntemin Özeti

Çalışma, gerçek bir kurumda yürütülen bir **saha deneyidir** (*field
experiment*). Aynı işlevi gören iki sistem sürümü, iki ayrı profesyonel
ekip tarafından aynı bakım göreviyle değiştirilmiş ve ekiplerin
harcadığı efor ile ürettikleri değişiklik hacmi karşılaştırılmıştır.
Araştırma tasarımı Şekil 1'de özetlenmiştir.

<img src="rapor/media/4b4fe9ac4fa2786a96124da3cad3b56b07ce945b.png"
style="width:6.14583in;height:3.125in" />

*Şekil 1. Lim, Jeong ve Schach (2005) çalışmasının araştırma tasarımı
(makaledeki bilgilere göre tarafımdan çizilmiştir)*

## 3.1. Sistem ve ortam

Deney, Kore'deki büyük bir kredi kartı şirketinin **kredi onay sistemi**
üzerinde yapılmıştır. Şirket 2003 yılında yaklaşık 20 milyon kart
sahibine hizmet vermiş ve günde ortalama 2,5 milyon işlem işlemiştir.
Sistem, hata toleranslı Tandem Himalaya sunucularında (12 CPU)
çalışmaktadır. Eski sistemin yeniden yazılması (*legacy migration*)
sürecinden dolayı aynı işlevi gören iki sürüm aynı anda canlıdadır:

- **NOO sürüm:** Yapısal yöntemlerle geliştirilmiş; C ve TAL (Tandem
  assembler) dilleriyle yazılmış.

- **OO sürüm:** UML ve Unified Process (UP) ile geliştirilmiş; C++ ile
  yazılmış, nesneye dayalı CASE araçları kullanılmış.

## 3.2. Katılımcılar

Toplam 12 bilgi sistemleri profesyoneli katılmıştır. **NOO grubundaki 6
kişi**, eski sistemi yıllardır sürdüren şirket çalışanlarıdır. **OO
grubundaki 6 kişi** ise sistemin C++ ile yeniden yazılma sürecinin
tamamında yer almış kişilerdir. Yazarlar iki grubun ilgili iş alanındaki
uzmanlığının eşdeğer olduğunu varsaymaktadır.

## 3.3. Bakım görevi

Görev, şirketin bilgi teknolojileri planlama biriminde bekleyen **488
değişiklik talebi** (CR) arasından rastgele seçilmiştir. CR'ler gereken
kaynağa göre 1 (en büyük, birkaç kişi-ay) ile 9 (en küçük, birkaç
kişi-gün) arasında sınıflandırılmıştır. Seçilen görev, yaklaşık bir
kişi-ay emek gerektiren 4. düzeyden **Kredi Limiti Birleştirme**
(*Credit Limit Integration*, CLI) talebidir. Bu değişiklikten önce her
müşterinin alışveriş ve nakit avans için ayrı kredi limitleri vardı. CLI
ile bunların yerine tek bir toplam limit getirilmiştir.

## 3.4. Bağımlı değişkenler

Briand vd. (2001) çalışmasındaki bakım edilebilirlik ölçütlerine dayanan
iki bağımlı değişken kullanılmıştır:

- **Efor:** Görevle ilgili öğeleri anlamak, değiştirmek ve test etmek
  için harcanan toplam kişi-dakika (yönetsel efor hariç).

- **Değişiklik hacmi:** Değişen belge sayfası, değiştirilen
  çalıştırılabilir kod satırı (LOC), oluşturulan test durumu, test
  betiği satırı, derlenen ve dağıtılan dosya sayısı.

İki ölçüt de yaşam döngüsünün tüm evrelerinde ayrı ayrı toplanmıştır.
Laboratuvar deneylerinden farklı olarak ekipler değişikliği gerçekten
uygulamak ve hatasız çalışır hale getirmek zorundaydı, çünkü bu canlı
bir sistemdi.

## 3.5. Prosedür ve veri doğrulama

Katılımcılardan, yaptıkları işleri harcadıkları süre ve değiştirdikleri
öğelerle birlikte ayrıntılı olarak kaydetmeleri istenmiştir. Ekiplerin
çalışma süreçlerine müdahale edilmemiş, yalnızca süreç gözlemlenmiştir.
Katılımcılara bir deneyin parçası oldukları **söylenmemiştir**. Yazarlar
bu sayede sonuçların Hawthorne etkisinden arınmış olduğunu öne sürer.
Görev bitince efor kayıtları incelenmiş, abartılı ya da eksik görünen
kayıtlar için görüşmeler yapılmış, tüm paydaşlarla grup toplantıları
düzenlenmiştir. Değişiklik hacmi verileri ise gözden geçirme
(*walkthrough*) ve denetim (*inspection*) oturumlarıyla doğrulanmıştır.

İki grubun kullandığı belgeler de farklıdır (Tablo 1). Bu fark,
sonuçları yorumlarken önemli bir rol oynar.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 37%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Evre</strong></th>
<th><strong>NOO sürüm</strong></th>
<th><strong>OO sürüm</strong></th>
</tr>
<tr class="odd">
<th>Gereksinim</th>
<th><p>Gereksinim belirtimi</p>
<p>Akış şemaları, iş tanımları</p></th>
<th><p>Gereksinim belirtimi</p>
<p>Etkinlik ve kullanım durumu diyagramları</p>
<p>Kullanım durumu açıklamaları</p></th>
</tr>
<tr class="header">
<th>Analiz ve tasarım</th>
<th><p>Fonksiyon listesi</p>
<p>Tasarım belgesi</p>
<p>Üretim listesi</p></th>
<th><p>Sınıf diyagramları</p>
<p>İşlem belirtimleri</p>
<p>Program izlenebilirlik belgesi</p></th>
</tr>
<tr class="odd">
<th>Gerçekleştirme</th>
<th>Kaynak kod</th>
<th>Kaynak kod</th>
</tr>
<tr class="header">
<th>Test</th>
<th>Test durumları</th>
<th>Test durumları</th>
</tr>
<tr class="odd">
<th>Dağıtım</th>
<th>Dağıtım planı</th>
<th>Dağıtım planı</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

*Tablo 1. Evrelere göre kullanılabilen belgeler (makaledeki Tablo 1'den
Türkçeleştirilmiştir)*

# 4. Bulguların ve Sonuçların Değerlendirilmesi

## 4.1. Efor bulguları

Makalenin ana bulgusu, OO grubunun **daha az eforla daha fazla yazılım
öğesi üzerinde değişiklik yapmış** olmasıdır. Makaledeki Tablo 3 ve
Tablo 4'teki efor değerleri Şekil 2'de bir arada gösterilmiştir.
Toplamlar makalede verilmemiştir, tarafımdan hesaplanmıştır. Buna göre
NOO grubu toplam **3.053**, OO grubu ise toplam **984** kişi-dakika
harcamıştır. Bu yaklaşık **3,1 kat** fark demektir.

<img src="rapor/media/f8551e2738b360b7f7e45373b96833b8b0ab3147.png"
style="width:5.625in;height:2.8125in" />

*Şekil 2. Yaşam döngüsü evrelerine göre bakım eforu (veri: makaledeki
Tablo 3 ve 4; grafik tarafımdan çizilmiştir)*

- **Gereksinim:** Bu evrede sonuçlar neredeyse eşittir, OO grubu biraz
  daha fazla efor harcamıştır (260'a karşı 240). OO tarafında UML
  diyagramları da güncellendiği için bu beklenen bir durumdur.

- **Analiz ve tasarım:** NOO grubu üç kattan fazla efor harcamıştır
  (1.020'ye karşı 310). Yazarlar bunu, OO grubunun sınıf diyagramları ve
  ayrıntılı işlem belirtimleri sayesinde **etki analizini** belgeler
  üzerinden yapabilmesine bağlar. NOO grubu ise etki analizi için kaynak
  kodu okumak ve sistem analistleriyle sözlü iletişim kurmak zorunda
  kalmıştır.

- **Gerçekleştirme:** NOO grubunun eforu yaklaşık üç kattır (660'a karşı
  215). Yazarlar NOO grubunun var olan kodu kopyalayıp değiştirme
  (*copy-paste*) yoluna gittiğini, belirsiz gereksinimleri tekrar tekrar
  sözlü olarak netleştirmek zorunda kaldığını ve **yoğun global değişken
  kullanımının** işi zorlaştırdığını gözlemlemiştir.

- **Test:** En büyük fark bu evrededir: NOO grubu yaklaşık **6 kat**
  efor harcamıştır (1.103'e karşı 182). OO grubu C++ için JUnit benzeri
  bir birim test çatısı olan **CppUnit** ile 283 satırlık otomatik test
  betikleri yazmış ve 39 test durumu çalıştırmıştır. NOO grubu ise bir
  simülatörle 15 test durumu çalıştırmış ve test betiği yazmamıştır.

- **Dağıtım:** NOO grubu yaklaşık 2 kat efor harcamıştır (30'a karşı
  17).

## 4.2. Değişiklik hacmi bulguları

| **Ölçüt**                                                   | **NOO**        | **OO**        |
|-------------------------------------------------------------|----------------|---------------|
| Değişen belge sayfası (gereksinim + analiz/tasarım)         | 2              | 11            |
| Değiştirilen çalıştırılabilir LOC (alışveriş / nakit avans) | 182 (51 / 131) | 277 (268 / 9) |
| Değiştirilen dosya                                          | 5              | 11            |
| Test durumu                                                 | 15             | 39            |
| Test betiği (LOC)                                           | yapılmadı      | 283           |
| Derlenen / dağıtılan dosya                                  | 2 / 2          | 6 / 6         |

*Tablo 2. Değişiklik hacmi karşılaştırması (makaledeki Tablo 3 ve 4'ten
derlenmiştir)*

En dikkat çekici sonuç kod satırlarındadır. OO grubu toplamda **daha
fazla** satır değiştirmiştir (277'ye karşı 182). Ancak bu satırların
268'i alışveriş bileşenindedir, nakit avans bileşeninde yalnızca 9 satır
değişmiştir. Yazarlara göre bunun nedeni **yeniden kullanımdır**: OO
sürümde alışveriş bileşeni için yazılan iş mantığı küçük değişikliklerle
nakit avans bileşeninde de kullanılmıştır. NOO sürümde ise iki bileşenin
mantığı birbirinden bağımsız olarak, ikişer kez yazılmıştır (51 ve 131
satır). OO sürümde derlenen ve dağıtılan dosya sayısının üç kat fazla
olması da sınıfların **ince taneli** (*fine-grained*) olmasından
kaynaklanmaktadır.

## 4.3. Performans bulgusu

Makalenin 7. bölümü önemli bir maliyeti ortaya koyar: Çok sayıda
ayarlamaya rağmen OO sürüm, NOO sürümden sürekli olarak **daha yavaş**
çalışmıştır. Şirket bu yüzden ek CPU, disk ve ara katman yazılımı
lisansı için yaklaşık **bir milyon dolar** harcamıştır. Yazarlar bu
kararı, şirketin OO sistemin daha bakım edilebilir olduğuna ve
gelecekteki bakım tasarrufunun bu maliyete değeceğine inandığının kanıtı
olarak yorumlar.

## 4.4. Güçlü yönler

- **Dış geçerlilik:** Gerçek bir sistem, gerçek bir değişiklik talebi ve
  gerçek profesyonellerle çalışılmıştır. Bu, alanda nadir görülen bir
  durumdur.

- **Rastgele görev seçimi:** Görev araştırmacılar tarafından seçilmemiş,
  488 talep arasından rastgele belirlenmiştir. Böylece OO'nun avantajlı
  olacağı bir görevin bilerek seçilmesi önlenmiştir.

- **Tüm yaşam döngüsünün ölçülmesi:** Çoğu deney yalnızca kod
  değişikliğine bakarken bu çalışma gereksinimden dağıtıma kadar tüm
  evreleri ölçmüştür.

- **Şeffaflık:** Yazarlar sonuçların genellenemeyeceğini açıkça
  belirtir, OO sürümün performans zaafını ve dosya sayısındaki artışı
  gizlemez.

## 4.5. Zayıf yönler ve geçerlilik tehditleri

- **Örneklem çok küçük ve istatistiksel test yok:** Tek bir görev ve
  6'ya 6 kişilik iki grup vardır. Sonuçlar yalnızca betimsel tablolarla
  sunulmuştur, hiçbir anlamlılık testi uygulanmamıştır. Bu nedenle
  farkların rastlantısal olup olmadığı bilinemez.

- **Paradigma tek değişken değil:** İki grup arasında dil (C/TAL ve
  C++), süreç (yapısal yöntem ve UP), belgeleme düzeyi (sözlü iletişim
  ve UML artı işlem belirtimleri) ve test aracı (simülatör ve CppUnit)
  aynı anda farklıdır. Yani karşılaştırılan şey yalnızca "OO ile NOO"
  değil, iki ayrı **teknoloji ve süreç paketidir**. Yazarlar da 6.
  bölümde bu farkı kabul eder. Örneğin test evresindeki 6 katlık fark,
  paradigmadan çok otomatik test kültürüyle açıklanabilir.

- **Grupların deneyimi farklı:** OO ekibi sistemi yakın zamanda baştan
  yazmıştı, yani tasarımı tazeydi. NOO ekibi ise yıllardır biriken eski
  bir kod tabanıyla çalışıyordu. Bu da sonuçları OO lehine çarpıtmış
  olabilir.

- **Öz bildirim verisi:** Efor değerleri katılımcıların kendi
  kayıtlarına dayanmaktadır. Yöneticinin görevin önemini vurgulaması ve
  ayrıntılı kayıt istemesi, katılımcılar deneyden habersiz olsa bile
  davranışlarını etkilemiş olabilir.

- **Performans maliyeti hesaba katılmamış:** Bakım edilebilirlik
  kararında bir milyon dolarlık ek donanım maliyeti nicel olarak
  değerlendirilmemiştir. Bu harcamayı "OO daha bakım edilebilirdir"
  sonucunun kanıtı saymak güçlü bir çıkarımdır. Şirket bu kararı geçiş
  sürecinde zaten yapılmış yatırımlar nedeniyle de vermiş olabilir.

- **Etik ve küçük tutarsızlıklar:** Katılımcılara deneyde oldukları
  söylenmemiştir. Bu bugün bilgilendirilmiş onam açısından tartışmalı
  bir uygulamadır. Ayrıca 5. bölümde test durumu karşılaştırmasında
  gruplar karıştırılmıştır: NOO grubunun, NOO grubunun yarısından az
  test çalıştırdığı yazılmıştır. Tablodan ikinci grubun OO olması
  gerektiği anlaşılmaktadır.

# 5. Makaledeki Fikirlerin Nesneye Dayalı Programlama Kavramlarıyla İlişkisi

Makalenin sayısal sonuçlarının arkasındaki nitel gözlemler, NDP'nin
temel kavramlarıyla doğrudan ilişkilendirilebilir.

## 5.1. Kapsülleme ve bilgi gizleme – global değişkenlere karşı

NOO sürümde kart okuma verisi ve paylaşılan sabitler, her bakımcının
erişebildiği **global değişkenlerde** ve harici dosyalarda
tutulmaktadır. Yazarlar bu dosyada yapılan küçük bir hatanın bile ciddi
sonuçlar doğurduğunu belirtir. OO sürümde ise değişkenler sınıfların
içinde **kapsüllenmiş** ve kapalı mimari katmanlara yerleştirilmiştir.
Bu durum, Parnas'ın (1972) bilgi gizleme ilkesinin pratikteki
karşılığıdır. Bir sınıfın iç durumuna yalnızca kendi metotları
erişebildiğinde, değişikliğin etkisi o sınıfın sınırları içinde kalır.
Böylece bakımcının zihninde tutması gereken bilgi azalır. Yazarların
vurguladığı **zihinsel yükün azalması** tam olarak budur.

## 5.2. Soyutlama, arayüzler ve kara kutu yeniden kullanımı

Yazarlar, NOO grubunun Détienne'in (1997) "anlamadan kaçınma"
(*comprehension avoidance*) olarak adlandırdığı stratejiyi izlediğini,
yani kodu anlamak yerine bir şablonu kopyalayıp değiştirdiğini
gözlemlemiştir. Bu da mantığın modüller arasında **çoğalmasına** yol
açmıştır. OO sürümde ise bileşenler dışa açık arayüzlerle
modülerleştirildiği için bakımcıların bileşenlerin içini bilmesi
gerekmemiştir. Bu durum **soyutlama** ilkesinin ve arayüze göre
programlamanın (*program to an interface*) bir sonucudur. Nakit avans
bileşeninde yalnızca 9 satır değişmesi, bu **kara kutu yeniden
kullanımının** (*black-box reuse*) somut bir göstergesidir ve DRY
(*Don't Repeat Yourself*) ilkesiyle örtüşür.

## 5.3. Modülerlik, ince taneli sınıflar ve bağımlılık yönetimi

OO'nun bedeli de makalede açıkça görülmektedir: Derlenen ve dağıtılan
dosya sayısı üç kat artmış, OO ekibi bunun bakım yükünü artırdığını
belirtmiştir. Bu, **Tek Sorumluluk İlkesi** (SRP) gibi SOLID ilkeleri
(Martin, 2003) uygulandıkça sınıf ve dosya sayısının artmasının doğal
bir sonucudur. Bu karmaşıklığı yönetmek için derleme ve bağımlılık
yönetimi araçlarına (bugünkü karşılıkları Maven, Gradle, CMake) ve
**Bağımlılığın Tersine Çevrilmesi İlkesi** (DIP) gibi kurallara ihtiyaç
vardır. Makaledeki performans sorunu da kısmen bu ince taneliliğe, sanal
çağrı ve nesne oluşturma maliyetine bağlanabilir.

## 5.4. UML, UP ve tasarım desenleri

Makaleye göre OO'nun avantajının önemli bir kısmı dilin kendisinden
değil, **UML ile yapılan modellemeden** gelmektedir. Kullanım durumu
diyagramları gereksinimleri, sınıf diyagramları etkilenecek sınıfları,
işlem belirtimleri ise ön koşul, son koşul ve sözde kodla iş mantığını
belgelemiştir. Yazarlar **tasarım desenlerinin** (Gamma vd., 1994)
yaygın kullanıldığını da belirtir. Bu yüzden sıralama (*sequence*)
diyagramlarında çok fazla tekrarlayan işlem görünmüş ve bu diyagramlar
etki analizinde pek işe yaramamıştır. Bu gözlem, desenlerin kodu esnek
kılarken davranışı diyagramlarda izlemeyi zorlaştırabileceğini
göstermektedir.

## 5.5. Kendi örnek uygulamam: Prosedürel ve nesneye dayalı tasarımda bakım

Makalenin bulgularını küçük ölçekte somutlaştırmak için bir bankacılık
senaryosunu Java'da iki biçimde yazdım (GitHub deposunda ornek-kod/
klasörü). Sonra her iki sürümde aynı bakım görevini uyguladım: sisteme
**yeni bir "Altın" hesap türü** eklemek. Prosedürel sürümde hesap türü
bir tamsayı koduyla tutulmakta ve her işlem switch-case ile türe göre
dallanmaktadır:

> static double islemUcreti(HesapKaydi h) {
>
> switch (h.tur) {
>
> case VADESIZ: return 2.0;
>
> case VADELI: return 0.0;
>
> case ALTIN: return h.bakiye \* 0.001; // v2'de eklendi
>
> default: throw new IllegalArgumentException("Bilinmeyen tur");
>
> }
>
> } // aynı değişiklik aylikFaiz, paraCekilebilirMi ve turAdi'nda da
> gerekti

Nesneye dayalı sürümde ise soyut Hesap sınıfı ortak sözleşmeyi tanımlar,
türe özgü kurallar alt sınıflarda **çok biçimlilik** (*polymorphism*)
ile gerçekleştirilir (Şekil 4). Yeni tür, mevcut hiçbir sınıfa
dokunulmadan yeni bir alt sınıf olarak eklenir:

> public class AltinHesap extends Hesap {
>
> private static final double KOMISYON = 0.001;
>
> public AltinHesap(String no, double bakiye) { super(no, bakiye); }
>
> @Override public double aylikFaiz() { return 0.0; }
>
> @Override public double islemUcreti() { return bakiye \* KOMISYON; }
>
> @Override public boolean paraCekilebilirMi(double t) {
>
> return bakiye \>= t + islemUcreti(); }
>
> @Override public String turAdi() { return "Altin"; }
>
> }

<img src="rapor/media/d49ec767d4a7c6f969e8a87ef16f8532e32cedb1.png"
style="width:5.41667in;height:3.28125in" />

*Şekil 4. Nesneye dayalı örneğin UML sınıf diyagramı; turuncu sınıf
bakım görevinde eklenen tek yeni birimdir*

| **Ölçüt (v1 → v2)**                   | **Prosedürel**              | **Nesneye dayalı**         |
|---------------------------------------|-----------------------------|----------------------------|
| Değiştirilen mevcut dosya             | 1                           | 1 (yalnızca istemci main)  |
| Mevcut kodda değişiklik noktası       | 6 (sabit + 4 switch + main) | 1 satır                    |
| Eklenen yeni dosya                    | 0                           | 1 (9 satır)                |
| Değişikliğe kapalı kalan sınıf sayısı | –                           | 3 (Hesap, Vadesiz, Vadeli) |

*Tablo 3. Örnek bakım görevinin değişiklik etkisi (diff ile
ölçülmüştür)*

Bu küçük deney, makaledeki iki bulguyu birlikte yansıtmaktadır.
Birincisi, OO sürümde değişiklik **yerelleşmiştir**. Bu, **Açık/Kapalı
İlkesinin** (OCP) gereğidir: sistem genişlemeye açık, değişikliğe
kapalıdır. Prosedürel sürümde ise türe bağlı her fonksiyonun bulunup
değiştirilmesi gerekir ve birinin unutulması bir hataya yol açar. Bu,
makaledeki NOO grubunun etki analizine harcadığı yüksek eforun küçük
ölçekli bir karşılığıdır. İkincisi, OO sürümde **dosya sayısı
artmıştır**, tıpkı makalede derlenen ve dağıtılan dosya sayısının
artması gibi. Bununla birlikte bu örnek Freeman ve Schach'ın (2005)
uyarısını da doğrular: Görev "yeni bir **işlem** eklemek" olsaydı
(örneğin tüm hesaplara vergiHesapla()), OO sürümde her alt sınıfın
değişmesi gerekirdi, prosedürel sürümde ise tek bir yeni fonksiyon
yeterli olurdu. Yani paradigmanın avantajı **görevin türüne bağlıdır**.

<img src="rapor/media/036b2a0827b4955f24dc4d0c2f2d17be51d7dda8.png"
style="width:4.47917in;height:2.27083in" />

*Şekil 5. Örnek bakım görevinde değişiklik yayılımı*

# 6. Temel Kaynaklar Üzerinden Alanın Gelişim Süreci

Makalenin kaynakçasındaki çalışmalar, NDP ve bakım edilebilirlik
araştırmalarının 1990'ların ortasından 2005'e kadar nasıl geliştiğini
gösterir (Şekil 3). Bu bölümde kaynakçadan seçtiğim dört temel çalışma
incelenmekte, diğerleri ise bağlam için anılmaktadır.

<img src="rapor/media/7a5b3fd5806512abfd928831386cef5d86686375.png"
style="width:6.14583in;height:2.55208in" />

*Şekil 3. Makalenin kaynakçasındaki temel çalışmaların zaman çizelgesi
(tarafımdan hazırlanmıştır)*

## 6.1. Daly vd. (1996) – Kalıtım derinliğinin etkisi

Daly, Brooks, Miller, Roper ve Wood, *Empirical Software Engineering*
dergisinde yayımlanan çalışmalarında kalıtım derinliğinin bakım
edilebilirliğe etkisini, iç replikasyon da içeren bir dizi kontrollü
laboratuvar deneyiyle sınamışlardır. Lim vd.'nin özetine göre bu
deneyler, **üç kalıtım düzeyine** sahip OO yazılımın, kalıtım içermeyen
eşdeğer nesne tabanlı yazılıma göre anlamlı ölçüde **daha kısa sürede**
değiştirilebildiğini göstermiştir. Bu çalışma alandaki ilk sistematik
deneysel girişimlerden biridir. Ancak katılımcıların öğrenci olması ve
programların küçük olması, Lim vd.'nin eleştirdiği tipik sınırlılıkları
taşımaktadır.

## 6.2. Briand, Bunse, Daly ve Differding (1997) – OO ve yapısal tasarım belgeleri

Bu çalışma karşılaştırmayı koddan **tasarım belgeleri** düzeyine
taşımıştır. Yazarlar, OO ve yapısal tasarım belgelerinin anlaşılırlığını
ve değiştirilebilirliğini kontrollü bir deneyle karşılaştırmıştır.
Ayrıca OO tasarımın bu avantajı sağlayabilmesi için iyi tasarım
ilkelerine uyulması gerektiğini ortaya koymuşlardır. Yani OO'nun
avantajı paradigmanın kendisinden çok, **tasarımın kalitesine**
bağlıdır. Ekibin 2001 tarihli devam çalışması, Lim vd.'nin kullandığı
efor ve değişiklik hacmi ölçütlerinin de kaynağıdır. Bu çizgi, Lim
vd.'nin UML ve işlem belirtimlerinin faydasına ilişkin bulgusunun
kuramsal arka planını oluşturur.

## 6.3. Harrison, Counsell ve Nithi (2000) – Çelişkili sonuçlar

Daly vd.'nin olumlu sonucu uzun süre geçerli kalmamıştır. Cartwright'ın
(1998) replikasyonu **ters yönde** bir etki bulmuştur. Harrison vd. ise
*The Journal of Systems and Software* dergisinde 0, 3 ve 5 kalıtım
düzeyine sahip sürümleri karşılaştırmış ve değişikliğin **kalıtım
içermeyen** sürümde daha kolay yapıldığını raporlamıştır. Prechelt vd.
(2003) de kalıtım derinliği arttıkça bazı bakım görevlerinin süresinin
uzadığını göstermiştir. Bu dönem, "OO bakımı kolaylaştırır" iddiasının
basit bir evet ya da hayır sorusu olmadığını ortaya koymuştur.
Deligiannis vd. (2003, 2004) de araştırmanın odağını tek tek tasarım
sezgisellerinin (ör. aşırı sorumluluk yüklenmiş "tanrı sınıf") bakıma
etkisine kaydırmıştır.

## 6.4. Freeman ve Schach (2005) – Görev bağımlılığı

Çelişkiyi uzlaştıran çalışma, Lim vd. ile aynı yıl aynı dergide
yayımlanan ve ortak yazar Schach'ın da içinde olduğu bu makaledir.
Yazarlar, biri kalıtım hiyerarşisi içeren, diğeri düz (*flat*) iki
eşdeğer C++ programıyla üç deney yapmıştır. Bir bakım görevi hiyerarşili
sürümde, ikincisi düz sürümde daha kolay olmuş, üçüncüsünde ise fark
çıkmamıştır. Sonuç, kalıtımın bakıma etkisinin **görevin doğasına
bağlı** olduğudur. Lim vd. bu sonuca dayanarak diğer OO özelliklerinin
(sınıf, nesne, çok biçimlilik, dinamik bağlama) de göreve bağlı etkiler
taşıyabileceğini öne sürmüş ve bu yüzden tek deneylerinin
genellenemeyeceğini vurgulamıştır.

## 6.5. Gelişim sürecinin sentezi

Bu kaynaklar alanın üç aşamadan geçtiğini göstermektedir. İlk aşamada
(yaklaşık 1995–1998) tek bir OO özelliği, çoğunlukla kalıtım,
öğrencilerle ve küçük programlarla sınanmış ve **çelişkili** sonuçlar
elde edilmiştir. İkinci aşamada (1998–2004) deneyler çoğaltılmış,
tasarım belgeleri ve tasarım sezgiselleri de incelenmiş ve etkinin
bağlama bağlı olduğu fark edilmiştir. Üçüncü aşamada (2005) ise bir
yandan **görev bağımlılığı** kuramsal olarak açıklanmış (Freeman ve
Schach), diğer yandan laboratuvar dışına çıkılarak **gerçek sistemlerde
saha çalışmaları** başlamıştır (Lim vd.). İncelediğim makale bu son
aşamanın öncü örneklerindendir. Makalenin vardığı en önemli sonuç da bu
gelişimle uyumludur: Bakım edilebilirliği yalnızca kodun yapısal
özellikleri değil, kullanılan **yöntem, süreç ve araçlar** gibi
bağlamsal etkenler de belirler.

# 7. Kendi Yorumlarım ve Geliştirme Önerileri

## 7.1. Genel değerlendirmem

Bence makalenin en değerli katkısı, NDP'nin bakım üzerindeki etkisini
laboratuvardan gerçek bir kuruma taşıması ve etkinin **tüm yaşam
döngüsüne yayıldığını** göstermesidir. Efor farkının en çok
analiz/tasarım ve test evrelerinde ortaya çıkması dikkat çekicidir. Bu
bana, OO'nun asıl faydasının "sınıf yazmak"tan değil, **iyi belgelenmiş
arayüzler, model tabanlı iletişim ve otomatik testten** geldiğini
düşündürmektedir. Bu yüzden makalenin başlığındaki "paradigma" kelimesi
biraz geniş kalmaktadır. Daha doğru bir başlık, bir "OO teknoloji ve
süreç paketinin" bakıma etkisi olurdu.

Öte yandan makalenin sonuçları bugünkü yazılım mühendisliği
uygulamalarıyla da örtüşmektedir. Global durumdan kaçınmak, kapsülleme,
birim testleri ve tasarım belgeleri modern kod tabanlarında da bakım
edilebilirliğin temel taşlarıdır. Makaledeki performans bulgusu ise bir
uyarıdır: Bakım edilebilirlik ile çalışma zamanı verimliliği arasında
bir **ödünleşim** (*trade-off*) vardır. Bu ödünleşim, karar alınırken
nicel olarak hesaba katılmalıdır.

## 7.2. Geliştirme önerileri

1.  **Birden fazla görev ve tabakalı örnekleme:** Freeman ve Schach'ın
    gösterdiği görev bağımlılığı göz önüne alındığında, tek bir CR
    yerine farklı düzeylerden (ör. 2, 4, 6 ve 8) ve farklı türlerden
    (düzeltici, uyarlayıcı, geliştirici) birden çok CR seçilmelidir.

2.  **İstatistiksel analiz:** Gruplar ve görevler çoğaltılarak
    Mann–Whitney U gibi parametrik olmayan testler ve etki büyüklüğü
    raporlanmalıdır.

3.  **Karıştırıcı etkenlerin ayrıştırılması:** Paradigma, belgeleme
    düzeyi ve test otomasyonu ayrı etkenler olarak ele alınmalıdır.
    Örneğin NOO ekibine de birim test aracı ve ayrıntılı işlem
    belirtimleri verilerek bir faktöriyel tasarım kurulabilir.

4.  **Kalite ve uzun dönem ölçümleri:** Efora ek olarak, değişiklikten
    sonraki birkaç aydaki hata sayısı, regresyonlar ve sonraki
    değişikliklerin maliyeti de izlenmelidir.

5.  **Toplam sahip olma maliyeti:** Bir milyon dolarlık ek donanım gibi
    performans maliyetleri, bakım tasarruflarıyla birlikte aynı finansal
    modelde değerlendirilmelidir.

6.  **Günümüze uyarlanmış bir tekrar:** Bugün aynı soru, açık kaynak
    projelerin git geçmişi üzerinden yazılım deposu madenciliği (MSR)
    ile çok daha büyük ölçekte sınanabilir. Chidamber ve
    Kemerer'in (1994) metrikleri (WMC, DIT, CBO, LCOM) ve SonarQube gibi
    araçların bakım edilebilirlik göstergeleri, değişiklik başına
    dokunulan dosya sayısı ve hata düzeltme süresiyle
    ilişkilendirilebilir.

7.  **Yeni paradigmalar ve araçlar:** Günümüzde saf OO yerine
    fonksiyonel ve OO karışık diller (Kotlin, Scala, TypeScript),
    mikroservis mimarileri ve yapay zekâ destekli kod asistanları
    yaygındır. Bu bağlamlarda kapsülleme ve arayüz tabanlı tasarımın
    bakıma katkısının yeniden ölçülmesi değerli olacaktır.

8.  **Etik:** Katılımcılardan sonradan da olsa bilgilendirilmiş onam
    alınmalı ve bu süreç makalede raporlanmalıdır.

# 8. Sonuç

Lim, Jeong ve Schach (2005), bir kredi kartı şirketinin görev-kritik
kredi onay sisteminin aynı işlevi gören OO ve NOO sürümlerini, gerçek
bir değişiklik talebi üzerinden 12 profesyonelle karşılaştırmıştır. OO
grubu, yaşam döngüsünün hemen her evresinde daha az eforla (toplam
yaklaşık 984'e karşı 3.053 kişi-dakika) daha fazla yazılım öğesini
değiştirmiştir. Yazarlar bunu UML tabanlı etki analizine, kapsüllemeye,
kara kutu yeniden kullanımına ve otomatik teste bağlamıştır. Buna
karşılık OO sürümde dosya sayısı artmış ve performans düşmüştür. Çalışma
tek görev, küçük örneklem ve birbirine karışmış teknoloji farkları
nedeniyle kesin bir genelleme sunmasa da NDP'nin bakım üzerindeki
etkisini gerçek dünyada inceleyen öncü bir saha çalışmasıdır. Kendi
küçük Java deneyim de aynı ödünleşimi göstermiştir: Kapsülleme ve çok
biçimlilik değişikliği yerel tutarken dosya sayısını artırır ve
avantajın büyüklüğü bakım görevinin türüne bağlıdır.

# Kaynakça

Briand, L. C., Bunse, C., Daly, J. W., & Differding, C. (1997). An
experimental comparison of the maintainability of object-oriented and
structured design documents. *Empirical Software Engineering, 2*(3),
291–312.

Briand, L. C., Bunse, C., & Daly, J. (2001). A controlled experiment for
evaluating quality guidelines on the maintainability of object-oriented
designs. *IEEE Transactions on Software Engineering, 27*(6), 513–529.

Cartwright, M. (1998). An empirical view of inheritance. *Information
and Software Technology, 40*(14), 795–799.

Chidamber, S. R., & Kemerer, C. F. (1994). A metrics suite for object
oriented design. *IEEE Transactions on Software Engineering, 20*(6),
476–493.

Daly, J., Brooks, A., Miller, J., Roper, M., & Wood, M. (1996).
Evaluating inheritance depth on the maintainability of object-oriented
software. *Empirical Software Engineering, 1*(2), 109–132.

Deligiannis, I., Shepperd, M., Roumeliotis, M., & Stamelos, I. (2003).
An empirical investigation of an object-oriented design heuristic for
maintainability. *The Journal of Systems and Software, 65*(2), 127–139.

Détienne, F. (1997). Assessing the cognitive consequences of the
object-oriented approach: A survey of empirical research on
object-oriented design by individuals and teams. *Interacting with
Computers, 9*(1), 47–72.

Freeman, G. L., & Schach, S. R. (2005). The task-dependent nature of the
maintenance of object-oriented programs. *The Journal of Systems and
Software, 76*(2), 195–206.

Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design
Patterns: Elements of Reusable Object-Oriented Software.*
Addison-Wesley.

Harrison, R., Counsell, S., & Nithi, R. (2000). Experimental assessment
of the effect of inheritance on the maintainability of object-oriented
systems. *The Journal of Systems and Software, 52*(2–3), 173–179.

ISO/IEC (1995). *ISO/IEC 12207:1995 – Information technology – Software
life cycle processes.* ISO, Geneva.

Lim, J. S., Jeong, S. R., & Schach, S. R. (2005). An empirical
investigation of the impact of the object-oriented paradigm on the
maintainability of real-world mission-critical software. *The Journal of
Systems and Software, 77*(2), 131–138.
https://doi.org/10.1016/j.jss.2004.11.004

Martin, R. C. (2003). *Agile Software Development: Principles, Patterns,
and Practices.* Prentice Hall.

Parnas, D. L. (1972). On the criteria to be used in decomposing systems
into modules. *Communications of the ACM, 15*(12), 1053–1058.

Prechelt, L., Unger, B., Philippsen, M., & Tichy, W. (2003). A
controlled experiment on inheritance depth as a cost factor for code
maintenance. *The Journal of Systems and Software, 65*(2), 115–126.

# Ek: GitHub Deposu ve Örnek Kod

Raporun Markdown sürümü, şekillerin üretildiği betikler, okuma notları
ve Bölüm 5.5'teki Java örneğinin dört sürümü (prosedürel v1/v2, nesneye
dayalı v1/v2) GitHub deposunda yer almaktadır.
Örnekler javac ile derlenip java BankaSistemi komutuyla
çalıştırılabilir.
