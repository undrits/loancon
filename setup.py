import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read().strip()

VERSION = '0.0.1'

setuptools.setup(
    name="RuLoan",
    version=VERSION,
    author="Yulia Spektor",
    author_email="yuliaspektor@gmail.com",
    description="Lexicon of English loanwords in Russian",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/undrits/loancon",
    keywords=[
        "morphology",
        "loanwords",
        "russian",
        "language",
        "natural language processing",
        "computational linguistics",
        ],
    license="GNU General Public License v3 (GPLv3)",
    py_modules=["rus_loan_lexicon", "ruloan_pb2", "utils", "compile"],
    python_requires=">=3.8",
    zip_safe=False,
    install_requires=["protobuf"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
    ],
)