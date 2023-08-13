import setuptools

with open("README.rd","r",encoding="utf-8") as f:
    long_description = f.read()


__version__ =  "0.0.1"

REPO_NAME = 'textSumarization'
AUTHOR_USER_NAME = "kabyabasu"
SRC_REPO = "textSumarization"
AUTHOR_EMAIL = "kabyabasu@yahoo.co.uk"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarization",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kabyabasu/textSumarization",
    project_urls={
        "Bug Tracker": "https://github.com/kabyabasu/textSumarization/issues",
    },

    package_dir= ("":"src"),
    packages=setuptools.find_packages(where="src"),
    
)