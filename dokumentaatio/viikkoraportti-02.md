# Viikkoraportti 2

## Mitä olen tehnyt tällä viikolla?

Tällä viikolla perehdyin alkulukujen teoriaan ja alustin siltä pohjalta python-ohjelman. Ohjelma on mahdollista suorittaa komentoriviltä.

## Miten ohjelma on edistynyt?

Ohjelma on alustettu ja sillä voi generoida alkulukuja `n` syötteeseen asti. Generoituja alkulukuja testataan `pytest` kirjastolla. Myös testikattavuusraportointi on otettu käyttöön. Ohjelmassa on kaksi tapaa generoida alkulukuja. Ensimmäinen tapa lisää listaan luvun `n` mikäli se ei ole jaollinen luvuilla `[2,n-1]`. Toinen tapa on generoida lista luvuista `[2,n]`ja seuloa niistä Eratosthenen seulalla pois kaikki ei alkuluvut.

## Mitä opin tällä viikolla?

Alkuluvut ovat lukua `1` suurempia luonollisia lukuja, jotka ovat jaollisia vain itsellään tai luvulla `1`. Eratosthenen seula on yksinkertaisimpia algoritmeja laskea alkulukuja, mutta se on huono vaihtoehto suurten alkulukujen etsimiseen. Koska RSA-salauksen toiminta perustuu nimenomaan suurten alkulukujen käsittelyyn, tämä ei liene paras vaihtoehto salausavainten generointiin.

## Mitä teen seuraavaksi?

Seuraavalla viikolla perehdyn lisää aiheeseen ja toteutan salausavainten generoinnin.

## Työaika

4h
