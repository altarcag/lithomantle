from pathlib import Path

content = """# Updating the LithoMantle Jupyter Book GitHub Page

Use this checklist whenever you change one of the notebooks or files in the project.

## 1. Work normally in your notebooks

Edit your `.ipynb`, `.md`, data files, figures, or `myst.yml` as usual.

## 2. Save everything

In VS Code/Jupyter, save the changed notebooks/files.

## 3. Build the website locally

From the project folder:

```bash
jupyter book build --html


##

git status
git add .
git commit -m "Update Jupyter Book content"
git push origin main
