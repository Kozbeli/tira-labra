# Toteutusdokumentti

RSA salaus perustuu suurten alkulukujen avulla luotuihin julkiseen ja yksityiseen avainpariin. Avainparit muodostetaan alkulukuparin tulosta `modulus`, tämän lisäksi määritellään julkinen ja yksityinen eksponentti. Julkinen eksponentti arvotaan väliltä `[2^{n-1}, 2^{n}]`, jossa `n` on avaimen koko bitteinä.

### Alkulukujen luominen

Ohjelmassa generoidaan satunnaisia lukuja, kunnes ne läpäisevät Rabin-Millerin alkulukutestin. Kun sattumanvarainen luku läpäisee Rabin-Millerin testin, on se suurella todennäköisyydellä alkuluku.

### Avainten luominen

Julkista avainta voi käyttää ainoastaan viestin salaamiseen ja salattu viesti on purettavissa ainoastaan vastinparina olevalla yksityisellä avaimella. Generoidusta alkupariluvusta muodostetaan modulus `n` alkulukujen tulona. Lisäksi generoidaan julkinen eksponentti `e`, sekä salassa pidettävä yksityinen eksponentti `d`. Julkinen avain muodostuu siis luvuista `(n, e)` ja yksityinen avain muodostuu luvuista `(n, d)`. 

### Salaus ja purku

Nyt jos `Alice` haluaa lähettää salatun viestin `Bobille`, tulee `Alicen` ensin saada `Bobin` julkinen avain. Julkinen avain voidaan huoletta lähettää salaamatonta yhteyttä pitkin. Seuraavaksi `Alice` salaa viestin `Bobin` julkisella avaimella ja lähettää salatun viestin `Bobille`. Lopuksi `Bob` voi purkaa vastaanottamansa viestin salauksen omalla yksityisellä avaimella.

Näin Kummankin yksityinen avain on pysynyt piilossa ja ainoastaan julkinen avain sekä salattu viesti on paljastunut muulle liikenteelle. Selkokielinen viesti on ollut näkyvillä vain lähettäjällä sekä vastaanottajalla.

### Suorituskyky

avaimen koko (bit) | avainparin generointi (sec) | viestin salaus (sec) | salauksen purku (sec)
-------------------|-----------------------------|----------------------|---------------------- 
64                 |0.00836801528930664          |4.982948303222656e-05 |7.891654968261719e-05
128                |0.014656305313110352         |5.936622619628906e-05 |0.00011777877807617188
256                |0.04590725898742676          |0.00032520294189453125|0.0007309913635253906
512                |0.17227673530578613          |0.0017366409301757812 |0.0036115646362304688
1024               |1.0259060859680176           |0.010691404342651367  |0.023462772369384766
2048               |10.3712477684021             |0.08822202682495117   |0.1667191982269287
4096               |145.04743146896362           |0.5353426933288574    |1.2123470306396484