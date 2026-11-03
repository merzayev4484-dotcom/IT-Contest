from pathlib import Path
from collections import Counter,deque
from itertools import combinations
import json,random,math
ROOT=Path(__file__).parent
F=[]
def add(name,tag,level,desc,fmt,hint,fn,kind='array'):
 F.append(dict(name=name,tag=tag,level=level,desc=desc,fmt=fmt,hint=hint,fn=fn,kind=kind))
AF='Birinchi qatorda N (1 ≤ N ≤ 60). Ikkinchi qatorda N ta butun son, −30 ≤ Aᵢ ≤ 30. Indekslar 1 dan boshlanadi.'
def arr(name,desc,fn,hint='Massivni bir yoki bir nechta yurish bilan qayta ishlang.',level=1,tag='Massivlar'):
 add(name,tag,level,desc,AF,hint,fn)
arr('Qo‘shni farqlar','Har bir i=1..N−1 uchun Bᵢ=Aᵢ₊₁−Aᵢ ni hosil qiling.',lambda a:[y-x for x,y in zip(a,a[1:])])
arr('Qo‘shni yig‘indilar','Har bir yonma-yon juftlik yig‘indisini B ro‘yxatiga kiriting: Aᵢ+Aᵢ₊₁.',lambda a:[x+y for x,y in zip(a,a[1:])])
arr('Prefiks balansi','B ro‘yxati A massivining barcha prefiks yig‘indilaridan iborat: Bᵢ=A₁+…+Aᵢ.',lambda a:[sum(a[:i]) for i in range(1,len(a)+1)],'Yig‘ilib boruvchi summani saqlang.',2,'Prefiks yig‘indi')
arr('Suffiks balansi','Har bir i=1..N uchun Aᵢ+…+Aₙ ni B ga yozing.',lambda a:[sum(a[i:]) for i in range(len(a))],'Massivni orqadan ko‘rib chiqing.',2,'Prefiks yig‘indi')
arr('Chapdagi rekordlar','Aᵢ o‘zidan oldingi barcha elementlardan qat’iy katta bo‘lsa, Aᵢ ni B ga kiriting. A₁ har doim kiradi.',lambda a:[x for i,x in enumerate(a) if i==0 or x>max(a[:i])])
arr('O‘ngdagi rekordlar','Aᵢ o‘zidan keyingi barcha elementlardan qat’iy katta bo‘lsa, Aᵢ ni B ga kiriting. Oxirgi element har doim kiradi.',lambda a:[x for i,x in enumerate(a) if i==len(a)-1 or x>max(a[i+1:])])
arr('Mahalliy cho‘qqilar','Faqat 2..N−1 indekslar ko‘riladi. Ikkala qo‘shnisidan qat’iy katta Aᵢ qiymatlarni B ga yig‘ing.',lambda a:[a[i] for i in range(1,len(a)-1) if a[i]>a[i-1] and a[i]>a[i+1]])
arr('Mahalliy vodiylar','Faqat ichki elementlardan ikkala qo‘shnisidan qat’iy kichik bo‘lganlarini B ga yozing.',lambda a:[a[i] for i in range(1,len(a)-1) if a[i]<a[i-1] and a[i]<a[i+1]])
arr('Chastotalar xazinasi','A dagi har bir turli qiymat uchun uning takrorlanish sonini B ga bir martadan yozing.',lambda a:list(Counter(a).values()),'Qiymat → chastota jadvalini tuzing.',2,'Sanash')
arr('Takrorlanmagan qiymatlar','A massivida aynan bir marta uchraydigan qiymatlarni B ga yozing.',lambda a:[x for x,c in Counter(a).items() if c==1],tag='Sanash')
arr('O‘suvchi bo‘laklar','A ni maksimal qat’iy o‘suvchi ketma-ket bo‘laklarga ajrating. B shu bo‘laklar uzunliklaridan iborat.',lambda a:run_lengths(a,lambda x,y:y>x),'Aᵢ₊₁>Aᵢ bo‘lsa joriy bo‘lakni uzaytiring.',2)
arr('Tenglar zanjiri','Massivni yonma-yon teng qiymatlarning maksimal bo‘laklariga ajrating; B ga ularning uzunliklarini yozing.',lambda a:run_lengths(a,lambda x,y:y==x))
arr('Juftliklar bozori','Barcha 1≤i<j≤N juftliklar uchun Aᵢ+Aⱼ ni B ga kiriting. Teng natijalar alohida saqlanadi.',lambda a:[x+y for x,y in combinations(a,2)],'Ichma-ich ikki sikl yetadi.',2,'Kombinatorika')
arr('Juftliklar masofasi','Barcha i<j juftliklarning |Aᵢ−Aⱼ| qiymatlarini B ga yozing.',lambda a:[abs(x-y) for x,y in combinations(a,2)],level=2)
arr('Oraliqlar energiyasi','Har bir bo‘sh bo‘lmagan uzluksiz A[L..R] bo‘lagining yig‘indisini B ga kiriting.',lambda a:[sum(a[l:r]) for l in range(len(a)) for r in range(l+1,len(a)+1)],'Prefiks yig‘indi bilan har bir oraliqni O(1) da toping.',2,'Prefiks yig‘indi')
arr('Oraliqlar cho‘qqisi','B dagi qiymatlar A ning barcha bo‘sh bo‘lmagan uzluksiz bo‘laklarining maksimumlaridir.',lambda a:[max(a[l:r]) for l in range(len(a)) for r in range(l+1,len(a)+1)],'Har bir L uchun R ni oshirib, maksimumni yangilang.',2)
arr('Oraliqlar tubi','Har bir bo‘sh bo‘lmagan uzluksiz bo‘lakning minimumini B ga yozing.',lambda a:[min(a[l:r]) for l in range(len(a)) for r in range(l+1,len(a)+1)],level=2)
arr('Chapdagi katta qo‘shnilar','Har bir Aᵢ uchun chap tomonda nechta element undan qat’iy katta ekanini sanang va Bᵢ ga yozing.',lambda a:[sum(x>v for x in a[:i]) for i,v in enumerate(a)],'Har bir indeks uchun oldingi qiymatlarni tekshiring.',2)
arr('O‘ngdagi kichik qo‘shnilar','Bᵢ — i dan keyin keladigan, Aᵢ dan qat’iy kichik elementlar soni.',lambda a:[sum(x<v for x in a[i+1:]) for i,v in enumerate(a)],level=2)
arr('Keyingi kattagacha','Har i uchun eng yaqin j>i va Aⱼ>Aᵢ ni toping. Bᵢ=j−i; bunday j bo‘lmasa Bᵢ=0.',lambda a:[next((j-i for j in range(i+1,len(a)) if a[j]>v),0) for i,v in enumerate(a)],'O‘ngdagi birinchi mos elementni qidiring; stek bilan ham yechish mumkin.',2,'Stek')
arr('Oldingi kichikkacha','Har i uchun eng yaqin j<i va Aⱼ<Aᵢ ni toping. Bᵢ=i−j; topilmasa 0.',lambda a:[next((i-j for j in range(i-1,-1,-1) if a[j]<v),0) for i,v in enumerate(a)],level=2,tag='Stek')
arr('Siljuvchi uchlik','Har bir ketma-ket uch elementning yig‘indisini B ga yozing. N<3 bo‘lsa B bo‘sh.',lambda a:[sum(a[i:i+3]) for i in range(len(a)-2)],tag='Sliding window')
arr('Uchlik medianasi','Har bir uzluksiz uchlikni saralab, o‘rtadagi elementini B ga yozing. N<3 da B bo‘sh.',lambda a:[sorted(a[i:i+3])[1] for i in range(len(a)-2)],tag='Saralash')
arr('Saralangan bo‘shliqlar','A ni o‘sish tartibida saralang. Qo‘shni qiymatlarning farqlarini B ga yozing.',lambda a:[y-x for x,y in zip(sorted(a),sorted(a)[1:])],tag='Saralash')
arr('Simmetrik juftlar','i=1..⌊N/2⌋ uchun Aᵢ+Aₙ₊₁₋ᵢ ni B ga yozing. O‘rtadagi yolg‘iz element olinmaydi.',lambda a:[a[i]+a[-1-i] for i in range(len(a)//2)])
arr('O‘rtachadan og‘ish','S=A₁+…+Aₙ bo‘lsin. Har bir i uchun Bᵢ=N·Aᵢ−S ni hisoblang.',lambda a:[len(a)*x-sum(a) for x in a])
arr('Maksimum soyasi','M=A ning maksimumi. Har bir element uchun Bᵢ=M−Aᵢ ni hosil qiling.',lambda a:[max(a)-x for x in a])
arr('Prefiks EKUB','Bᵢ=EKUB(|A₁|,…,|Aᵢ|). EKUB(0,0)=0 deb oling.',lambda a:[math.gcd(*a[:i]) for i in range(1,len(a)+1)],'g=0 dan boshlang va g=EKUB(g,|Aᵢ|) qiling.',2,'Sonlar nazariyasi')
arr('O‘suvchi yo‘llar','Bᵢ — aynan i-indeksda tugaydigan eng uzun qat’iy o‘suvchi qism ketma-ketlik uzunligi. Indekslar ketma-ket bo‘lishi shart emas.',lambda a:lis_ending(a),'DP[i]=1+max(DP[j]) sharti j<i va Aⱼ<Aᵢ.',3,'Dinamik dasturlash')
arr('Oldingi turli qiymatlar','Bᵢ — A₁..Aᵢ prefiksdagi turli qiymatlar soni.',lambda a:[len(set(a[:i])) for i in range(1,len(a)+1)],tag='To‘plamlar')
# 20 number families
NF='Yagona qatorda N (1 ≤ N ≤ 10000) natural soni beriladi.'
def num(name,desc,fn,hint='Bo‘luvchilar yoki raqamlar ustida sikl tuzing.',level=2):add(name,'Sonlar nazariyasi',level,desc,NF,hint,fn,'number')
num('Bo‘luvchilar sandig‘i','N ning barcha musbat bo‘luvchilarini B ro‘yxatiga kiriting.',lambda n:[d for d in range(1,n+1) if n%d==0])
num('Xos bo‘luvchilar','N dan kichik bo‘lgan barcha musbat bo‘luvchilarni B ga kiriting.',lambda n:[d for d in range(1,n) if n%d==0])
num('Tub ko‘paytuvchilar','N ni tub ko‘paytuvchilarga ajrating. Har bir ko‘paytuvchini takrorlari bilan B ga yozing. N=1 bo‘lsa B bo‘sh.',lambda n:prime_factors(n))
num('Turli tub omillar','N ning turli tub bo‘luvchilarini B ga bir martadan kiriting.',lambda n:sorted(set(prime_factors(n))))
num('Raqamlar safi','N ning o‘nlik yozuvidagi har bir raqam B ro‘yxatining bitta elementidir.',lambda n:list(map(int,str(n))),level=1)
num('Raqamlar farqi','N yozuvidagi yonma-yon raqamlarning o‘ngdagisi minus chapdagisini B ga yozing.',lambda n:[int(y)-int(x) for x,y in zip(str(n),str(n)[1:])],level=1)
num('Tub sonlar yo‘lagi','1 dan N gacha bo‘lgan barcha tub sonlarni B ga kiriting.',lambda n:[k for k in range(2,n+1) if prime(k)],'Eratosfen elagidan foydalanish mumkin.')
num('Kvadratlar yo‘lagi','N dan oshmaydigan barcha musbat to‘liq kvadratlar B ro‘yxatiga kiradi.',lambda n:[i*i for i in range(1,math.isqrt(n)+1)],level=1)
num('Kublar yo‘lagi','N dan oshmaydigan barcha musbat to‘liq kublarni B ga yozing.',lambda n:[i**3 for i in range(1,23) if i**3<=n],level=1)
num('Palindrom sonlar','1..N orasidagi o‘nlik yozuvi ikki tomondan bir xil o‘qiladigan sonlar B ni tashkil qiladi.',lambda n:[i for i in range(1,n+1) if str(i)==str(i)[::-1]])
num('O‘zaro tub bekatlar','1≤k≤N va EKUB(k,N)=1 bo‘lgan barcha k larni B ga kiriting.',lambda n:[k for k in range(1,n+1) if math.gcd(k,n)==1])
num('Ikki darajalari','B ro‘yxatiga 1,2,4,8,… ketma-ketlikning N dan oshmaydigan elementlarini yozing.',lambda n:[1<<i for i in range(n.bit_length())],level=1)
num('Fibonacci bekatlari','F₁=1,F₂=1,Fᵢ=Fᵢ₋₁+Fᵢ₋₂. N dan oshmaydigan barcha Fᵢ ni takrorlari bilan B ga yozing.',lambda n:fibs(n))
num('Ikkilik yozuv bo‘laklari','N ning boshida nol bo‘lmagan ikkilik yozuvini teng bitlarning maksimal bo‘laklariga ajrating. B — bo‘laklar uzunliklari.',lambda n:run_lengths(list(bin(n)[2:]),lambda x,y:x==y))
num('Raqamlar ko‘paytmasi','1..N dagi har bir k uchun uning o‘nlik raqamlari ko‘paytmasini B ga kiriting.',lambda n:[math.prod(map(int,str(k))) for k in range(1,n+1)])
num('Bo‘luvchilar soni jadvali','Har bir k=1..N uchun musbat bo‘luvchilari sonini Bₖ ga yozing.',lambda n:divisor_counts(n),'Har bir d ning barcha karralilariga bittadan qo‘shing.')
num('Eyler jadvali','Har k=1..N uchun Bₖ — 1..k oralig‘ida k bilan o‘zaro tub bo‘lgan sonlar miqdori; B₁=1.',lambda n:totients(n),'Eyler funksiyasini elak yordamida hisoblang.',3)
num('Qoldiqlar spektri','Har d=1..N uchun N ni d ga bo‘lgandagi qoldiqni B ga yozing.',lambda n:[n%d for d in range(1,n+1)],level=1)
num('Butun bo‘linmalar','Har d=1..N uchun ⌊N/d⌋ ni B ga yozing. Takror natijalar saqlanadi.',lambda n:[n//d for d in range(1,n+1)],level=1)
num('Raqamlar yig‘indisi jadvali','Har k=1..N uchun k ning raqamlari yig‘indisini B ga yozing.',lambda n:[sum(map(int,str(k))) for k in range(1,n+1)],level=1)
# 20 string families
SF='Yagona qatorda S satri (1 ≤ |S| ≤ 60) beriladi. Faqat ingliz alifbosining kichik a..z harflari ishlatiladi. Harf kodi: a=1,…,z=26.'
def string(name,desc,fn,hint='Satrni indekslar yoki chastotalar orqali qayta ishlang.',level=2):add(name,'Satrlar',level,desc,SF,hint,fn,'string')
string('Harf kodlari','S dagi har bir harfning 1..26 kodini B ga yozing.',lambda s:[ord(c)-96 for c in s],level=1)
string('Harf chastotalari','B 26 ta sondan iborat: a,b,…,z harflarining S dagi chastotalari. Uchrashmagan harf chastotasi 0.',lambda s:[s.count(chr(97+i)) for i in range(26)],level=1)
string('Harf oralig‘i','Yonma-yon harflarning kodlari ayirmasini B ga yozing: kod(Sᵢ₊₁)−kod(Sᵢ).',lambda s:[ord(y)-ord(x) for x,y in zip(s,s[1:])],level=1)
string('Bir xil harf zanjirlari','S ni bir xil harflarning maksimal ketma-ket bo‘laklariga ajrating. B shu bo‘laklar uzunliklaridir.',lambda s:run_lengths(s,lambda x,y:x==y))
string('Unlilar manzili','a,e,i,o,u harflari unli. Har bir unlining S dagi 1 dan boshlangan indeksini B ga yozing.',lambda s:[i+1 for i,c in enumerate(s) if c in 'aeiou'],level=1)
string('Undoshlar manzili','a,e,i,o,u dan boshqa harflarning S dagi 1 dan boshlangan indekslarini B ga yozing.',lambda s:[i+1 for i,c in enumerate(s) if c not in 'aeiou'],level=1)
string('Prefiksdagi turfa harflar','Bᵢ — S ning dastlabki i ta belgisida uchraydigan turli harflar soni.',lambda s:[len(set(s[:i])) for i in range(1,len(s)+1)])
string('Suffiksdagi turfa harflar','Bᵢ — Sᵢ..Sₙ ichidagi turli harflar miqdori.',lambda s:[len(set(s[i:])) for i in range(len(s))])
string('Palindrom oynalar','S ning har bir bo‘sh bo‘lmagan palindrom qism satri uchun uning uzunligini B ga kiriting. Turli pozitsiyalar alohida sanaladi.',lambda s:[r-l for l in range(len(s)) for r in range(l+1,len(s)+1) if s[l:r]==s[l:r][::-1]],'Har bir markaz atrofida kengaytirish mumkin.',3)
string('Z funksiyasi izlari','Har i=1..|S|−1 (0 asosli indeks) uchun S bilan S[i..] ning eng uzun umumiy prefiksi uzunligini B ga yozing.',lambda s:[lcp(s,s[i:]) for i in range(1,len(s))],'Ikki satrni boshidan taqqoslash yoki Z algoritmi.',3)
string('Prefiks funksiyasi izlari','Har bir bo‘sh bo‘lmagan prefiks uchun uning butun uzunligidan kichik eng uzun teng prefiks-suffiks uzunligini B ga yozing.',lambda s:[max([0]+[k for k in range(1,i) if s[:k]==s[i-k:i]]) for i in range(1,len(s)+1)],'KMP prefiks funksiyasini o‘rganing.',3)
string('Harflar qaytishi','Har bir harfning keyingi uchrashigacha bo‘lgan masofani B ga yozing. Keyingi uchrashish bo‘lmasa 0.',lambda s:[next((j-i for j in range(i+1,len(s)) if s[j]==c),0) for i,c in enumerate(s)])
string('Birinchi manzillar','S da uchragan har bir turli harf uchun uning birinchi uchrashish indeksini (1 asosli) B ga bir marta yozing.',lambda s:[s.index(c)+1 for c in set(s)])
string('Oxirgi manzillar','S da uchragan har bir turli harf uchun uning oxirgi uchrashish indeksini (1 asosli) B ga yozing.',lambda s:[s.rindex(c)+1 for c in set(s)])
string('Harf bloklari kodi','Bir xil qo‘shni harflarni bitta harfga qisqartiring; hosil bo‘lgan harflarning kodlarini B ga yozing.',lambda s:[ord(c)-96 for i,c in enumerate(s) if i==0 or c!=s[i-1]])
string('Alifbo bo‘ylab yugurish','S ni harflar kodi qat’iy o‘suvchi maksimal ketma-ket bo‘laklarga ajrating. B — uzunliklar.',lambda s:run_lengths(s,lambda x,y:y>x))
string('Turli harfli oynalar','Har boshlanish pozitsiyasi uchun takror harfsiz eng uzun uzluksiz bo‘lak uzunligini B ga kiriting.',lambda s:[unique_window(s[i:]) for i in range(len(s))],'To‘plam yoki ikkita ko‘rsatkichdan foydalaning.',3)
string('Prefiks kod yig‘indilari','Har bir bo‘sh bo‘lmagan prefiksdagi harf kodlari yig‘indisini B ga yozing.',lambda s:[sum(ord(c)-96 for c in s[:i]) for i in range(1,len(s)+1)],level=1)
string('Uch harf energiyasi','S ning har bir uzluksiz uch belgili bo‘lagi uchun harf kodlari yig‘indisini B ga yozing. |S|<3 da B bo‘sh.',lambda s:[sum(ord(c)-96 for c in s[i:i+3]) for i in range(len(s)-2)],level=1)
string('Suffikslarning umumiy boshi','Har i<j pozitsiya jufti uchun S[i..] va S[j..] suffikslarning umumiy prefiksi uzunligini B ga yozing.',lambda s:[lcp(s[i:],s[j:]) for i in range(len(s)) for j in range(i+1,len(s))],'Kichik chegaralarda har bir suffiks juftini taqqoslang.',3)
# 15 matrices
MF='Birinchi qatorda N va M (1 ≤ N,M ≤ 12). Keyingi N qatorda M tadan butun son (−20 ≤ Aᵢⱼ ≤ 20). Indekslar 1 asosli.'
def matrix(name,desc,fn,hint='Qator va ustun indekslarini aniq ajrating.',level=2):add(name,'Matritsalar',level,desc,MF,hint,fn,'matrix')
matrix('Qator energiyasi','Har qator elementlari yig‘indisini B ga yozing.',lambda a:[sum(row) for row in a],level=1)
matrix('Ustun energiyasi','Har ustun elementlari yig‘indisini B ga yozing.',lambda a:[sum(col) for col in zip(*a)],level=1)
matrix('Qator cho‘qqilari','Har qatorning maksimumini B ga yozing.',lambda a:[max(row) for row in a],level=1)
matrix('Ustun tubi','Har ustunning minimumini B ga yozing.',lambda a:[min(col) for col in zip(*a)],level=1)
matrix('Kvadrat derazalar','Matritsadagi har bir 2×2 bo‘lakning to‘rt elementi yig‘indisini B ga kiriting. N<2 yoki M<2 bo‘lsa B bo‘sh.',lambda a:[a[i][j]+a[i+1][j]+a[i][j+1]+a[i+1][j+1] for i in range(len(a)-1) for j in range(len(a[0])-1)])
matrix('Gorizontal sakrashlar','Har bir qator ichida o‘ngdagi minus chapdagi qo‘shni element farqini B ga yozing.',lambda a:[row[j+1]-row[j] for row in a for j in range(len(row)-1)])
matrix('Vertikal sakrashlar','Har vertikal qo‘shni juftlik uchun pastdagi minus tepadagi element farqini B ga yozing.',lambda a:[a[i+1][j]-a[i][j] for i in range(len(a)-1) for j in range(len(a[0]))])
matrix('Chegara xazinasi','Eng tashqi qator yoki ustunda turgan har bir elementni B ga aynan bir marta kiriting.',lambda a:[v for i,row in enumerate(a) for j,v in enumerate(row) if i in (0,len(a)-1) or j in (0,len(row)-1)],level=1)
matrix('Markaz xazinasi','Eng tashqi chegara ustida bo‘lmagan barcha elementlar B ga kiradi. Ichki katak bo‘lmasa B bo‘sh.',lambda a:[a[i][j] for i in range(1,len(a)-1) for j in range(1,len(a[0])-1)],level=1)
matrix('Shaxmat oq kataklari','i+j juft bo‘lgan kataklardagi qiymatlarni B ga yozing.',lambda a:[v for i,row in enumerate(a,1) for j,v in enumerate(row,1) if (i+j)%2==0],level=1)
matrix('Diagonal oilalari','Har bir d=i−j diagonal uchun elementlar yig‘indisini B ga bir martadan kiriting.',lambda a:[sum(a[i][j] for i in range(len(a)) for j in range(len(a[0])) if i-j==d) for d in range(1-len(a[0]),len(a))])
matrix('Qator amplitudasi','Har qator uchun maksimum minus minimum qiymatini B ga kiriting.',lambda a:[max(row)-min(row) for row in a],level=1)
matrix('Ustun turfaligi','Har bir ustundagi turli qiymatlar sonini B ga yozing.',lambda a:[len(set(col)) for col in zip(*a)])
matrix('Prefiks to‘rtburchaklari','Har (i,j) katak uchun chap yuqori (1,1)..(i,j) to‘rtburchak yig‘indisini B ga kiriting.',lambda a:[sum(a[x][y] for x in range(i+1) for y in range(j+1)) for i in range(len(a)) for j in range(len(a[0]))],'Ikki o‘lchamli prefiks yig‘indidan foydalaning.',3)
matrix('Mahalliy balandliklar','Katak qiymati mavjud yuqori,past,chap,o‘ng qo‘shnilarining har biridan qat’iy katta bo‘lsa uni B ga kiriting. Yolg‘iz katak ham kiradi.',lambda a:[a[i][j] for i in range(len(a)) for j in range(len(a[0])) if all(a[i][j]>a[x][y] for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0<=x<len(a) and 0<=y<len(a[0]))])
# 15 graph families
GF='Birinchi qatorda N,M (1 ≤ N ≤ 30; 0 ≤ M ≤ N(N−1)/2). Keyingi M qatorda u v — yo‘naltirilmagan qirra. 1 ≤ u,v ≤ N, u≠v. Takror qirralar yo‘q.'
def graph(name,desc,fn,hint='Qo‘shnilik ro‘yxati, BFS yoki DFS dan foydalaning.',level=3):add(name,'Graflar',level,desc,GF,hint,fn,'graph')
graph('Tugun darajalari','Har tugunga tutash qirralar sonini B ga yozing.',lambda g:[len(x) for x in g],level=1)
graph('Bog‘lanish orollari','Har bog‘langan komponentadagi tugunlar sonini B ga bir martadan kiriting.',lambda g:[len(c) for c in components(g)])
graph('Komponenta yo‘llari','Har bog‘langan komponenta ichidagi qirralar sonini B ga yozing.',lambda g:[sum(len(g[v]) for v in c)//2 for c in components(g)])
graph('Birinchi bekatdan','1-tugundan barcha yetib boriladigan tugunlargacha eng qisqa masofalarni B ga yozing. 1-tugun masofasi 0 ham kiradi; yetib bo‘lmaydiganlar kirmaydi.',lambda g:[d for d in bfs(g,0) if d>=0])
graph('Barcha bekatlar orasida','Har bir u<v va o‘zaro yetib boriladigan tugun jufti uchun eng qisqa masofani B ga kiriting.',lambda g:[d for u in range(len(g)) for v,d in enumerate(bfs(g,u)) if v>u and d>=0])
graph('Bekat ekssentrisiteti','Har u uchun o‘zi turgan komponentadagi tugunlargacha eng qisqa masofalar maksimumini B ga yozing. Yolg‘iz tugun uchun 0.',lambda g:[max(bfs(g,u)) for u in range(len(g))])
graph('Ikki qadamli yo‘llar','Har u uchun u dan boshlanuvchi uzunligi 2 bo‘lgan yurishlar sonini B ga yozing. Tugunlarga qayta kirish mumkin.',lambda g:[sum(len(g[v]) for v in adj) for adj in g])
graph('Uchburchak ishtiroki','Har tugun uchun shu tugun qatnashgan turli uchburchaklar sonini B ga yozing.',lambda g:[sum(w in g[v] for v,w in combinations(sorted(adj),2)) for adj in g])
graph('Qirra daraja yig‘indisi','Har qirra (u,v) uchun daraja(u)+daraja(v) ni B ga bir martadan kiriting.',lambda g:[len(g[u])+len(g[v]) for u in range(len(g)) for v in g[u] if u<v])
graph('Qirra daraja farqi','Har qirra uchun ikki uch darajalarining mutlaq farqini B ga yozing.',lambda g:[abs(len(g[u])-len(g[v])) for u in range(len(g)) for v in g[u] if u<v])
graph('Yo‘q qirralar','Har u uchun u bilan bevosita ulanmagan boshqa tugunlar sonini B ga yozing. u ning o‘zi hisobga olinmaydi.',lambda g:[len(g)-1-len(adj) for adj in g],level=1)
graph('Umumiy qo‘shnilar','Har u<v juftlik uchun u va v ning umumiy qo‘shnilari sonini B ga yozing.',lambda g:[len(g[u]&g[v]) for u in range(len(g)) for v in range(u+1,len(g))])
graph('Ko‘prikdagi bo‘linish','Har ko‘prik uchun uni olib tashlaganda avvalgi komponenta ajraladigan ikki qismdan kichigining tugunlar sonini B ga yozing. Ko‘prik bo‘lmagan qirralar kirmaydi.',lambda g:bridge_parts(g),'Kichik chegarada har bir qirrani vaqtincha o‘chirib BFS qiling.')
graph('BFS qatlamlari','1-tugundan yetib boriladigan tugunlarni eng qisqa masofa bo‘yicha qatlamlang. Har mavjud qatlamdagi tugunlar sonini B ga yozing.',lambda g:list(Counter(d for d in bfs(g,0) if d>=0).values()))
graph('Komponenta ortiqchaligi','Har komponenta uchun E−V+1 ni B ga yozing; E uning qirralari, V tugunlari soni.',lambda g:[sum(len(g[v]) for v in c)//2-len(c)+1 for c in components(g)])
# helpers used at generation time
def run_lengths(a,cond):
 if not a:return []
 ans=[1]
 for x,y in zip(a,a[1:]):
  if cond(x,y):ans[-1]+=1
  else:ans.append(1)
 return ans
def lis_ending(a):
 dp=[]
 for i,v in enumerate(a):dp.append(1+max([0]+[dp[j] for j in range(i) if a[j]<v]))
 return dp
def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def prime_factors(n):
 out=[];d=2
 while d*d<=n:
  while n%d==0:out.append(d);n//=d
  d+=1
 if n>1:out.append(n)
 return out
def fibs(n):
 a,b=1,1;out=[]
 while a<=n:out.append(a);a,b=b,a+b
 return out
def divisor_counts(n):
 a=[0]*(n+1)
 for d in range(1,n+1):
  for k in range(d,n+1,d):a[k]+=1
 return a[1:]
def totients(n):
 a=list(range(n+1))
 for p in range(2,n+1):
  if a[p]==p:
   for k in range(p,n+1,p):a[k]-=a[k]//p
 return a[1:]
def lcp(a,b):
 i=0
 while i<min(len(a),len(b)) and a[i]==b[i]:i+=1
 return i
def unique_window(s):
 seen=set()
 for c in s:
  if c in seen:break
  seen.add(c)
 return len(seen)
def bfs(g,s):
 d=[-1]*len(g);d[s]=0;q=deque([s])
 while q:
  u=q.popleft()
  for v in g[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 return d
def components(g):
 seen=set();out=[]
 for s in range(len(g)):
  if s in seen:continue
  comp=[];q=[s];seen.add(s)
  while q:
   u=q.pop();comp.append(u)
   for v in g[u]:
    if v not in seen:seen.add(v);q.append(v)
  out.append(comp)
 return out
def bridge_parts(g):
 ans=[]
 for u in range(len(g)):
  for v in g[u]:
   if v<=u:continue
   old=sum(d>=0 for d in bfs(g,u));gg=[set(x) for x in g];gg[u].remove(v);gg[v].remove(u);new=sum(d>=0 for d in bfs(gg,u))
   if new<old:ans.append(min(new,old-new))
 return ans
# Ten genuinely different final requests, not ten changes of constants.
V=[
 ('juftlar miqdori','B ro‘yxatidagi juft qiymatlar sonini toping. 0 ham juft.',lambda b:sum(x%2==0 for x in b),'Juftlikni x%2==0 orqali tekshiring.'),
 ('toqlar yig‘indisi','B ro‘yxatidagi barcha toq qiymatlar yig‘indisini hisoblang.',lambda b:sum(x for x in b if x%2),'Toq qiymatlarni yig‘ing; manfiy sonlar ham bo‘lishi mumkin.'),
 ('eng katta natija','B ro‘yxatidagi eng katta qiymatni toping. B bo‘sh bo‘lsa 0 chiqaring.',lambda b:max(b,default=0),'Maksimumni birinchi mavjud qiymatdan boshlang.'),
 ('eng kichik natija','B ro‘yxatidagi eng kichik qiymatni toping. B bo‘sh bo‘lsa 0 chiqaring.',lambda b:min(b,default=0),'Minimumni birinchi mavjud qiymatdan boshlang.'),
 ('umumiy balans','B ro‘yxatidagi barcha qiymatlar yig‘indisini hisoblang.',lambda b:sum(b),'Yig‘indi uchun 64 bitli butun turdan foydalaning.'),
 ('eng kichik musbat','B dagi eng kichik musbat qiymatni toping. Bunday qiymat bo‘lmasa 0 chiqaring.',lambda b:min([x for x in b if x>0],default=0),'Musbat qiymat topilganini alohida belgilash qulay.'),
 ('tub qiymatlar','B dagi tub qiymatlarning uchrashishlar sonini toping. 0,1 va manfiy sonlar tub emas.',lambda b:sum(prime(x) for x in b),'d*d≤x bo‘lguncha bo‘luvchilarni tekshiring.'),
 ('kvadrat energiya','B dagi har bir qiymatni kvadratga oshirib, hosil bo‘lgan sonlar yig‘indisini toping.',lambda b:sum(x*x for x in b),'Ko‘paytirishdan oldin qiymatni 64 bitli turga o‘tkazing.'),
 ('turli natijalar','B ro‘yxatidagi har xil qiymatlar sonini toping. Har qiymat bir marta sanaladi.',lambda b:len(set(b)),'To‘plam yoki saralashdan foydalaning.'),
 ('natijalar kengligi','B dagi eng katta va eng kichik qiymat ayirmasini toping. B bo‘sh bo‘lsa 0 chiqaring.',lambda b:max(b)-min(b) if b else 0,'Bir yurishda minimum va maksimumni kuzating.')]
assert len(F)==100,len(F)
rng=random.Random(20261103)
def make_case(kind,idx):
 if kind=='array':
  a=([0] if idx==0 else [-3,0,4,4,-2,7] if idx==1 else [rng.randint(-12,12) for _ in range(rng.randint(4,10))]);return a,str(len(a))+'\n'+' '.join(map(str,a))
 if kind=='number':
  n=[1,24,37,100,128,360][idx];return n,str(n)
 if kind=='string':
  s=['a','abacaba','zzzaabbc','itcontest','abcxyzab','aeeiou'][idx];return s,s
 if kind=='matrix':
  a=([[0]] if idx==0 else [[2,-1,3],[0,4,-2]] if idx==1 else [[rng.randint(-6,9) for _ in range(4)] for _ in range(3)]);return a,f'{len(a)} {len(a[0])}\n'+'\n'.join(' '.join(map(str,row)) for row in a)
 n=[1,6,7,5,8,6][idx];edges=[]
 if idx==1:edges=[(0,1),(1,2),(2,0),(2,3),(4,5)]
 elif idx==2:edges=[(0,1),(1,2),(2,0),(3,4),(4,5)]
 elif idx==3:edges=[(0,1),(1,2),(2,0),(3,4)]
 elif idx==4:edges=list(combinations(range(4),2))+[(4,5),(5,6),(6,4)]
 elif idx==5:edges=[(i,i+1) for i in range(n-1)]
 g=[set() for _ in range(n)]
 for u,v in edges:g[u].add(v);g[v].add(u)
 return g,f'{n} {len(edges)}'+('' if not edges else '\n'+'\n'.join(f'{u+1} {v+1}' for u,v in edges))
problems=[];family_info=[]
for fi,f in enumerate(F):
 cases=[]
 for ci in range(6):
  obj,inp=make_case(f['kind'],ci);b=f['fn'](obj);assert all(isinstance(x,int) for x in b),(fi,b);cases.append((inp,b))
 family_info.append({'name':f['name'],'count':10,'category':f['tag']})
 for vi,(vname,req,solve,vhint) in enumerate(V):
  pid=fi*10+vi+1
  tests=[{'input':inp,'output':str(solve(b))} for inp,b in cases]
  statement=f['desc']+'\n\n'+req+'\n\nB — yordamchi ro‘yxat; uni to‘liq xotirada saqlash shart emas. B bo‘sh bo‘lsa natija 0. Takrorlar yuqorida alohida aytilmasa saqlanadi.'
  problems.append(dict(id=pid,title=f['name']+' — '+vname,category=f['tag'],level=f['level'],family=fi+1,variant=vi+1,statement=statement,input=f['fmt'],output='Yagona butun son — so‘ralgan natija. Natija 64 bitli ishorali butun songa sig‘adi.',hint=f['hint']+' '+vhint,samples=tests[:2],practice=tests[2:],time='2 soniya',memory='256 MB'))
assert len(problems)==1000
assert len({p['title'] for p in problems})==1000
assert len({p['statement'] for p in problems})==1000
(ROOT/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,separators=(',',':')))
(ROOT/'families.json').write_text(json.dumps(family_info,ensure_ascii=False))
print('100 families, 1000 unique statements, 6000 reference-computed outputs generated.')
