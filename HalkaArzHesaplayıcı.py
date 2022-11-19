import tkinter as tk


arayüz=tk.Tk()
arayüz.title("HALKA ARZ KAZANÇ HESAPLAYICI  (v1.0.0)")
arayüz.geometry("730x700")

lotsayısı = tk.Label(text="LOT SAYISI :")
lotsayısı.place(x=10,y=10)


y=tk.IntVar()
lotsayısıgirişi =tk.Entry(textvariable=y)
lotsayısıgirişi.place(x=100,y=10)


kullanıcısayısı = tk.Label(text="KATILIMCI SAYISI:")
kullanıcısayısı.place(x=300,y=10)


x=tk.IntVar()
kullanıcısayısı =tk.Entry(textvariable=x)
kullanıcısayısı.place(x=420,y=10)


hissefiyatı = tk.Label(text="HİSSE FİYATI:")
hissefiyatı.place(x=10,y=50)


z=tk.DoubleVar()
hissefiyatı =tk.Entry(textvariable=z)
hissefiyatı.place(x=100,y=50)

hesapbaşılotsonuç=tk.Label()
hesapbaşılotsonuç.place(x=180,y=100)

maxtutar=tk.Label(text="YATIRILMASI GEREKEN TUTAR:")
maxtutar.place(x=10,y=130)

maxtutar1=tk.Label()
maxtutar1.place(x=210,y=130)

tutar19=tk.Label(text="YATIRACAĞINIZ TUTAR:")
tutar19.place(x=300,y=50)

p=tk.IntVar()
tutar20=tk.Entry(textvariable=p)
tutar20.place(x=460,y=50)

lotsayısı19=tk.Label(text="LOT ADEDİNİZ:")
lotsayısı19.place(x=320,y=100)

lotsayısı20=tk.Label()
lotsayısı20.place(x=420,y=100)

tavan1=tk.Label(text="1.TAVAN:")
tavan1.place(x=10,y=160)
Tavan1=tk.Label()
Tavan1.place(x=80,y=160)

tavan2=tk.Label(text="2.TAVAN:")
tavan2.place(x=10,y=200)
Tavan2=tk.Label()
Tavan2.place(x=80,y=200)

tavan3=tk.Label(text="3.TAVAN:")
tavan3.place(x=10,y=240)
Tavan3=tk.Label()
Tavan3.place(x=80,y=240)

tavan4=tk.Label(text="4.TAVAN:")
tavan4.place(x=10,y=280)
Tavan4=tk.Label()
Tavan4.place(x=80,y=280)

tavan5=tk.Label(text="5.TAVAN:")
tavan5.place(x=10,y=320)
Tavan5=tk.Label()
Tavan5.place(x=80,y=320)

tavan6=tk.Label(text="6.TAVAN:")
tavan6.place(x=10,y=360)
Tavan6=tk.Label()
Tavan6.place(x=80,y=360)

tavan7=tk.Label(text="7.TAVAN:")
tavan7.place(x=10,y=400)
Tavan7=tk.Label()
Tavan7.place(x=80,y=400)

tavan8=tk.Label(text="8.TAVAN:")
tavan8.place(x=10,y=440)
Tavan8=tk.Label()
Tavan8.place(x=80,y=440)

tavan9=tk.Label(text="9.TAVAN:")
tavan9.place(x=10,y=480)
Tavan9=tk.Label()
Tavan9.place(x=80,y=480)

tavan10=tk.Label(text="10.TAVAN:")
tavan10.place(x=10,y=520)
Tavan10=tk.Label()
Tavan10.place(x=80,y=520)

tpara=tk.Label(text="TOPLAM PARA:")
tpara.place(x=250,y=160)
tpara1=tk.Label()
tpara1.place(x=360,y=160)

tpara=tk.Label(text="TOPLAM PARA:")
tpara.place(x=250,y=200)
tpara2=tk.Label()
tpara2.place(x=360,y=200)

tpara=tk.Label(text="TOPLAM PARA:")
tpara.place(x=250,y=240)
tpara3=tk.Label()
tpara3.place(x=360,y=240)

tpara=tk.Label(text="TOPLAM PARA:")
tpara.place(x=250,y=280)
tpara4=tk.Label()
tpara4.place(x=360,y=280)

tpara=tk.Label(text="TOPLAM PARA:")
tpara.place(x=250,y=320)
tpara5=tk.Label()
tpara5.place(x=360,y=320)
tpara=tk.Label(text="TOPLAM PARA:")

