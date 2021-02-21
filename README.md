# rcc
Randomized Caesar Cypher

RCC is a simple implematation of randomized ceaser cypher. The class is a singleton which need to be initialized only once during the runtime of the program. During initialization, it will create a random map for ceaser cypher. During initialization, one can pass a argument (do_not_replace_list) to force some characters to stay as-is after the encoding. By default the following characters stay as-is during encoding:
* space
* period
* forward slash
* backward slash

test.py shows an example of how to initialize the encoder and use it.
