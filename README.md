Bu alıştırmaya kadar geldiğin için tebrikler! Şimdi bir Sudoku Validator implement edeceğiz. Amaç basit: verilen bir **9x9 Sudoku grid**’inin geçerli olup olmadığını belirlemek! 


## Kurallar

Bir Sudoku ancak ve ancak aşağıdaki koşullar sağlanıyorsa geçerlidir:

-Her satır 1’den 9’a kadar tüm sayıları içerir
-Her sütun 1’den 9’a kadar tüm sayıları içerir
-Dokuz adet 3x3’lük küçük karelerin her biri 1’den 9’a kadar olan sayıları içerir


## Veri Modeli

Bir Sudoku grid’i, Python’da list of lists şeklinde temsil edilecektir:

```python
grid = [
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,7,2,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],

    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],

    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4]
]
```

Bu yapıyı göz önünde bulundurduğunda, `i`’nci satır ve `j`’nci sütundaki hücreye şu şekilde erişebilirsin:

```python
grid[i][j]
```

💡 Unutma: Python list index’leri 0’dan başlar, yani `i` ve `j` değerleri 0 ile 8 arasındadır.

## Alıştırma

`sudoku.py`dosyasını aç ve `sudoku_validator()` method’unu implement et.Kodunun çalışıp çalışmadığını kontrol etmek için testleri şu komutla çalıştır:

```bash
make
```
