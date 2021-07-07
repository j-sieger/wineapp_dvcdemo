```
pip install cookiercutter

cookiecutter https://github.com/drivendata/cookiecutter-data-science
```
```bash
git init
```
```
pip install dvc
pip install dvc[gdrive]
```
```bash
dvc init
dvc add .\data_given\winequality.csv
```
```
git add .
git commit -m "first commit"
```
```bash
git remote add origin https://github.com/j-sieger/wineapp_dvcdemo.git

git branch -M main
git push -u origin main
```

Creating stages of dvc
```
dvc repro
```
then use git add. and commit, push like as usual.

```
dvc params diff
dvc metrics show
```