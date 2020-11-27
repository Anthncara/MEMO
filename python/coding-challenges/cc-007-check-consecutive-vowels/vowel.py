def vowel():       # sesli ahrf bulan fonksiyon tanımlıyoruz.
    s = input("Metni Girin : ") # kullanıcıdan bir metin alıyoruz.
    s=s.lower()                 # kullanıcıdan aldığımız metni hepsini küçük harf yapıyoruz.
    sesli_harf = 'aeıioöuü'     # sesli harflari tanımlıyoruz. burada metni küçük harfe dönüştürmeden
                                # büyük sesli harfleri de buraya tanımlayarak problemi çözebiliriz.
    j = 0                       # for döngüsü içindeki i indexi haricinde bir index tanımlıyoruz. 
    sonuc=""                    # istediğimiz sonuc değerini bir değişkene atıyoruz. bunun yerine direk
                                # print ("positive") veya print ("negative") diyerek te problemi çözebiliriz. 
    for i in s:                 # aldığımız metin bir string ifade olduğu ve slicelanabilir bir ifade olduğu 
                                # için liste gibi davranarak for döngüsü oluşturabiliriz.  
        if s[j] in sesli_harf and s[j+1] in sesli_harf:   # bizden ardışık sesli harfler var mı diye istendiği için
                                                          # girilen metin içerisinde indexleme yöntemi ile peşpeşe gelen
                                                          # indexlerin sesli harf olup olmadığını kontrol ediyoruz.
            sonuc="positive"                     
            break                                         # bir tane bile peşpeşe sesli harf bulursak sonucu positive
                                                          # yapıp döngüden çıkıyoruz.
        else:
            j+=1                                          # eğer peşpeşe sesli harf yoksa indexi bir artırıp tekrar döngüye
                                                          # devam ediyoruz. 
            sonuc="negative"                              # listenin sonunda hala peşpeşe sesli harf yoksa sonuc negative oluyor.
    print (sonuc)                                         # sonucu ekrana yazdırıyoruz.
vowel()                                                   # tanımladığımız fonksiyonu çalıştırıyoruz.