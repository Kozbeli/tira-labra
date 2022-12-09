# Toteutusdokumentti

RSA salaus perustuu suurten alkulukujen avulla luotuihin julkiseen ja yksityiseen avainpariin. Avainparit muodostetaan alkulukuparin tulosta `modulus`, tämän lisäksi määritellään julkinen ja yksityinen eksponentti. Julkinen eksponentti arvotaan väliltä `[2^{n-1}, 2^{n}]`, jossa `n` on avaimen koko bitteinä.

### Alkulukujen luominen

Ohjelmassa generoidaan satunnaisia lukuja, kunnes ne läpäisevät Rabin-Millerin alkulukutestin. Kun sattumanvarainen luku läpäisee Rabin-Millerin testin, on se suurella todennäköisyydellä alkuluku.

### Avainten luominen

Julkista avainta voi käyttää ainoastaan viestin salaamiseen ja salattu viesti on purettavissa ainoastaan vastinparina olevalla yksityisellä avaimella. Generoidusta alkupariluvusta muodostetaan modulus `n` alkulukujen tulona. Lisäksi generoidaan julkinen eksponentti `e`, sekä salassa pidettävä yksityinen eksponentti `d`. Julkinen avain muodostuu siis luvuista `(n, e)` ja yksityinen avain muodostuu luvuista `(n, d)`. 

### Salaus ja purku

Nyt jos `Alice` haluaa lähettää salatun viestin `Bobille`, tulee `Alicen` ensin saada `Bobin` julkinen avain. Julkinen avain voidaan huoletta lähettää salaamatonta yhteyttä pitkin. Seuraavaksi `Alice` salaa viestin `Bobin` julkisella avaimella ja lähettää salatun viestin `Bobille`. Lopuksi `Bob` voi purkaa vastaanottamansa viestin salauksen omalla yksityisellä avaimella.

Näin Kummankin yksityinen avain on pysynyt piilossa ja ainoastaan julkinen avain sekä salattu viesti on paljastunut muulle liikenteelle. Selkokielinen viesti on ollut näkyvillä vain lähettäjällä sekä vastaanottajalla.

### Aikavaativuus