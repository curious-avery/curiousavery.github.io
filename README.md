# Avery H. Liu — browser-upload repair

This flat package repairs the text-only rendering at:

`https://curious-avery.github.io/`

GitHub's browser uploader placed the earlier package's CSS, JavaScript, and
images at the repository root. This export deliberately places every site file
at that same level and rewrites `index.html` and `404.html` to match.

## Upload

1. Open `https://github.com/curious-avery/curious-avery.github.io` while signed
   in as the `curious-avery` account.
2. Select **Add file → Upload files**.
3. Open this extracted folder and select every item inside it. Do not upload the
   ZIP or the enclosing folder.
4. Confirm `index.html`, `site.css`, `site.js`, `avery-sunset.jpg`, and
   `carenery.svg` are listed at the repository root.
5. Commit directly to `main` with a message such as
   `Repair Avery site assets`.
6. Wait for the Pages deployment to finish, then hard-refresh the site.

The layout is intentionally flat so GitHub's browser uploader cannot discard a
required directory structure.
