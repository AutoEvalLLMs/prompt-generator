from setuptools import find_packages, setup

def read_requirements(filename: str):
    with open(filename) as requirements_file:
        requirements = []
        for line in requirements_file:
            line = line.strip()
    return requirements

'''
setup(
    name="promt-generator",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=read_requirements("requirements.txt"),
    python_requires="~=3.10",
)
'''

setup(
    name='promt-generator',
    version='0.0.1',
    packages=find_packages(),
    install_requires=read_requirements("requirements.txt"),
    #python_requires="~=3.10",
)