# -*- coding: utf-8  -*-

fixes['nimikirjaimet'] = {
    'regex': True,
    'msg': {
        '_default': u'Lisätty välilyönnit nimikirjainlyhenteisiin'
    },
    'replacements': [
        (ur'J\.R\.R\. Tolkien', 
         u'J. R. R. Tolkien'),
        (ur'C\.S\. Lewis', 
         u'C. S. Lewis'),
        (ur'W\.H\. Lewis', 
         u'W. H. Lewis'),
    ]
}