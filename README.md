
pip install cookiercutter

cookiecutter https://github.com/drivendata/cookiecutter-data-science

git init

pip install dvc
pip install dvc[gdrive]

dvc init
dvc add .\data_given\winequality.csv

git add .
git commit -m "first commit"

git remote add origin https://github.com/j-sieger/wineapp_dvcdemo.git

git branch -M main
git push -u origin main


