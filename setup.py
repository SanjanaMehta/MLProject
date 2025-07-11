from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    reqs=[]
    with open(file_path)as file_obj:
        reqs=file_obj.readlines()
        reqs=[req.replace("\n","") for req in reqs]
        if HYPHEN_E_DOT in reqs:
            reqs.remove(HYPHEN_E_DOT)
    return reqs

setup(
name='mlproject',
version='0.0.1',
author='Sanjana Mehta',
author_email='sanjanamehta12feb@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)