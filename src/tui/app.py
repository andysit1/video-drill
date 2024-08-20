from textual.app import ComposeResult, App
from src.tui.test import ModalAboutDialog, ModalInputDialog, ModalJumpDialog
from textual.binding import Binding
from textual.widgets import Label

class MyApp(App):
    BINDINGS = [
        Binding("i", "show_input_dialog", "Input Dialog"),
        Binding("a", "show_about_dialog", "About Dialog"),
        Binding("j", "show_jump_dialog", "Jump Dialog"),
    ]

    def compose(self) -> ComposeResult:
        yield Label("Press 'i' for Input Dialog, 'a' for About Dialog, 'j' for Jump Dialog")

    def action_show_input_dialog(self) -> None:
        self.push_screen(ModalInputDialog("Enter your name:"))

    def action_show_about_dialog(self) -> None:
        self.push_screen(ModalAboutDialog("# About This App\nThis is a simple app to demonstrate modal dialogs."))

    def action_show_jump_dialog(self) -> None:
        self.push_screen(ModalJumpDialog("Jump to:"))

if __name__ == "__main__":
    MyApp().run()