from setuptools import setup, find_packages
import os

version = '0.2.1'

setup(name='collective.miscbehaviors',
      version=version,
      description="Miscellaneous behaviors for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone dexterity behavior',
      author='Izhar Firdaus',
      author_email='izhar@inigo-tech.com',
      url='http://svn.plone.org/svn/collective/collective.miscbehaviors',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          'collective.autopermission',
          'plone.namedfile[blobs]',
          'collective.dexteritytextindexer',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],

      )
