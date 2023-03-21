from setuptools import find_packages, setup

setup(
    name="TP2",
    version="0.1.1",
    description="Travail pratique sur la qualité de code et le CI/CD",
    long_description=open("README.md").read(),
    author="prenom.nom",
    packages=find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    install_requires=open("requirements.txt").readlines()
)
