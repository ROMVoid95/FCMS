import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_storage',
    'waitress',
    'alembic',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'bcrypt',
    'colander',
    'deform',
    'passlib',
    'argon2_cffi',
    'psycopg2-binary',
    'requests',
    'authlib',
    'humanfriendly',
    'numpy',
    'graypy',
    'zmq',
    'simplejson',
    'semver',
    'discord-webhook',
    'sqldictalchem',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest >= 3.7.4',
    'pytest-cov',
]

setup(
    name='FCMS',
    version='2.0',
    description='FCMS',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='ROMVoid95',
    author_email='rom.void95@gmail.com',
    url='https://github.com/ROMVoid95',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = FCMS:main',
        ],
        'console_scripts': [
            'initialize_FCMS_db=FCMS.scripts.initialize_db:main',
            'eddn_client=FCMS.scripts.eddn_client:main',
            'load_regions=FCMS.scripts.load_regions:main',
        ],
    },
)
