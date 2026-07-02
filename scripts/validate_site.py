#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
html_files=list(ROOT.rglob('*.html'))
errors=[]
for f in html_files:
    t=f.read_text(encoding='utf-8')
    if '<title>' not in t or 'name="description"' not in t or 'rel="canonical"' not in t:
        errors.append(f'Metadonnées SEO incomplètes: {f.relative_to(ROOT)}')
    if ':splat' in t:
        errors.append(f'Référence :splat interdite: {f.relative_to(ROOT)}')
    for url in re.findall(r'(?:src|href)="(/assets/[^"?#]+)',t):
        candidate=ROOT/url.lstrip('/')
        if not candidate.exists(): errors.append(f'Ressource absente {url} dans {f.relative_to(ROOT)}')
for f in ROOT.rglob('*.html'):
    t=f.read_text(encoding='utf-8')
    if '<section class="related"' in t:
        errors.append(f'Ancien bloc related avec images encore présent: {f.relative_to(ROOT)}')
if not (ROOT/'sitemap.xml').exists(): errors.append('sitemap.xml absent')
if not (ROOT/'robots.txt').exists(): errors.append('robots.txt absent')
print(f'{len(html_files)} pages HTML contrôlées.')
if errors:
    print('\n'.join(errors));sys.exit(1)
print('Validation réussie : métadonnées, ressources, sitemap/robots, absence de :splat et de cartes d’articles au bas des pages.')
