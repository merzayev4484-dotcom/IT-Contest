# IT Contest — email-parol va Google bilan kirish

Bu versiya ChatGPT hisobini talab qilmaydi. 1000 original mashq, profil, admin, coin va serverdagi kod tekshirish saqlangan. Email-parol bilan kirish, ro‘yxatdan o‘tish, emailni tasdiqlash, parol tiklash, Google OAuth va chiqish Supabase Auth orqali ishlaydi.

## Hozirgi holat
Manba tayyor, GitHub yoki Cloudflare akkauntingizga yuklanmagan. Google provider Supabase-da yoqilishi kerak. GitHub Pages server kodini bajarmaydi: frontend GitHub-da, judge API Cloudflare Worker+D1-da ishlaydi. API ulanmaguncha tizim kirishdan keyin bu haqda aniq xabar ko‘rsatadi. Soxta Accepted yoki coin berilmaydi. Avvalgi ChatGPT akkauntidagi natijalar avtomatik ko‘chmaydi.

## 1. Supabase
Authentication → URL Configuration: Site URL va Redirect URL:
https://merzayev4484-dotcom.github.io/IT-Contest/
Email provider va signups yoqilgan bo‘lsin. Google provider uchun o‘zingiz yaratgan Client ID va yangi secretni dashboardga kiriting. Secretlar bu paketda yo‘q. Google test rejimida faqat test users kira oladi. Email yuborish limitlari Supabase tarifiga bog‘liq.

## 2. Cloudflare API
Kompyuterda Node.js o‘rnating. Shu papkada terminal oching:
```
npm install
npx wrangler login
npm run db:create
```
Chiqqan database_id ni wrangler.toml ga qo‘ying.
Supabase → Authentication → Users ichidagi o‘z foydalanuvchi UUID qiymatingizni ADMIN_USER_ID ga qo‘ying. Birinchi kirgan odam avtomatik admin qilinmaydi.
```
npm run db:migrate
npm run deploy:api
```
Chiqqan https://it-contest-api....workers.dev manzilini config.js dagi apiUrl ga kiriting (oxirida slashsiz). Cloudflare va Wandbox cheklovlari amal qiladi. Maxfiy testlarni saqlash uchun worker manbasini public repozitoriyga yuklamang.

## 3. GitHub Pages
Faqat index.html, app.js, config.js fayllarini IT-Contest repozitoriy ildiziga yuklang. Avvalgi Google tasdiqlash faylini o‘chirmang. Bu eski launcher index.html o‘rnini bosadi. Boshqa eski frontend/worker fayllari Pages uchun kerak emas. Ctrl+F5 bilan yangilang.

## Tekshirish
`npm test` — server identifikatsiyasi, soxta header, admin huquqi, CORS va foydalanuvchilar ajratilishini tekshiradi. Haqiqiy OAuth browserga qaytish va email oqimini o‘z akkauntingiz bilan deploymentdan keyin sinang.

Google Cloud client secret yoki Supabase secret/service_role kalitini frontendga, GitHubga yoki chatga qo‘ymang. Paket faqat ochiq publishable kalitni o‘z ichiga oladi.
