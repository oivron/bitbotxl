import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitbotxl",
    version="0.0.1",
    author="Øivind Rønning, Statped",
    author_email="oiron@statped.no",
    license = "GNU GENERAL PUBLIC LICENSE",
    description="A Python module for the 4tronix Bit:bot XL.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oivron/bitbotxl",
    packages=setuptools.find_packages(include=['bitbot']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    keywords='micro:bit Bit:bot XL',
    project_urls={
    'Source': 'https://github.com/oivron/bitbotxl',
    },
    #package_dir={'': 'bitbotxl'},
    py_modules=['bitbot'],
    python_requires='>=3',
    install_requires=['uflash', 'microfs', 'pylint'],
)