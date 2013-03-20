from setuptools import setup

setup(
    name='django-suit-ckeditor',
    version='0.0.2',
    description='CKEditor (WYSIWYG editor) integration app for Django admin. http://ckeditor.com',
    author='Kaspars Sprogis (darklow)',
    author_email='info@djangosuit.com',
    url='https://github.com/darklow/django-suit-ckeditor',
    packages=['suit_ckeditor'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'License :: OSI Approved',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Topic :: Software Development :: User Interfaces',
    ]
)
