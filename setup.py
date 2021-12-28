from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

about = {}
with open(path.join(here, "src", "nft_utils", "__version__.py"), encoding="utf8") as fh:
    exec(fh.read(), about)

with open(path.join(here, "README.md"), "r", "utf-8") as f:
    readme = f.read()

setup(
    name="nft-utils",
    version=about["__version__"],
    url="https://github.com/unparalleled-js/nft-utils",
    project_urls={
        "Issue Tracker": "https://github.com/unparalleled-js/nft-utils/issues",
        "Documentation": "https://github.com/unparalleled-js/nft-utils",
        "Source Code": "https://github.com/unparalleled-js/nft-utils",
    },
    description="A wrapper around the Pinata REST APIs",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7, <4",
    install_requires=["pydantic>=1.8.2,<2.0.0"],
    extras_require={
        "dev": [
            "flake8==3.9.2",
            "pinata==0.1.0",
            "pytest==6.2.4",
            "pytest-cov==2.12.1",
            "pytest-mock==3.6.1",
            "tox==3.24.0",
        ]
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)