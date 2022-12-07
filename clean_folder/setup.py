from setuptools import setup

setup(name='clean_folder',
      version='0.0.1',
      description='script for cleaning folders',
      url='https://github.com/Poznanskyi/New-repository',
      author='Poznanskyi Dmytro',
      author_email='shazampoz@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
      )