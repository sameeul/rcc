from rcc import Rcc
rcc = Rcc.instance()
test_str = "alaska is a funny pl\\ace."
encoded_str = rcc.encode(test_str)
print(encoded_str)
test_str = "This is great!"
encoded_str = rcc.encode(test_str)
print(encoded_str)
