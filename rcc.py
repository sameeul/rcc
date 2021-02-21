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
    _to_map_range = [(0x0030, 0x0039), (0x0061,0x007A)]
    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls, do_not_replace_list =[]):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
            import random
            to_map_list = []
            for char_range in cls._to_map_range:
              start_val = char_range[0]
              end_val = char_range[1] + 1
              for i in range(start_val, end_val):
                to_map_list.append(chr(i))
            
            to_map_length = len(to_map_list)

            replace_value_list = []
            replace_key_list = []
            if do_not_replace_list != []:
              cls._do_not_replace_list = sorted(do_not_replace_list)
            do_not_replace_map = {}

            count = 0
            for char_set in cls._char_set_range_map:
              start_val = cls._char_set_range_map[char_set][0]
              end_val = cls._char_set_range_map[char_set][1] + 1
              for i in range(start_val, end_val):
                map_index = count % to_map_length
                replace_key_list.append(chr(i))
                replace_value_list.append(to_map_list[map_index])
                if chr(i) in cls._do_not_replace_list:
                  do_not_replace_map[chr(i)] = count
                count += 1

            new_replace_list = []
            last_split_index = -1
            for c in cls._do_not_replace_list:
              split_index = do_not_replace_map[c]
              new_replace_list = new_replace_list+replace_value_list[last_split_index+1:split_index]
              last_split_index = split_index

            new_replace_list = new_replace_list+replace_value_list[last_split_index+1:]

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
            cls._replace_map = dict(zip(replace_key_list, shuffled_replace_list))

        return cls._instance

        
    @classmethod
    def encode(cls, input_str):
      output_str =''
      for c in input_str:
        output_str += cls._replace_map[c]
      return output_str
