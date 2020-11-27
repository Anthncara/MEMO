# en çok oy alanı bulmaya yarayan fonksiyon, eğer alınan oylar eşit ise alfabetik sıraya göre eşit oy alanlardan 
# alfabetik olarak önce gelen seçilmektedir. (Alfabetik sıra yerine iki tane veya üç tane kazanan da ilan edilebilir
# veya random olarak  en çok oyu alanlardan birisi seçilebilir.) yapılan işlemin sonuçlarını görmeniz açısından 
# print ile her aşamayı yazdırmaya çalıştım, normalde bu kadar print işlemine gerek yok ben programın takibi açısından
# bu şekilde yazdım. aslında bize gerekli olan fonksiyon içerisinde en sonda bulunan print satırı ve fonksiyon 
# dışındaki print satırı yeterlidir. lst isimli liste satırı güzel oldu tek bir satırda eşit oy alanları dictionary içinden
# lst listesine ekledim. Normalde bir for döngüsü ile bir kaç satırdan oluşmalıydı ama bu şekilde programcılık açısından 
# daha efektif.


from collections import Counter

def maximum_votes (votes):
    vote_count = Counter(votes)                       
    max_vote = max (vote_count.values())              
    print("oylama sonucu:", vote_count)                   
    print("en çok alınan oy sayısı: ", max_vote)                        
    lst = [i for i in vote_count.keys() if vote_count[i] == max_vote]   
    print("en çok oy alanlar: ", lst)                                  
    print("en çok oy alan:", sorted(lst)[0])                             
    



votes = ['C', 'A', 'B', 'B', 'B', 'B', 'A', 'D', 'B', 'A', 'A', 'A']
print("input :", votes)
maximum_votes(votes)
