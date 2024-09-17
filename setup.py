from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filename: str) -> List[str]:
    requirements = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            requirements.append(line.strip())
             
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
        
    return requirements
    
setup(
    name='Kaggle SDD',
    packages=find_packages(),
    version='0.0.1',
    description='Kaggle - Software Defects Dataset',
    author='Theod',
    install_requires=get_requirements('requirements.txt'),
       
)