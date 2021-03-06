# -*- coding: utf-8  -*-
"""
UploadRobot test.

These tests write to the wiki.
"""
#
# (C) Pywikibot team, 2015
#
# Distributed under the terms of the MIT license.
#
from __future__ import unicode_literals

__version__ = '$Id: b7e2de2adc75da03716c9ea62e0652ff99a2be9d $'
#

import os

from scripts import upload
from tests import _images_dir
from tests.aspects import unittest, TestCase


class TestUploadbot(TestCase):

    """Test cases for upload."""

    write = True

    family = 'wikipedia'
    code = 'test'

    def test_png_list(self):
        """Test uploading a list of pngs using upload.py."""
        image_list = []
        for directory_info in os.walk(_images_dir):
            for dir_file in directory_info[2]:
                image_list.append(os.path.join(directory_info[0], dir_file))
        bot = upload.UploadRobot(url=image_list,
                                 description="pywikibot upload.py script test",
                                 useFilename=None, keepFilename=True,
                                 verifyDescription=True, aborts=set(),
                                 ignoreWarning=True, targetSite=self.get_site())
        bot.run()

    def test_png(self):
        """Test uploading a png using upload.py."""
        bot = upload.UploadRobot(url=[os.path.join(_images_dir, "MP_sounds.png")],
                                 description="pywikibot upload.py script test",
                                 useFilename=None, keepFilename=True,
                                 verifyDescription=True, aborts=set(),
                                 ignoreWarning=True, targetSite=self.get_site())
        bot.run()

    def test_png_url(self):
        """Test uploading a png from url using upload.py."""
        bot = upload.UploadRobot(url=['https://upload.wikimedia.org/wikipedia/commons/f/fc/MP_sounds.png'],
                                 description="pywikibot upload.py script test",
                                 useFilename=None, keepFilename=True,
                                 verifyDescription=True, aborts=set(),
                                 ignoreWarning=True, targetSite=self.get_site())
        bot.run()


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
