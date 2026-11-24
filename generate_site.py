from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parent
DOCS=ROOT/'docs'
ASSETS=ROOT/'assets'
DOCS.mkdir(exist_ok=True)
for folder in ('css','images','js'):
    (DOCS/folder).mkdir(parents=True,exist_ok=True)
    src=ASSETS/folder
    if src.exists(): shutil.copytree(src,DOCS/folder,dirs_exist_ok=True)
pages={
 'index.html':('Home','Build a better digital presence.','A modern, responsive starter website you can customize and publish using GitHub Pages.'),
 'about/index.html':('About','A little about this website.','Replace this paragraph with your story, mission, values, and what makes your work unique.'),
 'services/index.html':('Services','What we offer.','Describe your services, products, or capabilities here.'),
 'contact/index.html':('Contact',"Let's connect.",'Replace the example details with your real contact information.')
}
for file,(title,heading,paragraph) in pages.items():
    p=DOCS/file
    p.parent.mkdir(parents=True,exist_ok=True)
    prefix='../'*(len(Path(file).parts)-1)
    html='''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>'''+title+''' | DigitalStudio</title>
<meta name="description" content="'''+paragraph+'''">
<link rel="stylesheet" href="'''+prefix+'''css/style.css">
</head><body>
<header class="site-header"><a class="brand" href="'''+prefix+'''index.html">Digital<span>Studio</span></a>
<nav aria-label="Main navigation"><a href="'''+prefix+'''index.html">Home</a>
<a href="'''+prefix+'''about/index.html">About</a>
<a href="'''+prefix+'''services/index.html">Services</a>
<a href="'''+prefix+'''contact/index.html">Contact</a></nav></header>
<main><section class="hero"><div class="hero-content"><p class="eyebrow">YOUR ONLINE HOME</p>
<h1>'''+heading+'''</h1><p>'''+paragraph+'''</p>
<a class="button" href="'''+prefix+'''contact/index.html">Get in touch</a></div></section>
<section class="section"><h2>Designed for the next step</h2>
<p>Use this starter to present your ideas, work, services, or organization online. Edit the generator and assets to make it your own.</p>
<div class="cards"><article class="card"><h3>Responsive</h3><p>Designed for phones, tablets, and desktops.</p></article>
<article class="card"><h3>Simple</h3><p>Lightweight HTML, CSS, and a Python build script.</p></article>
<article class="card"><h3>Publishable</h3><p>Ready for GitHub Pages using the docs folder.</p></article></div></section></main>
<footer><p>Copyright 2026 DigitalStudio. Replace this sample brand and content.</p></footer>
<script src="'''+prefix+'''js/script.js"></script></body></html>'''
    p.write_text(html,encoding='utf-8')
print('Generated docs folder successfully.')
