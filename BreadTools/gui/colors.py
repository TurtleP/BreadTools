from ..storage import Storage
import toml

COLORS = None
with open(Storage.resolve_data("colors.toml"), "r") as file:
    COLORS = toml.load(file)

color_mode_str = "light"
color_mode = False

color_modes = {
    "False": "light",
    "True": "dark"
}


def toggle_colors():
    global color_mode, color_mode_str
    color_mode = not color_mode

    color_mode_str = color_modes[str(color_mode)]

    print(f"color mode is now {color_mode_str}")

    return color_mode


def get_color(color):
    if color in COLORS[color_mode_str]:
        return f"#{COLORS[color_mode_str][color]}"
