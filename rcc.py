"""
Currently the following code blocks are supported
0000..007F; Basic Latin
0080..00FF; Latin-1 Supplement
0100..017F; Latin Extended-A
0180..024F; Latin Extended-B
"""

class Rcc(object):
    _instance = None
    _replace_map = None
    _do_not_replace_list = sorted([' ', '.', "\\", '/']) # keep this sorted
    _char_set_range_map = {'Basic Latin':(0x0000, 0x007F),
                           'Latin-1 Supplement':(0x0080, 0x00FF),
                           'Latin Extended-A':(0x0100, 0x017F),
                           'Latin Extended-B':(0x0180, 0x024F),
                          }
    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls, do_not_replace_list =[]):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
            import random

            replace_list = []
            if do_not_replace_list != []:
              cls._do_not_replace_list = sorted(do_not_replace_list)

            do_not_replace_map = {}

            for char_set in cls._char_set_range_map:
              start_val = cls._char_set_range_map[char_set][0]
              end_val = cls._char_set_range_map[char_set][1] + 1
              for i in range(start_val, end_val):
                c = chr(i)
                replace_list.append(c)
                if c in cls._do_not_replace_list:
                  do_not_replace_map[c] = i

            print(do_not_replace_map)
            new_replace_list = []
            last_split_index = -1
            for c in cls._do_not_replace_list:
              split_index = do_not_replace_map[c]
              new_replace_list = new_replace_list+replace_list[last_split_index+1:split_index]
              last_split_index = split_index

            new_replace_list = new_replace_list+replace_list[last_split_index+1:]

            random.shuffle(new_replace_list)

            shuffled_replace_list = []
            last_split_index = 0
            split_count = 0
            for c in cls._do_not_replace_list:
              split_index = do_not_replace_map[c] - split_count
              shuffled_replace_list = shuffled_replace_list+new_replace_list[last_split_index:split_index]+[c]
              last_split_index = split_index
              split_count += 1

            shuffled_replace_list = shuffled_replace_list+new_replace_list[last_split_index:]
            cls._replace_map = dict(zip(replace_list, shuffled_replace_list))

        return cls._instance

        
    @classmethod
    def encode(cls, input_str):
      output_str =''
      for c in input_str:
        output_str += cls._replace_map[c]
      return output_str
