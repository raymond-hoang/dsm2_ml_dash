from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='dsm2_ml_dash',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Short description",
    license="MIT",
    author="Raymond Hoang",
    author_email='raymond.hoang@water.ca.gov',
    url='https://github.com/raymond-hoang/dsm2_ml_dash',
    packages=['dsm2_ml_dash'],
    entry_points={
        'console_scripts': [
            'dsm2_ml_dash=dsm2_ml_dash.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='dsm2_ml_dash',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
