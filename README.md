# buid

A better UID generator with more readable, memorable content.

## Usages

```python
from buid import BUID
>>> b = BUID()
>>> b
BUID('hahi-fugo-bino-deca')
>>> BUID('hahi-fugo-bino-deca')
BUID('hahi-fugo-bino-deca')
>>> str(b)
'hahi-fugo-bino-deca'
>>> BUID(VOWEL_CHARS='ae')
BUID('bena-rama-texa-yewe')
>>> BUID(SEPARATOR_CHARS='_')
BUID('mube_xaro_wudu_wivo')
>>> BUID(format='CVC-CVC-CVC-CVC')
BUID('kab-doj-xem-giz')
```
## Meta

Jimmy Lin <b00502013@gmail.com>

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/j3ygithub/](https://github.com/j3ygithub/)

## Contributing

1. Fork it (<https://github.com/j3ygithub/buid/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
