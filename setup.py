from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="versalaw2",
    version="1.0.0",
    author="VersaLaw AI Team",
    author_email="team@versalaw.ai",
    description="Comprehensive Legal AI Analysis System with Maya AI Integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/versalaw/versalaw2",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Legal :: AI Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="legal, ai, law, analysis, maya, contract, document",
    project_urls={
        "Bug Reports": "https://github.com/versalaw/versalaw2/issues",
        "Source": "https://github.com/versalaw/versalaw2",
        "Documentation": "https://versalaw.ai/docs",
    },
)
