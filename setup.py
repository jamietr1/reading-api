from setuptools import setup

setup(name='readingapi',
      version='0.1',
      description='API for my reading list',
      url='http://github.com/jamietr1/baseball-century',
      author='Jamie Todd Rubin',
      author_email='jamie@jamietoddrubin.com',
      license='MIT',
      packages=['readingapi'],
      package_dir={'readingapi': 'readingapi'},
      install_requires=[

      ],
      scripts=['bin/readingapi'],
      include_package_data=False,
      zip_safe=False)
