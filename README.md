`conda create -n wineq python3.8 -y`

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
running the test cases
`pytest -v`

## Building a package with tox and testing
```
tox
```
Rebuildig
```
tox -r
```

Create a setup.py file and below command to create package.
pip install -e .

Below command will create distribution. then any can install this library that got created in './dist' after below command.
```
python setup.py sdist bdist_wheel
```
But it is not required deleting the `./build` and `./dist` from our project.


