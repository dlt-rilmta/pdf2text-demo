# DEMO

Cél: megnézni, milyen eszközökkel hogyan lehet szöveget kinyerni PDF fájlokból.
Ezután meg kéne nézni, hogy melyik eszköz a legjobb nekünk.

## Eszközök

* ~~[pypdf4](https://github.com/claird/PyPDF4)~~
  * A *pypdf* nem alkalmas szöveg kinyerésére!
* ~~[pdfrw](https://github.com/pmaupin/pdfrw)~~ (kicsit elárvultnak tűnik, de ki lehet próbálni)
  * A *pypdf*-hez hasonlóan ez sem nem alkalmas szöveg kinyerésére!
* [textract](https://github.com/deanmalmgren/textract)
  * A telepítése gondot okozhat: függ a `pocketsphinx` python csomagtól, amihez linuxon kellenek a `libpulse-dev` és a `libasound2-dev` debian csomagok is! Ezért a Pipfile-ból is kiszedtem.
  * A csomag a közlönyök esetében nem tudta jól megtippelni a használt karakterkódolást, ezt kézzel kell 'latin2'-re állítani.
* [tika-python](https://github.com/chrismattmann/tika-python)

## Előfeltételek

* python 3.6
* [`pipenv`](https://pipenv.readthedocs.io/en/latest/)
* fejlesztői környezet létrehozása: `pipenv update`

## Futtatás

```sh
make all
```

Az első futás hosszabb ideig fog tartani! A parancs letölt 4 PDF fájlt a `pdf/`
könyvtárba, kinyeri belőle a szöveget a fenti eszközökkel, az eredményt a
`txt/<eszkoz>/` könyvtárba írja. 
