from setuptools import setup
import os

setup(name='cody',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='AIO',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=[
                'script',
                'test'
                ],
      package_dir={
          '': 'src',
          'script': os.path.join('src', 'script'),
          'test': os.path.join('src', 'test'),
      },
      zip_safe=False)
