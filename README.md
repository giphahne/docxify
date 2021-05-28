# docxify

Encode/decode an arbitrary/(binary) payload in `.docx` transport wrapper.
Memory footprint is independent of payload size (`O(1)` memory size).

Setup:
```sh

$ pip install docxify
```


Usage:
```sh

$ docxify --input-file payload.dat  --output-directory word_docs

```

`--output-directory` is created at run-time; it must not exist
prior to execution.


----




## Encoding schemata

- Base64: good, but I'm nervous about non-alphanumerics

- Base58: probable starting point, provided I can get stream-wise encoding working easily

- hex: fallback from Base58 encoding as stream-wise encoding is trivial to implement

