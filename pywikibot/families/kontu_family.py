# -*- coding: utf-8 -*-
"""
This family file was auto-generated by $Id: 4993fd66518a2c61c49b9e1bdf8f4b622459ee34 $
Configuration parameters:
  url = http://kontu.wiki/Etusivu
  name = kontu

Please do not commit this to the Git repository!
"""

from pywikibot import family
from pywikibot.tools import deprecated


class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'kontu'
        self.langs = {
            'fi': 'kontu.wiki',
        }

    def scriptpath(self, code):
        return {
            'fi': '/w',
        }[code]

    @deprecated('APISite.version()')
    def version(self, code):
        return {
            'fi': u'1.24.1',
        }[code]
