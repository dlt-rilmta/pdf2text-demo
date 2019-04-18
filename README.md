# DEMO

Cél: megnézni, milyen eszközökkel hogyan lehet szöveget kinyerni PDF fájlokból.
Ezután meg kéne nézni, hogy melyik eszköz a legjobb nekünk.

## Eszközök

* [pypdf4](https://github.com/claird/PyPDF4)
* [textract](https://github.com/deanmalmgren/textract)
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
