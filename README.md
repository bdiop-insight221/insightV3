# Insight 221 — site statique prêt pour Netlify

Ce dossier est un **nouveau site complet**, autonome et prêt à déposer dans un nouveau dépôt GitHub. Il ne requiert ni Node.js ni commande de build.

## Ce qui a été corrigé

- Les liens d’articles utilisent directement des dossiers `articles/nom-de-l-article/index.html` : aucune règle de redirection et aucune référence `:splat`.
- Chaque page d’article possède une seule image de présentation compacte. Sa hauteur est limitée pour qu’elle ne prenne pas tout l’écran.
- Les blocs avec photos d’articles suggérés en bas de page ont été retirés. En fin d’article, il reste seulement des liens texte vers deux lectures associées.
- Toutes les pages disposent d’un titre SEO, d’une meta description, d’une URL canonique, d’Open Graph et de données structurées `NewsArticle`.
- `robots.txt`, `sitemap.xml`, `feed.xml`, formulaire Netlify et page 404 sont inclus.

## Test avant publication

Depuis WSL, dans ce dossier :

```bash
python3 scripts/validate_site.py
```

Le résultat attendu est une validation réussie sans erreur.

## Créer un nouveau dépôt GitHub et envoyer le site

1. Décompresse ce ZIP dans **Downloads**.
2. Sur GitHub, crée un nouveau dépôt vide, par exemple `insight221-site`. Ne coche pas README, licence ou .gitignore.
3. Dans WSL, ouvre ce dossier :

```bash
cd "/mnt/c/Users/ciner/Downloads/insight221"
```

4. Lance ensuite :

```bash
git init
git add .
git commit -m "Publication du nouveau site Insight 221"
git branch -M main
git remote add origin https://github.com/DiopBabacarEdu/insight221-site.git
git push -u origin main
```

Remplace seulement `insight221-site` si tu choisis un autre nom de dépôt. Lors de la demande de mot de passe GitHub, colle un **Personal Access Token**, jamais le mot de passe du compte.

## Déployer avec Netlify

Dans Netlify, importe le nouveau dépôt GitHub. Le fichier `netlify.toml` indique déjà que le dossier publié est la racine du projet (`.`). Ne crée aucune redirection personnalisée pour les articles.

Ajoute ensuite `insight221.com` dans les domaines du site Netlify et définis-le comme domaine principal.

## Emplacement des images

Les images sont sous `assets/images/`. La photo principale de chaque article est définie dans `content/articles.json` par la propriété `cover` et dans la page `articles/.../index.html` par la balise `<figure class="article-cover">`.

