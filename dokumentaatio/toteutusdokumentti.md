# Toteutusdokumentti

RSA salaus perustuu suurten alkulukujen avulla luotuihin julkiseen ja yksityiseen avainpariin. Avainparit muodostetaan alkulukuparin tulosta `modulus`, tämän lisäksi määritellään julkinen ja yksityinen eksponentti. Julkinen eksponentti arvotaan väliltä `[2^{n-1}, 2^{n}]`, jossa `n` on avaimen koko bitteinä.

### Alkulukujen luominen

Ohjelmassa generoidaan satunnaisia lukuja luokassa `KeyGeneraotr`, kunnes ne läpäisevät Eratosthenen sekä Rabin-Millerin alkulukutestit. Kun sattumanvarainen luku läpäisee Rabin-Millerin testin, on se suurella todennäköisyydellä alkuluku.

### Avainten luominen

Julkista avainta voi käyttää ainoastaan viestin salaamiseen ja salattu viesti on purettavissa ainoastaan vastinparina olevalla yksityisellä avaimella. Generoidusta alkupariluvusta muodostetaan modulus `n` alkulukujen tulona. Lisäksi generoidaan julkinen eksponentti `e`, sekä salassa pidettävä yksityinen eksponentti `d`. Julkinen avain muodostuu siis luvuista `(n, e)` ja yksityinen avain muodostuu luvuista `(n, d)`. Generoidut eksponentit sekä modulus tallenetaan luokan `KeyGenerator` attribuutteihin.

### Salaus ja purku

Nyt jos `Alice` haluaa lähettää salatun viestin `Bobille`, tulee `Alicen` ensin saada `Bobin` julkinen avain. Julkinen avain voidaan huoletta lähettää salaamatonta yhteyttä pitkin. Seuraavaksi `Alice` salaa viestin `Bobin` julkisella avaimella ja lähettää salatun viestin `Bobille`. Lopuksi `Bob` voi purkaa vastaanottamansa viestin salauksen omalla yksityisellä avaimella. Salaus toiminnallisuudesta vastaa luokka `Cypher` metodeilla `encrypt` ja `decrypt`.

### Suorituskyky ja aikavaativuus

Ohjelmassa käytetyt algoritmit on luettavuuden takia eriytetty omaan moduuliinsa `utils`.

avaimen koko (bit) | avainparin generointi (sec) | viestin salaus (sec) | salauksen purku (sec)
-------------------|-----------------------------|----------------------|---------------------- 
512                |0.11                         |0.0052                |0.017
1024               |0.56                         |0.037                 |0.032
2048               |15.66                        |0.012                 |0.17
4096               |35.10                        |0.59                  |1.25

Yllä on ohjelmalla mitattuja tuloksia avainparin generoinnista, viestin salauksesta sekä salauksen purkamisesta eri pituisilla avaimilla. Avainten generoinnissa hyödynnetään Eratosthenen seulaa, jonka aikavaativuus on `O(n log log n)`, sekä Rabin-Millerin algoritmia, jonka aikavaativuus on `O(k log^3 n)`. Tilavaativuus molemmissa käytetyissä algoritmeissa on `O(1)`.

Rabin-Millerin algoritmi perustuu todennäköisyyteen. Todennäköisyys, että testin läpäisee luku, joka ei ole alkuluku on `1/4^k`.


## Puutteet ja parannusehdotukset

Ohjelman graafinen käyttöliittymä jäi hieman yksipuoliseksi käytännön haasteista johtuen. Kivy kirjastolla on mahdollista tehdä siistejä sekä responsiivisa käyttöliittymiä, mutta tähän pitäisi perehtyä hieman tarkemmin. Tällä hetkellä osa käyttöliittymän elementeistä menee hieman päällekkäin. Viestin salausta ja salatun viestin lähettämistä ja vastaanottamista voisi myös olla miellekästä testata.


### Lähteet

- https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
- https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test