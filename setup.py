from setuptools import setup, find_packages
with open('README.md', 'r') as f:
	page_description = f.read()

with open('requirements.txt') as f:
	requirements = f.read().splitlines()	

setup(
	nome = 'condoAccess',
	version = '0.0.1',
	author = 'Adonis Pantoja',
	author_email = 'adonisruis07@gmail.com',
	description ='Sistema de gerenciamento de entrada e saída de condomínio.',
	long_description = page_description,
	long_description_content_type = 'text/markdown',
	url = 'https://github.com/Adonis071/gerenciamento_de_portaria.git',
	packages= find_packages(),
    install_requires= requirements,
	python_requires='>=3.8',	
)