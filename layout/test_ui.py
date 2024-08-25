from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, DataTable


class UtilityContainersExample(App):
    CSS_PATH = "utility_containers.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(classes="column"):
                yield DataTable()
            with Vertical(classes="column"):
                yield Static("volume graph")
                yield Static("more indepth stats")

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.show_cursor = True
        table.cursor_type = "row"
        table.zebra_stripes = True

        table.add_column(label="index")

        for i in range(0, 100):
            table.add_row(i)


if __name__ == "__main__":
    app = UtilityContainersExample()
    app.run()