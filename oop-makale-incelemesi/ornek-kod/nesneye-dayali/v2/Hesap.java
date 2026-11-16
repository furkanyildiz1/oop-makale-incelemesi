/**
 * Nesneye dayalı yaklaşım - soyut üst sınıf.
 * Veri (bakiye) ile ona ait davranış aynı birimde kapsüllenir.
 * Türe özgü kurallar alt sınıflarda (çok biçimlilik) tanımlanır.
 */
public abstract class Hesap {
    private final String no;
    protected double bakiye;

    protected Hesap(String no, double bakiye) {
        this.no = no;
        this.bakiye = bakiye;
    }

    public String getNo() { return no; }

    public abstract double aylikFaiz();
    public abstract double islemUcreti();
    public abstract boolean paraCekilebilirMi(double tutar);
    public abstract String turAdi();
}
