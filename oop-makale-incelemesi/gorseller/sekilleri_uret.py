import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import sys
out = sys.argv[1]
plt.rcParams["font.family"] = "DejaVu Sans"
INK="#1f2937"; BLUE="#dbeafe"; BLUEB="#2563eb"; GRAY="#f3f4f6"; GREEN="#dcfce7"; GREENB="#16a34a"; ORANGE="#ffedd5"; ORANGEB="#ea580c"

def box(ax,x,y,w,h,text,fc=BLUE,ec=BLUEB,fs=10,bold=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.08",fc=fc,ec=ec,lw=1.4))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=fs,color=INK,fontweight="bold" if bold else "normal",wrap=True)
def arrow(ax,x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=14,color=INK,lw=1.3))

# 1) Yöntem akışı
fig,ax=plt.subplots(figsize=(10,5.2)); ax.set_xlim(0,10); ax.set_ylim(0,5.2); ax.axis("off")
box(ax,0.2,3.6,2.6,1.1,"Kore'de büyük bir kredi\nkartı şirketi: görev-kritik\nkredi onay sistemi",GRAY,"#6b7280")
box(ax,3.6,4.2,2.8,0.8,"OO sürüm: C++, UML + UP\n6 profesyonel",GREEN,GREENB)
box(ax,3.6,3.0,2.8,0.8,"NOO sürüm: C + TAL, yapısal\n6 profesyonel",ORANGE,ORANGEB)
arrow(ax,2.8,4.15,3.6,4.6); arrow(ax,2.8,4.15,3.6,3.4)
box(ax,7.2,3.5,2.6,1.1,"Aynı gerçek değişiklik\ntalebi: Kredi Limiti\nBirleştirme (CLI)\n488 CR'den rastgele",GRAY,"#6b7280")
arrow(ax,6.4,4.6,7.2,4.1); arrow(ax,6.4,3.4,7.2,3.9)
box(ax,7.2,1.2,2.6,1.3,"Bağımlı değişkenler\n• Efor (kişi-dakika)\n• Değişiklik hacmi\n(6 evrenin her birinde)",BLUE,BLUEB,9)
box(ax,3.6,1.2,2.8,1.3,"Veri doğrulama\nGörüşmeler, grup\ntoplantıları, gözden\ngeçirme/denetimler",BLUE,BLUEB,9)
box(ax,0.2,1.2,3.0,1.3,"Karşılaştırma\nEvre bazında betimsel\ntablolar + nitel\ngözlemler",BLUE,BLUEB,9)
arrow(ax,8.5,3.5,8.5,2.5); arrow(ax,7.2,1.85,6.4,1.85); arrow(ax,3.6,1.85,3.2,1.85)
fig.savefig(f"{out}/sekil1_yontem_akisi.png",dpi=200,bbox_inches="tight"); plt.close(fig)

# 2) Zaman çizelgesi
events=[(1995,"ISO/IEC 12207\nbakımın tanımı"),(1996,"Daly vd.\n3 kalıtım düzeyi → daha hızlı"),
        (1997,"Briand vd.\nOO vs yapısal tasarım belgeleri"),(1998,"Cartwright\nreplikasyon: ters sonuç"),
        (2000,"Harrison vd.\n0/3/5 düzey: düz olan kolay"),(2003,"Prechelt vd.\nderinlik ↑ → süre ↑"),
        (2004,"Deligiannis vd.\n'god class' sezgiseli"),(2005,"Lim, Jeong & Schach\ngerçek görev-kritik sistem"),
        (2005,"Freeman & Schach\netki göreve bağlı")]
fig,ax=plt.subplots(figsize=(11,4.4)); ax.set_xlim(1992,2008.5); ax.set_ylim(-3.6,3.6); ax.axis("off")
ax.plot([1993,2007.5],[0,0],color=INK,lw=2)
levels=[1.3,-1.3,2.5,-2.6,1.3,-1.3,2.5,-2.6,1.3]
xs=[1994.2,1995.8,1997.2,1998.4,2000.0,2002.0,2003.6,2005.2,2006.4]
for i,((y,t),lvl,xt) in enumerate(zip(events,levels,xs)):
    up = 1 if lvl>0 else -1
    hi = "Lim" in t
    c = ORANGEB if hi else BLUEB
    ax.plot([y,xt],[0,lvl],color=c,lw=1.1)
    ax.scatter([y],[0],s=140 if hi else 60,color=c,zorder=3)
    ax.text(xt,lvl,f"{int(y)}\n{t}" if up>0 else f"{t}\n{int(y)}",ha="center",va="bottom" if up>0 else "top",fontsize=8,
            color=INK,fontweight="bold" if hi else "normal",bbox=dict(boxstyle="round,pad=0.25",fc=ORANGE if hi else "white",ec=ORANGEB if hi else "#d1d5db"))

fig.savefig(f"{out}/sekil3_zaman_cizelgesi.png",dpi=200,bbox_inches="tight"); plt.close(fig)

