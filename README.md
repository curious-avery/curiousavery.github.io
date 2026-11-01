# Avery H. Liu website: GitHub Pages repair

**Target repository:** https://github.com/curious-avery/curious-avery.github.io

**Target site:** https://curious-avery.github.io/

This repair preserves the existing portfolio text, photos, logos, CSS,
and JavaScript. It corrects the misplaced asset references in `index.html`
and `404.html`, and replaces outdated references to `curiousavery` in README.md.

## Use without Python (recommended for a quick repair)

In GitHub, open `index.html` and choose Edit (pencil icon). Apply these
replacements in order:

1. `assets/css/site.css` -> `site.css`
2. `assets/js/site.js` -> `site.js`
3. `assets/img/logos/` -> (empty string)
4. `assets/img/` -> (empty string)

Commit to `main`. Then edit `404.html` and replace:

1. `assets/img/favicon.svg` -> `favicon.svg`
2. `assets/css/site.css` -> `site.css`

Finally, update `README.md`: replace `curiousavery` with `curious-avery`.

No files should be deleted. The existing media and CSS/JS files are
already at the root of this repository.

## Rebuild the entire package with Python

1. On the GitHub repository's Code tab choose **Code > Download ZIP**.
2. Put the downloaded ZIP next to `repair_avery_site.py`.
3. Run:

   python repair_avery_site.py curious-avery.github.io-main.zip

4. The script creates `avery-site-fixed/` and `avery-site-fixed.zip`.
5. Extract `avery-site-fixed.zip` and upload its *contents* to the root
   of the same GitHub repository. Do not upload the ZIP itself.
6. Confirm Settings > Pages uses **Deploy from a branch**, **main**, **/(root)**.
7. Wait for a successful deployment in the repository's Actions tab,
   then hard-refresh https://curious-avery.github.io/.

**Note:** The ChatGPT-connected GitHub accounts currently have read-only
permissions for the `curious-avery` repository. This pack does not
automatically publish changes to GitHub.
