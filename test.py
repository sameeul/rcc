from rcc import Rcc
rcc_obj = Rcc.instance()
test_str = "alaska"
print(rcc_obj.encode(test_str))
rcc_obj_2 = Rcc.instance()
print(rcc_obj_2.encode(test_str))
