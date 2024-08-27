from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, MarkdownViewer


class ModalAboutDialog(ModalScreen[type(None)]):
    DEFAULT_CSS = """
    ModalAboutDialog {
        align: center middle;
        width: 80%;
        height: 80%;
    }

    ModalAboutDialog > Vertical {
        background: $panel;
        height: auto;
        width: auto;
        border: thick $primary;
    }

    ModalAboutDialog > Vertical > * {
        width: auto;
        height: auto;
    }

    ModalAboutDialog MarkdownViewer {
        align-horizontal: center;
        height: 24;
        width: 72;
    }

    ModalAboutDialog Button {
        margin-top: 1;
    }

    ModalAboutDialog #buttons {
        width: 100%;
        align-horizontal: center;
    }
    """
    """The default styling for the about dialog."""

    BINDINGS = [
        Binding("escape", "app.pop_screen", "", show=False),
        Binding("enter", "app.pop_screen", "", show=False),
    ]
    """Bindings for the dialog."""

    def __init__(
            self,
            content: str,
    ) -> None:
        """Initialise the input dialog.

        Args:
            content: The Markdown content.
        """
        super().__init__()
        self.content = content

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        with Vertical():
            yield MarkdownViewer(
                self.content,
                show_table_of_contents=False,
            )
            with Horizontal(id="buttons"):
                yield Button("OK", id="ok", variant="primary")

    def on_mount(self) -> None:
        """Move focus to viewer for immediate user interactivity."""
        self.query_one(MarkdownViewer).focus()

    @on(Button.Pressed, "#ok")
    def ok_clicked(self) -> None:
        self.dismiss()
