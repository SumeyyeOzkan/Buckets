def solution(N, Q, B, C):
    kovalar =  [] #kovaların tutan dizi
    for kovaEkle in range(0,N):
        kovalar.append([]) #kovaların içine top eklenebilen dizi
    for K in range(0,len(B)): #Topların Kovalara eklenmesi
        # print(B[K])
        # print(kovalar[B[K]])
        kovalar[B[K]].append(C[K]) #B de kovanın içine C de yer alan rengin eklenmesi
        renkler=[]
        herRenginSayisi=[]
        kova=kovalar[B[K]] #eklediğimiz topun kovası
        for j in range(0,len(kova)): #kovadaki toplara bakar
            if kova[j] in renkler: 
                index=renkler.index(kova[j]) #renklerin kaçıncı indekte olduğunu buluruz
                herRenginSayisi[index]+=1 #kovadaki renklerin sayısını arttırır
                if herRenginSayisi[index]==Q: #kovadaki topun renginin sayısı q ya eşit ise K döndür
                    return K
            else:
                renkler.append(kova[j]) 
                herRenginSayisi.append(1) # o an için rengin kaç tane olduğu
        
        #print(B[K])    
    return -1
#return K
#o kovadaki q adet aynı renkte top var mı diye bakılacak
N=3
Q=2
B=[1,2,0,1,1,0,0,1]
C=[0,3,0,2,0,3,0,0]
print(solution(N,Q,B,C))