import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="otus-qa-course-ksenia_yarysh",
    version="0.0.1",
    author="Ksenia Yarysh",
    author_email="ksana32@gmail.com",
    description="otus-qa-course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ksanayarysh",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)