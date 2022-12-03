# **RSA-salaus**

Tähän repositorioon palautetaa Helsingin yliopiston aineopintojen harjoitustyö kurssilla Tietorakenteet ja algoritmit.

## **Dokumentaatio**

* [Määrittelydokumentti](./dokumentaatio/maarittelydokumentti.md)
* [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
* [Testausdokumentti](./dokumentaatio/testausdokumentti.md)
* [Toteutusdokumentti](./dokumentaatio/toteutusdokumentti.md)

## **Viikkoraportit**

* [Viikko 1](./dokumentaatio/viikkoraportti-01.md)
* [Viikko 2](./dokumentaatio/viikkoraportti-02.md)
* [Viikko 3](./dokumentaatio/viikkoraportti-03.md)
* [Viikko 4](./dokumentaatio/viikkoraportti-04.md)
* [Viikko 5](./dokumentaatio/viikkoraportti-05.md)

## **Käyttöohje**

### Asenna tarvittavat riippuvuudet komennolla
```
poetry install
```

### Suorita ohjelma komennolla
```
poetry run invoke start
```

### Suorita ohjelman testit komennolla
```
poetry run invoke test
```

### Raportoi testikattavuus komennolla
```
poetry run invoke coverage-report
```

### Suorita laatutarkistus komennolla
```
poetry run invoke lint
```
