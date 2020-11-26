import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LFExtractor",
    version="0.0.1",
    packages=['LFE'],
    description="A corpus-linguistic tool to extract 95 general linguistic features",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Jack Wang",
    author_email="jackwang196531@gmail.com",

    url="https://github.com/jaaack-wang/ling_feature_extractor",
    keywords=['Computational linguistics', 'Corpus-linguistic tool', 'NLP', 'Natural Language Processing'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT License",
)
