from textual.app import ComposeResult, App
from test import ModalAboutDialog, ModalInputDialog, ModalJumpDialog
from textual.binding import Binding
from textual.widgets import Label, DataTable, Footer, Static
from rich.json import JSON
from textual.events import Paste
from textual import work

"""
run pipelines to analyze video part!

video format ->
(time stamp in video, "file_path", above average score, total score),

"""


ROWS = [
    ("lane", "swimmer", "country", "time"),
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]

data = r"E:\Projects\2024\Video-Content-Pipeline\output-video\private\cery\text_cache\analyze_data.txt"




from typing import List, Dict, Any
from textual import events

import os
import re


# def _extract_filepaths(text: str) -> List[str]:
#     split_filepaths = []
#     if os.name == "nt":
#         pattern = r'(?:[^\s"]|"(?:\\"|[^"])*")+'
#         split_filepaths = re.findall(pattern, text)
#     else:
#         split_filepaths = shlex.split(text)

#     split_filepaths = shlex.split(text)
#     print(split_filepaths)
#     filepaths = []
#     for i in split_filepaths:
#         item = i.replace("\x00", "").replace('"', "")
#         if os.path.isfile(item):
#             filepaths.append(i)
#         elif os.path.isdir(item):
#             for root, _, files in os.walk(item):
#                 for file in files:
#                     filepaths.append(os.path.join(root, file))
#     return filepaths


# def _build_filesobj(filepaths: List[str]) -> List[Dict[str, Any]]:
#     filesobj = []
#     for i in filepaths:
#         file_name = os.path.basename(i)
#         _, file_ext = os.path.splitext(file_name)
#         file_ext = file_ext.replace(".", "")
#         file_path = i
#         filesobj.append(
#             {
#                 "path": file_path,
#                 "name": file_name,
#                 "ext": file_ext,
#             }
#         )
#     return filesobj

# def getfiles(event: events.Paste) -> List[Dict[str, Any]]:
#     filepaths = _extract_filepaths(event.text)
#     filesobj = []
#     if filepaths:
#         filesobj = _build_filesobj(filepaths)
#     return filesobj

class MyApp(App):
    BINDINGS = [
        Binding("i", "show_input_dialog", "Input Dialog"),
        Binding("a", "show_about_dialog", "About Dialog"),
        Binding("j", "show_jump_dialog", "Jump Dialog"),
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Static(id="content", expand=True)
        yield Footer()

    def action_show_input_dialog(self) -> None:
        self.push_screen(ModalInputDialog("Enter your name:"))

    def action_show_about_dialog(self) -> None:
        self.push_screen(ModalAboutDialog("# About This App\nThis is a simple app to demonstrate modal dialogs."))

    def action_show_jump_dialog(self) -> None:
        self.push_screen(ModalJumpDialog("Jump to:"))

    def on_mount(self) -> None:

        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True
        self.load_txt_file()
        # table.add_columns(*ROWS[0])
        # table.add_rows(ROWS[1:])


    def on_paste(self, event : Paste):
        print("CONSOLE DEBUG", event.text)
        # self.query_one("#content").update(JSON(files))

    @work(thread=True)
    def load_txt_file(self):
        import ast

        table = self.query_one(DataTable)

        with open(data, "r") as f:
            lines = f.readlines()
            _ : dict = ast.literal_eval(lines[0])[0]
            for col in tuple(_):
                table.add_column(col, key=col)
            for line in lines:
                converted_dict : tuple = ast.literal_eval(line)[0] #ast.
                table.add_row(*tuple(converted_dict.values()))

        if "points" in table.columns:
            table.sort("points")
        else:
            print("Column 'points' does not exist in the table.")
            print("Pick from {}".format(table.columns.items()))
    # def action_todoactions

if __name__ == "__main__":
    MyApp().run()