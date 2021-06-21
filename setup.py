import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prime_linear_algebra",
    version="0.0.3",
    author="dknife",
    author_email="young.min.kang@gmail.com",
    description="A small linear algebra package",
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
