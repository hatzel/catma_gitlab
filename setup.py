import setuptools

setuptools.setup(
    name="gitma",
    version="1.5.0",
    author="Michael Vauth",
    packages=setuptools.find_packages(),
    description="Load CATMA annotations from their Git data",
    url="https://github.com/forTEXT/gitma",
    python_requires=">=3.7",
    install_requires=[
        "jupyter",
        "matplotlib",
        "networkx",
        "nltk",
        "pandas",
        "plotly",
        "pygit2",
        "python-gitlab",
        "scipy",
        "spacy",
        "tabulate"
    ]
)
