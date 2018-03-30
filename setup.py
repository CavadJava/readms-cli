from setuptools import setup

setup(name='readms-cli',
      version='0.1',
      description='A cli tool for downloading manga in https://readms.net',
      url='https://github.com/dslizardo/readms-cli',
      author='Daniel Lizardo',
      author_email='dslizardo@gmail.com',
      license='MIT',
      packages=['readms'],
      install_requires=['setuptools','lxml','requests'],
      entry_points="""
      [console_scripts]
      readms = readms.readms:main
      """,
      zip_safe=False)