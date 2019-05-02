l = [1, 2, 3, 4]
print(l)
l.append(55)  # .append oluşturulan listeye ekleme yapar. Burada "55" eklendi
print(l)
l.insert(2, 111)  # .insert komutu listenin istediğimiz bir yerine ekleme yapar. Burada 2. sıraya 111 eklemek istedik
l.append(111)
print(l)
l.remove(111)  # .remove listeden istediğimiz elemanı siler. Burada 111'i seçtik. İki tane olduğunda
# ilk önce kim gelirse onu siler
print(l)
print(l.pop())  # .pop listenin en sonunda ki elemanı çıkartır ve ekrana kimi çıkarttığını yazar
print(l)
print(l.index(55))  # .index listenin içinden hangi elemanı seçtiysek onun kaçıncı sırada olduğunu gösterir
l.append(1)
l2 = [8, 9, 0, 7]
l.extend(l2)  # .extend bu komut ise oluşturulan ikinci bir listeyi ana listemize birleştirmeye yarar
# .append gibi farklı bir liste olarak değil
print(l)
print(l.count(1))  # .count komutu yazdığımız elemanın listenin içerisinde kaç tane olduğunu gösterir
l.sort() # .sort listeyi sıraya sokar
print(l)
l.clear() # .clear komutu listenin içini temizler
print(l)
l3=l2.copy() # .copy listeyi kopyalamaya yarar
l3.append(444)
print(l2)
print(l3)