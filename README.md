#PrimeLA
### Visualization Package for 'Prime Linear Algebra'
### '으뜸 선형대수'를 위한 가시화 패키지

This is a simple preliminary package 
for visualizing the vectors (2d and 3d) and matrix (2x2, 3x3)

[GitHub Repository](https://github.com/dknife/PrimeLA)

Author: Young-Min Kang (c) 2021


### Python Package Distribution

Dknife Kang

#### Prepare Files for Package

##### Package_Dir

* src/
* example_package/
* __init__.py
* example.py
* tests/
* LINCENSE
* README.md
* pyproject.toml
* setup.py

##### Contents of Files

###### example.py
<pre>
def add_one(number):

    return number + 1
</pre>

###### setup.py
<pre>
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-dknife",
    version="0.0.1",
    author="dknife",
    author_email="young.min.kang@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dknife",
    project_urls={
        "Bug Tracker": "https://github.com/dknife",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
</pre>

###### pyproject.toml
<pre>
[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"
</pre>


#### Build

<pre>
$ python -m pip install --upgrade pip

$ python -m pip install --upgrade build

$ python -m build

$ python -m pip install --upgrade twine
</pre>

#### Get a token from TestPyPI (or PyPI)

Of course, you must have a valid id there...

https://test.pypi.org/manage/account/#api-tokens,

#### Copy token

To use this API token:

Set your username to __token__

Set your password to the token value, including the pypi- prefix

For example, if you are using Twine to upload your projects to PyPI, set up your $HOME/.pypirc file like this:

<pre>
[testpypi]
  username = __token__
  password = pypi-AgENdGVz**********************************************************************************************************DRw
</pre>

For further instructions on how to use this token, visit the PyPI help page.

#### location of .pypirc  / contents
* $HOME ( C:\Windows\Users\youraccount\)

###### .pypirc
<pre>
[distutils]
index-servers =
    pypi
    testpypi
 
[pypi]
username = __token__
password = pypi-AgENdGVzdC5weXBpLm9----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------S-pTn4mDkdtsThauWzSgGGjtE_rMNZEYCsDRw
 
[testpypi]
username = __token__
password = pypi-AgENdGVzdC5weXBpLm9----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------S-pTn4mDkdtsThauWzSgGGjtE_rMNZEYCsDRw
</pre>

#### upload your package
<pre>
$ python -m twine upload --repository testpypi dist/*
</pre>


#### install your own package and use it everywhere.


