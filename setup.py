from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    requirements = fh.read().split("\n")

setup(
    name="pyduckduckgosearch",
    version="1.1.0",
    author="Arvind Ahirwar",
    author_email="ad.ahirwar@gmail.com",
    description="A Python library for scraping the DuckDuckGo search engine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adahirwar/websearch",
    packages=["websearch"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[requirements]
)
