# edit notebooks

myst build --html

git add .
git commit -m "Update project"
git push origin main

ghp-import -n -p -f _build/html