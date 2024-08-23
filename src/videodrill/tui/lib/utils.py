"""
  add more util functions to help parse data
"""

from ast import literal_eval

def parse_dict(txt : str) -> dict:
  try:
    _crop = txt[txt.index("{"):txt.index("}") + 1]
  except:
    raise ValueError("Input is cut off or length error :{}".format(txt))
  else:
    return literal_eval(_crop)

def parse_tuple(txt : str) -> tuple:
  try:
    _crop = txt[txt.index("("):txt.index(")") + 1]
  except:
    raise ValueError("Input is cut off or length error  :{}".format(txt))
  else:
    return literal_eval(_crop)

def parse_list(txt : str) -> list:
  try:
    _crop = txt[txt.index("["):txt.index("]") + 1]
  except:
    raise ValueError("Input is cut off or length error  :{}".format(txt))
  else:
    return literal_eval(_crop)


def pick_parser(type : str) -> callable:
    if type == "dict":
      return parse_dict

    if type ==  "tuple":
      return parse_tuple

    if type == "list":
      return parse_tuple

    raise TypeError("Type not found {}".format(type))
