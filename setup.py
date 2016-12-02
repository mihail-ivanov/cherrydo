from setuptools import setup

setup(
    name='CherryDo',
    version='0.0.1.dev1',
    description='CherryPy generators',

    url='https://github.com/mihail-ivanov/cherrydo',

    author='Mihail Ivanov',
    author='mihail@muplextech.com',

    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 1 - Development',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],

    keywords='cherrypy python development generators',

    entry_points={
        'console_scripts': [
            'cherrydo=cherrydo:commands',
        ],
    },
)
