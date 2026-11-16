import java.util.ArrayList;
import java.util.List;

/**
 * Prosedürel (NOO) yaklaşım - v2
 * Bakım görevi: yeni "Altın" hesap türü eklendi.
 * Sonuç: türe göre dallanan HER fonksiyon tek tek bulunup değiştirilmek zorunda kaldı.
 */
public class BankaSistemi {

    static final int VADESIZ = 1;
    static final int VADELI  = 2;
    static final int ALTIN   = 3;

    static class HesapKaydi {          // yalnızca veri taşıyan yapı (C'deki struct gibi)
        String no;
        int tur;
        double bakiye;
        HesapKaydi(String no, int tur, double bakiye) {
            this.no = no; this.tur = tur; this.bakiye = bakiye;
        }
    }

    static double aylikFaiz(HesapKaydi h) {
        switch (h.tur) {
            case VADESIZ: return 0.0;
            case VADELI:  return h.bakiye * 0.035;
            case ALTIN:   return 0.0;
            default: throw new IllegalArgumentException("Bilinmeyen tur: " + h.tur);
        }
    }

    static double islemUcreti(HesapKaydi h) {
        switch (h.tur) {
            case VADESIZ: return 2.0;
            case VADELI:  return 0.0;
            case ALTIN:   return h.bakiye * 0.001;
            default: throw new IllegalArgumentException("Bilinmeyen tur: " + h.tur);
        }
    }

    static boolean paraCekilebilirMi(HesapKaydi h, double tutar) {
        switch (h.tur) {
            case VADESIZ: return h.bakiye >= tutar;
            case VADELI:  return false;            // vade dolmadan çekilemez
            case ALTIN:   return h.bakiye >= tutar + h.bakiye * 0.001;
            default: throw new IllegalArgumentException("Bilinmeyen tur: " + h.tur);
        }
    }

    static String turAdi(HesapKaydi h) {
        switch (h.tur) {
            case VADESIZ: return "Vadesiz";
            case VADELI:  return "Vadeli";
            case ALTIN:   return "Altin";
            default: return "?";
        }
    }

    public static void main(String[] args) {
        List<HesapKaydi> hesaplar = new ArrayList<>();
        hesaplar.add(new HesapKaydi("TR01", VADESIZ, 1000));
        hesaplar.add(new HesapKaydi("TR02", VADELI, 5000));
        hesaplar.add(new HesapKaydi("TR03", ALTIN, 2000));
        for (HesapKaydi h : hesaplar) {
            System.out.printf("%s %-8s faiz=%.2f ucret=%.2f cekim(500)=%b%n",
                    h.no, turAdi(h), aylikFaiz(h), islemUcreti(h), paraCekilebilirMi(h, 500));
        }
    }
}