tpara.place(x=250,y=360)
tpara6=tk.Label()
tpara6.place(x=360,y=360)

tpara=tk.Label(text="TOPLAM PARA:")
tpara.place(x=250,y=400)
tpara7=tk.Label()
tpara7.place(x=360,y=400)

tpara=tk.Label(text="TOPLAM PARA:")
tpara.place(x=250,y=440)
tpara8=tk.Label()
tpara8.place(x=360,y=440)

tpara=tk.Label(text="TOPLAM PARA:")
tpara.place(x=250,y=480)
tpara9=tk.Label()
tpara9.place(x=360,y=480)

tpara=tk.Label(text="TOPLAM PARA:")
tpara.place(x=250,y=520)
tpara10=tk.Label()
tpara10.place(x=360,y=520)

kazanc=tk.Label(text="KÂR:")
kazanc.place(x=520,y=160)
kazanc1=tk.Label()
kazanc1.place(x=570,y=160)

kazanc=tk.Label(text="KÂR:")
kazanc.place(x=520,y=200)
kazanc2=tk.Label()
kazanc2.place(x=570,y=200)

kazanc=tk.Label(text="KÂR:")
kazanc.place(x=520,y=240)
kazanc3=tk.Label()
kazanc3.place(x=570,y=240)

kazanc=tk.Label(text="KÂR:")
kazanc.place(x=520,y=280)
kazanc4=tk.Label()
kazanc4.place(x=570,y=280)

kazanc=tk.Label(text="KÂR:")
kazanc.place(x=520,y=320)
kazanc5=tk.Label()
kazanc5.place(x=570,y=320)

kazanc=tk.Label(text="KÂR:")
kazanc.place(x=520,y=360)
kazanc6=tk.Label()
kazanc6.place(x=570,y=360)

kazanc=tk.Label(text="KÂR:")
kazanc.place(x=520,y=400)
kazanc7=tk.Label()
kazanc7.place(x=570,y=400)

kazanc=tk.Label(text="KÂR:")
kazanc.place(x=520,y=440)
kazanc8=tk.Label()
kazanc8.place(x=570,y=440)

kazanc=tk.Label(text="KÂR:")
kazanc.place(x=520,y=480)
kazanc9=tk.Label()
kazanc9.place(x=570,y=480)

kazanc=tk.Label(text="KÂR:")
kazanc.place(x=520,y=520)
kazanc10=tk.Label()
kazanc10.place(x=570,y=520)







def hesapla_komut():
    lot= y.get()
    kullan=x.get()
    fiyat=z.get()
    para=p.get()
    n=para/fiyat
    o=lot/kullan
    h=fiyat*o
    print(h)
    maxtutar1.config(text=h,fg="green")
    print(o)
    hesapbaşılotsonuç.config(text=o,fg="green")
    print(n)
    lotsayısı20.config(text=n,fg="green")
    t1=fiyat*1.1
    t2=t1*1.1
    t3=t2*1.1
    t4=t3*1.1
    t5=t4*1.1
    t6=t5*1.1
    t7=t6*1.1
    t8=t7*1.1
    t9=t8*1.1
    t10=t9*1.1
    print(t1)
    Tavan1.config(text=t1,fg="green")
    print(t2)
    Tavan2.config(text=t2, fg="green")
    print(t3)
    Tavan3.config(text=t3, fg="green")
    print(t4)
    Tavan4.config(text=t4, fg="green")
    print(t5)
    Tavan5.config(text=t5, fg="green")
    print(t6)
    Tavan6.config(text=t6, fg="green")
    print(t7)
    Tavan7.config(text=t7, fg="green")
    print(t8)
    Tavan8.config(text=t8, fg="green")
    print(t9)
    Tavan9.config(text=t9, fg="green")
    print(t10)
    Tavan10.config(text=t10, fg="green")
    top1 = t1 * n
    top2= t2*n
    top3=t3*n
    top4=t4*n
    top5=t5*n
    top6=t6*n
    top7=t7*n
    top8=t8*n
    top9=t9*n
    top10=t10*n

    print(top1)
    tpara1.config(text=top1, fg="green")
    print(top2)
    tpara2.config(text=top2, fg="green")
    print(top3)
    tpara3.config(text=top3, fg="green")
    print(top4)
    tpara4.config(text=top4, fg="green")
    print(top5)
    tpara5.config(text=top5, fg="green")
    print(top6)
    tpara6.config(text=top6, fg="green")
    print(top7)
    tpara7.config(text=top7, fg="green")
    print(top8)
    tpara8.config(text=top8, fg="green")
    print(top9)
    tpara9.config(text=top9, fg="green")
    print(top10)
    tpara10.config(text=top10, fg="green")
    k=top1-para
    k2=top2-para
    k3=top3-para
    k4=top4-para
    k5=top5-para
    k6=top6-para
    k7 =top7-para
    k8 =top8-para
    k9 =top9-para
    k10 =top10-para


    print(k)
    kazanc1.config(text=k,fg="green")
    print(k2)
    kazanc2.config(text=k2, fg="green")
    print(k3)
    kazanc3.config(text=k3, fg="green")
    print(k4)
    kazanc4.config(text=k4, fg="green")
    print(k5)
    kazanc5.config(text=k5, fg="green")
    print(k6)
    kazanc6.config(text=k6, fg="green")
    print(k7)
    kazanc7.config(text=k7, fg="green")
    print(k8)
    kazanc8.config(text=k8, fg="green")
    print(k9)
    kazanc9.config(text=k9, fg="green")
    print(k10)
    kazanc10.config(text=k10, fg="green")

