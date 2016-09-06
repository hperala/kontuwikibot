# -*- coding: utf-8 -*-

from pywikibot import family
from pywikibot.tools import deprecated


class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'kontu'
        self.langs = {
            'fi': 'kontu.wiki',
            # A list of valid language codes is needed for the 
            # -exceptinsidetag:interwiki parameter of the replace script to 
            # work. The category script does not allow the values to be empty.
            'de': 'localhost',
            'en': 'localhost',
            'fa': 'localhost',
            'fr': 'localhost'
        }

    def scriptpath(self, code):
        return {
            'fi': '/w',
            'de': '/dummy',
            'en': '/dummy',
            'fa': '/dummy',
            'fr': '/dummy'
        }[code]

    @deprecated('APISite.version()')
    def version(self, code):
        return {
            'fi': u'1.24.1',
        }[code]
