# Alokbortika 2027 website, version 3

Deploy: upload everything in this folder (index.html, register.html, assets/) to any static host. No build step.

- Opens in English on every fresh visit; the EN | বাংলা toggle switches, and the choice carries to register.html for that visit.
- Photos: assets/people/muhammad-yunus.webp, venue photos in assets/venue/ (all WebP, lazy-loaded).
- Registration: set `sheetEndpoint` near the top of register.html to your Apps Script /exec URL to save entries.

Edit content: source/data.py (shared content), source/tr_bn.py (Bangla), source/build.py (page text, LEADS).
Then: cd source && python3 build.py   (rewrites index.html in this folder)
