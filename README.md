# Kontuwikibot

Kontuwikibot on tarkoitettu automaattisten massamuokkausten tekemiseen [Kontuwikissä](http://kontu.wiki). Se koostuu [Pywikibotista](https://www.mediawiki.org/wiki/Manual:Pywikibot) (2.0rc4) ja Kontuwikiä varten luoduista tai muokatuista asetustiedostoista.

## Vaatimukset

- Python (Pywikibotin manuaalin mukaan vähintään 2.7.2 tai 3.3)

## Tiedostot

- `user-fixes.py`
- `user-config.py`
- `pywikibot/families/kontu_family.py`

## Käyttö

Kirjautuminen:

`python pwb.py login`

Tee tekstimuutokset `nimikirjaimet` kaikille artikkeleille, jotka linkittävät artikkeliin "J.R.R. Tolkien":

`python pwb.py replace -ns:0 -ref:"J.R.R. Tolkien" -fix:nimikirjaimet -exceptinsidetag:template -exceptinsidetag:interwiki`

Edellisessä esimerkissä muutokset tehdään linkkien ja luokkamääritysten sisällä, mutta ei malline- tai interwikimerkinnöissä.

Tee tekstimuutokset `kaarmeen-linkit` kaikkien nimiavaruuksien sivuille, jotka sisältävät ulkoisen linkin domainiin kontu.info:

`python pwb.py replace -weblink:"*.kontu.info" -fix:kaarmeen-linkit`

Eräitä `replace`-skriptin parametreja:
- `-file`           Work on all pages given in a local text file. Will read any [[wiki link]] and use these articles. Argument can also be given as "-file:filename".
- `-page`           Only edit a specific page. Argument can also be given as "-page:pagetitle". You can give this parameter multiple times to edit multiple pages.
- `-search`         Work on pages that contain the given search string e.g. -search:"Color"
- `-always`         Don't prompt you for each replacement.
- `-summary:XYZ`    Set the summary message text, bypassing the default edit summaries.
- `-simulate`       Disables writing to the server.
