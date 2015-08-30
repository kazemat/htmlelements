from distutils.core import setup

setup(
    name='htmlelements',
    version='0.2',
    packages=['htmlelements', 'htmlelements.elements', 'htmlelements.decorators', 'htmlelements.log'],
    url='https://github.com/kazemat/htmlelements.git',
    license='GNU GPL',
    install_requires=['selenium'],
    author='plipchak',
    author_email='kazemat92@gmail.com',
    description='Html Elements is a Python framework providing easy-to-use way of interaction with web-page elements in web-page tests.'
)