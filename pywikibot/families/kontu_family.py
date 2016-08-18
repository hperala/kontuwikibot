# -*- coding: utf-8 -*-

from pywikibot import family
from pywikibot.tools import deprecated


class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'kontu'
        self.langs = {
            'fi': 'kontu.wiki',
            # List of valid language codes needed for 
            # -exceptinsidetag:interwiki to work
            'de': None,
            'en': None,
            'fa': None,
            'fr': None
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
