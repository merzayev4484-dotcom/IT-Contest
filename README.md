# IT Contest — GitHub uchun loyiha

1000 ta original masala (100 algoritmik asos × 10 shart varianti), C++/Python kod yuborish, profil/bio/rasm, admin orqali masala qo‘shish, coin, faollik, reyting va yechimlar tarixi.

## GitHub’ga yuklash
1. ZIPni kompyuterda oching (Extract All / Извлечь всё).
2. GitHub → New repository → repository nomini yozing → Create repository.
3. Add file → Upload files orqali ZIP ichidagi fayl va papkalarni yuklang. ZIPning o‘zini repositoryga yuklamang.
4. Commit changes tugmasini bosing. .openai va .gitignore kabi yashirin fayllarni ham qo‘shish kerak. To‘liq manba uchun Git orqali push qilish qulayroq.

Git orqali (Git o‘rnatilgan bo‘lishi kerak):
```bash
git init
git add .
git commit -m "IT Contest initial version"
git branch -M main
git remote add origin https://github.com/SIZNING_LOGIN/IT-Contest.git
git push -u origin main
```
SIZNING_LOGIN o‘rniga GitHub loginni, IT-Contest o‘rniga yaratgan repository nomini yozing.

## GitHub Pages’ni yoqish
Settings → Pages → Deploy from a branch → main → /(root) → Save.

Rootdagi index.html sahifasi tayyor **jonli IT Contest’ga kirish tugmasini** ko‘rsatadi. U butun backendni GitHub Pages’da bajarmaydi. Jonli sayt manzili:
https://it-contest-firdavs-live.chicberry11.chatgpt.site/

Sayt hozir egasiga yopiq. “Continue with ChatGPT” orqali aynan sayt egasining hisobi bilan kiriladi. GitHub Pages yoqilishi jonli saytning yopiq kirish siyosatini o‘zgartirmaydi. Boshqa odamlar foydalanishi uchun jonli saytga ruxsatlar alohida sozlanishi kerak.

## Muhim farq
GitHub repository — manba kodini saqlash joyi. GitHub Pages — HTML/CSS/JavaScript fayllarini uzatuvchi statik hosting. C++/Python’ni tekshirish, hisoblar va bazani saqlash backend hamda tashqi kompilyator talab qiladi.

Bu ZIP allaqachon ishlayotgan Sites loyihasining manba nusxasi. Boshqa hostingga ko‘chirish tayyor bir bosishli jarayon emas: autentifikatsiya, D1 bazasi va migrationlarni moslashtirish kerak. Sites kiritadigan oai-authenticated-user-id sarlavhasini ochiq oddiy serverda tekshirmasdan ishonchli deb qabul qilish mumkin emas. Alohida hosting uchun tasdiqlangan autentifikatsiya qo‘shilmaguncha API’ni internetga ochmang.

## Fayllar
- index.html — GitHub Pages uchun jonli saytga kirish sahifasi.
- frontend.html, frontend.js — serverga ulangan foydalanuvchi interfeysi.
- worker/index.js — joylashtiriladigan to‘liq server kodi va o‘rnatilgan 1000 ta masala.
- backend.js — API, huquqlar, profil, yechim yuborish va judge adapteri.
- hidden.json — 6000 ta server testi. Repository ommaviy bo‘lsa ular ham ko‘rinadi; testlarni sir saqlash kerak bo‘lsa repositoryni Private qiling.
- drizzle/ — ma’lumotlar bazasi migrationlari.
- db/schema.ts — baza sxemasi.
- build_frontend.py — interfeysni va serverni yig‘ish skripti.
- authoring/ — 1000 ta original masala generatori, shablonlar va tekshiruvlar.
- scripts/build.sh — server artefaktini yig‘ish.
- test-backend.mjs — backend integratsion testlari (kompilyator javobi mock qilinadi).
- README-server.md — server arxitekturasi va cheklovlari.

## Lokal tekshiruv
Node.js 24+ va Python 3 kerak:
```bash
npm ci
npm run build
npm run validate
node test-backend.mjs
python3 authoring/verify.py
```

`npm run build` saytni lokal serverda avtomatik ishga tushirmaydi; joylashtiriladigan Worker faylini tayyorlaydi. HTML’ni kompyuterda ochish backendni ishga tushirmaydi.

Jonli serverdagi C++ va Python dasturlari haqiqatan bajarilishi tekshirilgan. Hisob ichidagi yakuniy foydalanuvchi testi egasining loginini talab qiladi. Wandbox xizmati mavjudligi va limitlari tashqi xizmatga bog‘liq; xatolar natija sifatida aniq ko‘rsatiladi. Keyinchalik maxsus Judge0 xizmatiga ulash uchun JUDGE0_URL va kerak bo‘lsa JUDGE0_TOKEN server secretlari ishlatiladi.

## Sirlarni saqlash
Parol, API tokeni, .env, .dev.vars yoki haqiqiy foydalanuvchilar bazasini GitHubga yuklamang. Bu ZIPga ular kiritilmagan.
