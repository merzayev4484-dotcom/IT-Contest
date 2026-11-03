# IT Contest — hosted platform

1000 original exercises, authenticated profiles, administrator-only problem creation, C++17 and Python execution via server-side compiler API, D1-persisted submissions, accepted solutions, coins, drafts and bookmarks.

Hosting remains owner-private. ChatGPT sign-in supplies the Site-specific user ID. The first authenticated visitor on this newly created owner-private Site becomes the persistent administrator; subsequent authenticated identities receive normal user access. Changing Site audience is a separate explicit action, never performed by the app.

## Execution
By default, Wandbox is used without an API key. User code and one test input are sent per compilation with `save:false`. CPU, memory and language availability depend on that external compiler service. This is a private educational installation, not a load-tested contest service. The UI reports service errors rather than granting acceptance. For a dedicated judge, configure JUDGE0_URL and optionally JUDGE0_TOKEN as runtime secrets, then redeploy. Judge0 must support wait=true and language IDs 54/71. In Judge0 mode, 2s CPU, 5s wall time, 256MB and network-disabled execution are requested.

Each of the 1000 base tasks has six additional server-only tests generated independently from its public examples. Text output is compared after whitespace normalization. Code is sent test-by-test through `/api/judge-step`; if the tab closes, resume from submissions. This avoids hiding a long job after the response finishes. No queue runs independently of a browser. Pending locks expire after 30 seconds.

Accepted solutions are stored under a unique user/problem key, so repeating an Accepted result never grants more coins. Client-supplied solved/coin/admin values are not accepted. Personal write APIs validate name, bio, avatar and drafts. Admin-created tasks require reference tests, and only administrators can create them. There is no user-role promotion endpoint.

## Validation
`npm run db:generate` generates the Drizzle migration. Build with `bash scripts/build.sh`, validate with `node scripts/validate-artifact.mjs`, and run `node test-backend.mjs`. The latter uses an in-memory SQLite D1 adapter and a mocked compiler transport to verify auth, persisted profiles, forged-reward rejection, user isolation, six-test acceptance, wrong answers, compilation errors and idempotent rewards.

The deployed `/api/diagnostics` endpoint is protected by the Site owner-private platform gate and performs fixed C++ and Python addition tests without user identity or writes. Its result verified both actual remote compiler execution and the production D1 schema. Interactive account/submission verification requires the owner's ChatGPT login.
