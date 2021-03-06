from Cython.Build import cythonize
from setuptools import setup, find_packages, Extension

from queryexpander import __version__

extensions = [
    Extension(
        'queryexpander.semantic_similarity',
        ['queryexpander/semantic_similarity.pyx'],
        libraries=['accelerator'],
        language='c++',
        extra_compile_args=['-std=c++1z', '-O3', '-fopenmp', '-DEIGEN_DONT_PARALLELIZE',
                            '-I./libraries/document-search-accelerator/libraries/fmt'],
        extra_link_args=['-std=c++1z', '-fopenmp', '-L./libraries/document-search-accelerator/build/lib'],
    ),
]

setup(
    name='QueryExpansion',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'QueryExpander = queryexpander.__main__:cli',
            'VocabularyTester = vocabularytester.__main__:run_test',
            'FeedbackCalculator = feedbackcalculator.__main__:cli',
        ],
    },

    install_requires=[
        'click',
        'pandas',
        'scipy',
        'cython',
        'sortedcontainers',
        'lxml'
    ],

    ext_modules=cythonize(extensions)
)
