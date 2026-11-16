public class VadesizHesap extends Hesap {
    public VadesizHesap(String no, double bakiye) { super(no, bakiye); }
    @Override public double aylikFaiz() { return 0.0; }
    @Override public double islemUcreti() { return 2.0; }
    @Override public boolean paraCekilebilirMi(double tutar) { return bakiye >= tutar; }
    @Override public String turAdi() { return "Vadesiz"; }
}
