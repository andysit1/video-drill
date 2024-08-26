"""
  add more util functions to help parse data
"""

from ast import literal_eval
import subprocess


def open_video(in_filename : str):
  try:
    subprocess.run(['LosslessCut', in_filename], check=True)
  except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
  except FileNotFoundError:
    print("Media player executable not found.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

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

if __name__ == "__main__":
  in_file = r"E:\Projects\2024\Video-Content-Pipeline\output-video\private\cery\clips\video00.mp4"
  open_video(in_file)