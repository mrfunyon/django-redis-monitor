import os
from setuptools import setup, find_packages
version = __import__('django_redis_monitor').get_version()
if u'SVN' in version:
    version = ' '.join(version.split(' ')[:-1])
    
setup(name='sosdadmin',
    version=version.replace(' ', '-'),
    description='Django Redis Monitor',
    author='simonw',
    author_email='simon@simonwillison.net',
    url='https://github.com/simonw/django-redis-monitor',
    packages=find_packages(),
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