hesapla=tk.Button(text="HESAPLA",command=hesapla_komut)
hesapla.place(x=300,y=70)







hesapbaşılot=tk.Label(text="HESAP BAŞI DÜŞEN LOT:")
hesapbaşılot.place(x=10,y=100)




kartsayısı=tk.Label(text="KART SAYISI:")
kartsayısı.place(x=10,y=613)

m=tk.IntVar()
kartsayısı1=tk.Entry(text=m)
kartsayısı1.place(x=100,y=613)

tavansayısı=tk.Label(text="SATIŞ FİYAT:")
tavansayısı.place(x=10,y=640)
v=tk.DoubleVar()
tavansayısı1=tk.Entry(text=v)
tavansayısı1.place(x=100,y=640)

payoranı=tk.Label(text="KOMİSYON ORANI:")
payoranı.place(x=10,y=586)
kom=tk.IntVar()
payoranı=tk.Entry(text=kom)
payoranı.place(x=130,y=586)

Kazanc=tk.Label(text="KÂR:")
Kazanc.place(x=320,y=600)
Kazanc1=tk.Label()
Kazanc1.place(x=360,y=600)

lotadet1=tk.Label(text="LOT SAYINIZI GİRİNİZ:")
lotadet1.place(x=10,y=559)
ltad=tk.IntVar()
lotadet=tk.Entry(text=ltad)
lotadet.place(x=150,y=559)

topplam1=tk.Label(text="TOPLAM PARA(KOMİSYON VERİLMİŞ):")
topplam1.place(x=320,y=640)
topplam=tk.Label()
topplam.place(x=570,y=640)

kartbası=tk.Label(text="KART BAŞINA VERİLECEK PAY:")
kartbası.place(x=320,y=620)
kartbası1=tk.Label()
kartbası1.place(x=550,y=620)




def hesapla1_komut():
    ksayısı=m.get()
    tsayısı=v.get()
    Lotadet=ltad.get()
    kosayısı = kom.get()
    parra=p.get()
    TRK1=ksayısı*tsayısı*Lotadet-parra*ksayısı
    TRK2=ksayısı*tsayısı*Lotadet
    kar=ksayısı*tsayısı*Lotadet-parra*ksayısı

    kkar=kar*kosayısı
    kkar2=kkar/100
    kkar3=kkar2/ksayısı
    tpar=TRK2-kkar3*ksayısı
    kark=ksayısı*tsayısı*Lotadet-parra*ksayısı-kkar3*ksayısı
    tpar2 = tpar / 100
    tpar3 = tpar2 / ksayısı
    tpar3 = tpar2 / ksayısı




    if kosayısı==0 :
        print(TRK1)
        Kazanc1.config(text=TRK1,fg="green")
        print(TRK2)
        topplam.config(text=TRK2, fg="green")
        print("0")
        kartbası1.config(text=0,fg="green")
    else :
        print(kark)
        Kazanc1.config(text=kark,fg="green")
        print(tpar3)
        topplam.config(text=tpar,fg="green")
        print(kkar3)
        kartbası1.config(text=kkar3,fg="green")











hesapla1=tk.Button(text="HESAPLA",command=hesapla1_komut)
hesapla1.place(x=340,y=550)








arayüz.mainloop()
