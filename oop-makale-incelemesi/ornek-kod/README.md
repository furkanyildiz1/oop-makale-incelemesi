# Örnek: Prosedürel ve nesneye dayalı tasarımda bakım

**Bakım görevi:** Sisteme yeni bir "Altın" hesap türü eklemek.

| Klasör | Açıklama |
|---|---|
| `prosedurel/v1` | Hesap türü tamsayı kodu, her işlem `switch-case` ile dallanıyor |
| `prosedurel/v2` | Yeni tür için sabit, 4 `switch` bloğu ve `main` değişti (1 dosya, 6 nokta) |
| `nesneye-dayali/v1` | Soyut `Hesap` + `VadesizHesap`, `VadeliHesap` (çok biçimlilik) |
| `nesneye-dayali/v2` | Yalnızca yeni `AltinHesap.java` eklendi + `main`'de 1 satır (Açık/Kapalı İlkesi) |

Farkları görmek için:
```bash
diff prosedurel/v1/BankaSistemi.java prosedurel/v2/BankaSistemi.java
diff -r nesneye-dayali/v1 nesneye-dayali/v2
```

**Ters örnek (görev bağımlılığı):** Görev "tüm hesaplara yeni bir işlem eklemek" olsaydı, OO sürümde her alt sınıfın değişmesi gerekirdi, prosedürel sürümde ise tek bir yeni fonksiyon yeterli olurdu (bkz. Freeman & Schach, 2005).
