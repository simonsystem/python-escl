from setuptools import setup

setup(
    name='escl',
    version='0.0.1',
    description='eSCL Scanning Utility',
    long_description='eSCL Scanning Utility',
    author='Simon Schroeter',
    author_email='simon.schroeter@gmail.com',
    url='https://github.com/simonsystem/python-escl',
    packages=['escl'],
    install_requires=['requests', 'xmltodict'],
    entry_points=dict(console_scripts=['escl=escl.cli:main']),
    classifier=[
        'Environment :: Console',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics :: Capture :: Scanners',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
        'License :: OSI Approved :: MIT License',
    ]
)
