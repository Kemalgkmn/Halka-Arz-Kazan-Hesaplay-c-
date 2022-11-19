from setuptools import setup


APP = ['HalkaArzHesaplayıcı.py']

OPTİONS = {
    'argv_emulation': True
}


setup(app=APP,options={'py2app':OPTİONS},setup_requires=['py2aapp'])
