# -*- coding: utf-8  -*-

# Ei korvaa tekstiä, jos sitä edeltää välittömästi kaksoispiste esimerkiksi 
# interwikilinkissä
kw_jrr_regex = ur'(?<!:)J\.R\.R\. Tolkien'

fixes['nimikirjaimet'] = {
    'regex': True,
    'msg': {
        '_default': u'Muutettu J.R.R. → J. R. R.'
    },
    'replacements': [
        (kw_jrr_regex, 
         u'J. R. R. Tolkien'),
    ]
}

fixes['nimikirjaimet-nb'] = {
    'regex': True,
    'msg': {
        '_default': u'Muutettu J.R.R. → J. R. R. (sitovilla välilyönneillä)'
    },
    'replacements': [
        (kw_jrr_regex, 
         u'J.&#8239;R.&#8239;R.&nbsp;Tolkien'),
    ]
}
