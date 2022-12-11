# Testausdokumentti

## Yksikkötestaus

Tässä projektissa on toteutettu automaatiotestit yksikkötestien tasolla hyödyntäen pythonin unittest kirjastoa. Testeissä otetaan huomioon kaikki moduulit lukuunottamatta pääohjelmaa `main`. Lisäksi moduulissa `primegenerator` jää tarkistamatta haara, jossa funktio luo alkulukuparin, mutta näiden lukujen samanarvoisuutta ei kyetä testien avulla vertaamaan. Tämä johtuu siitä, että alkulukujen generointi pohjautuu satunnaisuuteen.


## Suorituskyky

Sovelluksessa voi generoida avaimia pituuksilla `[512< n < 4096] | (n = 2^i, 9<= i <= 12)`. Tässä on joitakin mitattuja tuloksia avainparin generoinnista, viestin salauksesta sekä salauksen purkamisesta.

avaimen koko (bit) | avainparin generointi (sec) | viestin salaus (sec) | salauksen purku (sec)
-------------------|-----------------------------|----------------------|---------------------- 
512                |0.11                         |0.0052                |0.017
1024               |0.56                         |0.037                 |0.032
2048               |15.66                        |0.012                 |0.17
4096               |35.10                        |0.59                  |1.25

## Testikattavuus

Testikattavuus on 97%.

![coverage](../images/coverage-report.png)

## Testien suorittaminen

Ohjelman testit voi suorittaa komennola
```
poetry run invoke test
```

Kattavuuden testauksen ja raportin voi luoda komennoilla
```
poetry run invoke coverage
poetry run invoke coverage-report
```

Kattavuusraportti generoituu hakemistoon
```
/htmlcov/index.html
```


