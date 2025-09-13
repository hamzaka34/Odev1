#ÖDEV 1

yas = int(input("Yaşınızı giriniz:" ))
cinsiyet_bilgisi = input("Cinsiyetinizi giriniz: ")
cinsiyet = cinsiyet_bilgisi.lstrip().rstrip().replace("İ", "i").replace("I", "ı").lower()
if cinsiyet == "erkek":
    if yas > 18:
        print("Askere gidebilirsiniz.")
    else:
        print("Askere gidemessiniz. Yaşınız küçük.")
elif cinsiyet == "kadın":
    print("Kadın olduğunuz için askere gidemezsiniz.")
else:
    print("Hatalı cinsiyet girdiniz.")




#ÖDEV 2

gun_bilgisi = input("Gün giriniz: ")
gun = gun_bilgisi.lstrip().rstrip().replace("İ", "i").replace("I", "ı").lower() 
#PAZARTESİ kelimesinde "İ" karakteri olduğu için hata veriyor. Bunu düzeltmek için "İ" karakterini "i" karakterine çevirdim.
#Doğru yazılan ancak boşluk bırakılan günler için lstrip() ve rstrip() metodlarını kullandım.
if gun == "pazartesi" or gun == "salı" or gun == "çarşamba" or gun == "perşembe" or gun == "cuma":
    print("Hafta içi")
elif gun == "cumartesi" or gun == "pazar":
    print("Hafta sonu")
elif gun.isalpha() == False:  #Kullanıcıyı hatalı yazımından dolayı uyarmak için isalpha() metodunu kullandım.
    print("Sadece harf kullanınız.")
else:
    print("Hatalı gün girdiniz.")

