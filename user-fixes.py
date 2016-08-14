# -*- coding: utf-8  -*-

fixes['nimikirjaimet'] = {
    'regex': True,
    'msg': {
        '_default': u'Muutettu J.R.R. → J. R. R.'
    },
    'replacements': [
        (ur'J\.R\.R\. Tolkien', u'J. R. R. Tolkien'),
    ]
}

fixes['nimikirjaimet-np'] = {
    'regex': True,
    'msg': {
        '_default': u'Muutettu J.R.R. → J. R. R. (sitovilla välilyönneillä)'
    },
    'replacements': [
        (ur'J\.R\.R\. Tolkien', u'J.&#8239;R.&#8239;R.&nbsp;Tolkien'),
    ]
}