public class VadeliHesap extends Hesap {
    public VadeliHesap(String no, double bakiye) { super(no, bakiye); }
    @Override public double aylikFaiz() { return bakiye * 0.035; }
    @Override public double islemUcreti() { return 0.0; }
    @Override public boolean paraCekilebilirMi(double tutar) { return false; } // vade dolmadan çekilemez
    @Override public String turAdi() { return "Vadeli"; }
}
