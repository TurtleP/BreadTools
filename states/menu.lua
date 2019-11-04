local menu = {}

require "data.user.scrollbar"
require "data.user.checkbox"
require "data.user.label"
require "data.user.button"

function menu:load()
    self.scrollbar = scrollbar:new(_env.WINDOW_W - 4, 32, {height = _env.WINDOW_H - 32})

    self.checkboxes =
    {
        -- GENERAL
        checkbox:new(25, 85, {text = "Toggle Hidden Files"}),
        checkbox:new(25, 115, {text = "Open Regedit"}),
        checkbox:new(25, 145, {text = "Restart Explorer"}),
        checkbox:new(25, 175, {text = "Show File Extensions"}),
        -- COMMAND LINE
        checkbox:new(25, 255, {text = "Open Bash Here"}),
        checkbox:new(25, 285, {text = "Open Command Prompt Here"}),
        checkbox:new(50, 315, {text = "As Administator"}),
        checkbox:new(25, 345, {text = "Open PowerShell Here"}),
        checkbox:new(50, 375, {text = "As Administator"})
    }

    self.headers =
    {
        label:new(10, 40, "General", {font = Fonts.Header}),
        label:new(10, 210, "Command Line", {font = Fonts.Header})
    }

    self:onThemeChanged()
end

function menu:onThemeChanged()
    self.button = button:new(_env.WINDOW_W - 112, _env.WINDOW_H - 50, {background = theme.Button,
        hover = theme.Highlights.Button,
        text = {string = "Install", font = Fonts.Title},
        center = true,
        width = 80
    })
end

function menu:update(dt)
    self.scrollbar:update(dt)
end

function menu:draw()
    self.scrollbar:draw()

    _env.RENDERGROUP(self.checkboxes)

    _env.RENDERGROUP(self.headers)

    self.button:draw()
end

function menu:mousepressed(x, y)
    _env.MOUSEGROUP(self.checkboxes, "mousepressed", x, y)
end

function menu:mousemoved(x, y, dx, dy)
    _env.MOUSEGROUP(self.checkboxes, "mousemoved", x, y)
    self.scrollbar:mousemoved(x, y)
    self.button:mousemoved(x, y)
end

return menu
