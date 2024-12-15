"""Lab 01.03 - SwapVar"""
def convert_string_to_tuples(text_in):
  values = text_in.strip('()').split(', ')
  return tuple(map(float, values))

def swap_var() :
    """Lab 01.03 - SwapVar"""
    laongdao_data = convert_string_to_tuples(input())
    my_list = list(laongdao_data)
    new_list = [my_list[1],my_list[0]]
    print(tuple(new_list))
swap_var()
