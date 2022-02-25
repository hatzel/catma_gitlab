import setuptools

setuptools.setup(
    name="gitma",
    version="1.4.1",
    author="Michael Vauth",
    packages=setuptools.find_packages(),
    description="Load CATMA annotations from their Git data",
    url="https://github.com/forTEXT/gitma",
    python_requires=">=3.5",
    install_requires=[
        "jupyter",
        "matplotlib",
        "pandas",
        "plotly",
        "pygit2",
        "python-gitlab",
        "spacy",
        "tabulate"
    ]
)
