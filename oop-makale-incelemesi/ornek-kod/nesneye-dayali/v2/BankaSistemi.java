import java.util.ArrayList;
import java.util.List;

/** İstemci kod yalnızca soyut Hesap tipine bağımlıdır (Bağımlılığın Tersine Çevrilmesi). */
public class BankaSistemi {
    public static void main(String[] args) {
        List<Hesap> hesaplar = new ArrayList<>();
        hesaplar.add(new VadesizHesap("TR01", 1000));
        hesaplar.add(new VadeliHesap("TR02", 5000));
        hesaplar.add(new AltinHesap("TR03", 2000));
        for (Hesap h : hesaplar) {
            System.out.printf("%s %-8s faiz=%.2f ucret=%.2f cekim(500)=%b%n",
                    h.getNo(), h.turAdi(), h.aylikFaiz(), h.islemUcreti(), h.paraCekilebilirMi(500));
        }
    }
}
