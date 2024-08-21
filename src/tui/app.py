from textual.app import ComposeResult, App
from test import ModalAboutDialog, ModalInputDialog, ModalJumpDialog
from textual.binding import Binding
from textual.widgets import Label, DataTable, Footer
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


class MyApp(App):
    BINDINGS = [
        Binding("i", "show_input_dialog", "Input Dialog"),
        Binding("a", "show_about_dialog", "About Dialog"),
        Binding("j", "show_jump_dialog", "Jump Dialog"),
    ]


    def compose(self) -> ComposeResult:
        yield Label("Press 'i' for Input Dialog, 'a' for About Dialog, 'j' for Jump Dialog")
        yield DataTable()
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
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    @work
    def load_data_side_by_side(self):
        pass
    

    # def action_todoactions

if __name__ == "__main__":
    MyApp().run()