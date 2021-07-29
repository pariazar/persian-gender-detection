# Persian gender detection

A simple Python package to detect gender by Persian first name. (With more than 25K names)

</br>

## Installation
first install requirements with below command: </br>
``` pip install -r requirements.txt ```

then intall PGD from pypip: </br>
``` pip install PGD ```

</br>

## Example:

```

import pgd

print(pgd.detectGender('علی'))
print(pgd.detectGender('حآمد'))
print(pgd.detectGender('ندا'))
print(pgd.detectGender('مهدي'))
print(pgd.detectGender('سارا'))
print(pgd.detectGender('می5نا'))
print(pgd.detectGender('مری97145م'))


```

That would result in:

```

male
male
female
male
female
female
female

```