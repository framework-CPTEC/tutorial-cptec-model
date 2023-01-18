import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='cptec-model',
      version='0.0.1',
      description='Distribuição de Dados dos Modelos Numéricos!',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/framework-CPTEC/CPTEC-user',
      packages=setuptools.find_packages(),
      author='Framework CPTEC',
      author_email='frameworkcptec@gmail.com',
      license='GNU GPL v3',
      zip_safe=False,
      include_package_data=True,
      install_requires=[
          'matplotlib',
          'Cython',
          'geos',
          'pyproj',
          'cartopy==0.16.0',
          'oauth2client',
          'google-api-python-client',
          'earthengine-api',
      ],
      entry_points={
        'console_scripts': [
            'cee_install_test = cartoee.tests.installation_test:main',
            'cee_plotting_test = cartoee.tests.plotting_test:main'
        ],
      },
)
