```
jupyter book build --html

git status
git add .
git commit -m "Update Jupyter Book"
git push origin main

ghp-import -n -p -f _build/html