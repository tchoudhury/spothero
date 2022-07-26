from setuptools import setup, find_packages

setup(
   name='spothero_database',
   version='1.0',
   description='A useful module',
   author='Tahmid',
   author_email='fakeemail@email.example',
   packages=find_packages('lib'),
   install_requires=[
      'sqlalchemy', 'flask', 'flask_restful'
   ],
)
