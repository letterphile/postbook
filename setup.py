import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="postbook", 
    version="0.0.1",
    author="Aswin Rajasekharan",
    author_email="aswin4400@gmail.com",
    description="Convert IPython Notebook to Blog Post",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aswin4400/postbook.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'postbook=postbook.main:main',
        ]
    }
)