# 3) UML sınıf diyagramı
def cls(ax,x,y,w,name,attrs,ops,hi=False,abstract=False):
    lh=0.28; h=lh*(1+len(attrs)+len(ops))+0.25
    fc=ORANGE if hi else "white"; ec=ORANGEB if hi else INK
    ax.add_patch(plt.Rectangle((x,y-h),w,h,fc=fc,ec=ec,lw=1.3))
    ax.text(x+w/2,y-lh*0.6,("«abstract» " if abstract else "")+name,ha="center",va="center",fontsize=9,fontweight="bold",style="italic" if abstract else "normal")
    yy=y-lh; ax.plot([x,x+w],[yy,yy],color=ec,lw=1)
    for a in attrs: yy-=lh; ax.text(x+0.08,yy+0.06,a,fontsize=8,va="center",family="DejaVu Sans Mono")
    yy-=0.12; ax.plot([x,x+w],[yy,yy],color=ec,lw=1)
    for o in ops: yy-=lh; ax.text(x+0.08,yy+0.08,o,fontsize=8,va="center",family="DejaVu Sans Mono",style="italic" if abstract and "getNo" not in o else "normal")
    return (x,y-h,w,h)
fig,ax=plt.subplots(figsize=(10,6)); ax.set_xlim(0,10); ax.set_ylim(0,6.4); ax.axis("off")
cls(ax,0.2,6.2,2.4,"BankaSistemi",[],["+main(args)"])
ax.annotate("",xy=(3.6,5.6),xytext=(2.6,5.85),arrowprops=dict(arrowstyle="->",ls="--",color=INK))
ax.text(2.7,6.0,"kullanır",fontsize=8)
p=cls(ax,3.6,6.2,3.4,"Hesap",["- no : String","# bakiye : double"],["+ getNo() : String","+ aylikFaiz() : double","+ islemUcreti() : double","+ paraCekilebilirMi(t) : bool","+ turAdi() : String"],abstract=True)
subs=[(0.4,"VadesizHesap",False),(3.7,"VadeliHesap",False),(7.0,"AltinHesap  (v2 - yeni)",True)]
for x,n,h in subs:
    cls(ax,x,2.5,2.9,n,[],["+ aylikFaiz()","+ islemUcreti()","+ paraCekilebilirMi(t)","+ turAdi()"],hi=h)
    ax.annotate("",xy=(5.3,p[1]),xytext=(x+1.45,2.5),arrowprops=dict(arrowstyle="-|>",color=INK,lw=1.2,mutation_scale=16,fc="white"))
fig.savefig(f"{out}/sekil4_uml_sinif.png",dpi=200,bbox_inches="tight"); plt.close(fig)

# 4) Değişiklik karşılaştırması
import numpy as np
labels=["Değiştirilen\nmevcut dosya","Mevcut kodda\ndeğişiklik noktası","Eklenen yeni\ndosya"]
proc=[1,6,0]; oo=[1,1,1]
x=np.arange(3); w=0.36
fig,ax=plt.subplots(figsize=(7.5,3.8))
b1=ax.bar(x-w/2,proc,w,label="Prosedürel (NOO)",color="#f97316")
b2=ax.bar(x+w/2,oo,w,label="Nesneye dayalı (OO)",color="#2563eb")
for b in list(b1)+list(b2): ax.text(b.get_x()+b.get_width()/2,b.get_height()+0.08,str(int(b.get_height())),ha="center",fontsize=9)
ax.set_xticks(x); ax.set_xticklabels(labels,fontsize=9); ax.set_ylim(0,7.2)
for s in ["top","right"]: ax.spines[s].set_visible(False)
ax.legend(frameon=False,fontsize=9); ax.set_ylabel("Adet",fontsize=9)
fig.savefig(f"{out}/sekil5_ornek_degisiklik.png",dpi=200,bbox_inches="tight"); plt.close(fig)

phases=["Gereksinim","Analiz ve\ntasarım","Gerçekleştirme","Test","Dağıtım"]
noo=[240,1020,660,1103,30]; oo=[260,310,215,182,17]
x=np.arange(5); w=0.38
fig,ax=plt.subplots(figsize=(8,4))
b1=ax.bar(x-w/2,noo,w,label="NOO (C/TAL) – toplam 3.053",color="#f97316")
b2=ax.bar(x+w/2,oo,w,label="OO (C++) – toplam 984",color="#2563eb")
for b in list(b1)+list(b2): ax.text(b.get_x()+b.get_width()/2,b.get_height()+15,f"{int(b.get_height()):,}".replace(",","."),ha="center",fontsize=8.5)
ax.set_xticks(x); ax.set_xticklabels(phases,fontsize=9); ax.set_ylabel("Efor (kişi-dakika)",fontsize=9)
for sp in ["top","right"]: ax.spines[sp].set_visible(False)
ax.legend(frameon=False,fontsize=9)
fig.savefig(f"{out}/sekil2_efor_evre.png",dpi=200,bbox_inches="tight"); plt.close(fig)
print("ok")
