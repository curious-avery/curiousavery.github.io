# Avery H. Liu — research portfolio

A dependency-free static portfolio based on Avery H. Liu’s supplied 2026 resume.

The current design uses a restrained clinical-documentation style with a purple editorial palette, ruled lists, straightforward descriptions, and linked institutional marks. RuKaiKai and DermLatBench use original local project illustrations because no public standalone project logos could be verified. The profile photograph was supplied for this site and optimized locally for web delivery.

## Structure

```text
.
├── index.html
├── 404.html
├── .nojekyll
├── README.md
├── robots.txt
└── assets
    ├── css/site.css
    ├── js/site.js
    └── img/
        ├── *.svg
        └── logos/*
```

## Preview

```bash
python3 -m http.server 8010
```

Open `http://localhost:8010`.

## Deploy to GitHub Pages

1. Copy the files in this folder to the root of the chosen GitHub Pages repository.
2. Commit and push to the default branch.
3. In **Settings → Pages**, select **Deploy from a branch**, the default branch, and `/ (root)`.

There is no build step and no package installation.

## Content sources

Personal history, projects, service, skills, awards, and contact details come from `Avery_H_Liu_Resume_2026_v8_HSRC_SAWC_MIDL_Links.docx` supplied for this build.

Primary public links used in the site include:

- MIDL 2026 paper: `https://openreview.net/pdf?id=qejEHZL4pH`
- DermLatBench SAWC Fall 2026 poster: poster ID `842178`
- Los Angeles County Science Fair 2026 official results
- Los Angeles County Science Fair 2025 official results
- EagleMUN conference leadership page
- LeftRightQuest: `https://leftrightquest.org/`
- Official organization pages linked from each award and community-service logo

The DermLatBench summary statistics come directly from the linked SAWC poster page.
Institutional and conference marks were obtained from the organizations' official sites or, for SCCLA, the official NAPABA awards page. They remain the property of their respective organizations and are used only to identify Avery's associated work and service.

## Editing

- Content: `index.html`
- Colors, layout, and responsive design: `assets/css/site.css`
- Navigation and reveal behavior: `assets/js/site.js`
- Retained original project art: `assets/img/`

The public contact address is `aver.hong.liu@gmail.com`. Avery’s phone number is intentionally omitted from the site.
