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

fixes['kaarmeen-linkit'] = {
    'regex': True,
    'msg': {
        '_default': u'Muutettu ulkoisessa linkissä kontu.info/keskustelut → kontu.me/keskustelut'
    },
    'replacements': [
        (ur'kontu\.info/keskustelut', 
         u'kontu.me/keskustelut')
    ]
}