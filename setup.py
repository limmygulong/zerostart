import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zerostart",
    version="0.0.1",
    author="feng",
    author_email="970734493@qq.com",
    description="by arcade",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/limmygulong/zerostart",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)