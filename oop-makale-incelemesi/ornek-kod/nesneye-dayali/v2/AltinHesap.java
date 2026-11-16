/** Bakım görevi: yeni tür, mevcut sınıflara dokunmadan yeni bir alt sınıf olarak eklendi (Açık/Kapalı İlkesi). */
public class AltinHesap extends Hesap {
    private static final double KOMISYON = 0.001;
    public AltinHesap(String no, double bakiye) { super(no, bakiye); }
    @Override public double aylikFaiz() { return 0.0; }
    @Override public double islemUcreti() { return bakiye * KOMISYON; }
    @Override public boolean paraCekilebilirMi(double tutar) { return bakiye >= tutar + islemUcreti(); }
    @Override public String turAdi() { return "Altin"; }
}
