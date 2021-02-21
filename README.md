# rcc
Randomized Caesar Cypher

RCC is a simple implematation of randomized ceaser cypher. The class is a singleton which need to be initialized only once during the runtime of the program. During initialization, it will create a random map for ceaser cypher. During initialization, one can pass a argument (do_not_replace_list) to force some characters to stay as-is after the encoding. By default the following characters stay as-is during encoding:
* space
* period
* forward slash
* backward slash

Example

from rcc import Rcc \n
rcc_obj = Rcc.instance()
test_str = "alaska is a funny pl\\ace"

Output:
ĎǶĎĆBĎ ǺĆ Ď ƬÌ99ǉ ºǶ\ĎƐõ
