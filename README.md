# docxify

Encode/decode an arbitrary/(binary) payload in `.docx` transport wrapper.
Memory footprint is independent of payload size (`O(1)` memory size).


Usage:
```sh

$ docxify --input-file payload.dat  --output-directory word_docs

```


## Encoding schemata

- Base64: good, but I'm nervous about non-alphanumerics

- Base58: probable starting point, provided I can get stream-wise encoding working easily

- hex: fallback from Base58 encoding as stream-wise encoding is trivial to implement

