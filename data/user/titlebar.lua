local titlebar = class("titlebar")

require "data.user.button"

function titlebar:initialize()
    self.x = 0
    self.y = 0

    self.width = _env.WINDOW_W
    self.height = 32

    self.dragging = false
    self.position = {0, 0}

    self:createButtons()

    self.handleSize = (self.width - (#self.buttons * 42))
    self.header = love.graphics.newText(Fonts.Title, love.window.getTitle())
end

function titlebar:onThemeChanged()
    self:createButtons()
end

function titlebar:createButtons()
    self.buttons = {}

    self.buttons[1] = button:new(self.width - 42, self.y, {image = Images.CloseButton,
        background = theme.Background,
        hover = {1, 0, 0},
        callback = love.event.quit,
        center = true,
        color = theme.Interface
    })

    self.buttons[2] = button:new(self.width - 84, self.y, {image = Images.MaximizeButton,
        background = theme.Background,
        hover = theme.Highlights.Button,
        center = true,
        color = theme.Disabled.Button
    })

    self.buttons[3] = button:new(self.width - 126, self.y, {image = Images.MinimizeButton,
        background = theme.Background,
        hover = theme.Highlights.Button,
        center = true,
        color = theme.Disabled.Button
    })

    local icon = Images.Moon
    if _env.THEME == "dark" then
        icon = Images.Sun
    end

    self.buttons[4] = button:new(self.width - 168, self.y, {image = icon,
        background = theme.Background,
        hover = theme.Highlights.Button,
        callback = function(button)
            if _env.THEME == "light" then
                theme:set("dark")
                return
            end
            theme:set("light")
        end,
        center = true,
        color = theme.Interface,
        toggled = true,
    })
end

function titlebar:draw()
    love.graphics.setColor(theme.Interface)
    love.graphics.draw(self.header, 12, self.y + (self.height - self.header:getHeight()) / 2)

    _env.RENDERGROUP(self.buttons)
end

function titlebar:mousepressed(x, y, button)
    if button ~= 1 then
        return
    end

    local pass = true
    for key, value in ipairs(self.buttons) do
        if _env.CHECKBOUNDS(x, y, 1, 1, value.x, value.y, value.width, value.height) then
            pass = false
            break
        end
    end

    if pass then
        if y > 32 then
            return
        end
        love.mouse.setRelativeMode(true)

        self.dragging = true
        self.position = {x, y}
        return
    end

    _env.MOUSEGROUP(self.buttons, "mousepressed", x, y)
end

function titlebar:mousereleased(x, y, button)
    if self.dragging then
        love.mouse.setRelativeMode(false)
        love.mouse.setPosition(unpack(self.position))
        self.dragging = false
    end
end

function titlebar:mousemoved(x, y, dx, dy)
    if self.dragging then
        local WINX, WINY, display = love.window.getPosition()

        local target_x = WINX + dx
        local target_y = WINY + dy

        love.window.setPosition(target_x, target_y, display)
        return
    end

    _env.MOUSEGROUP(self.buttons, "mousemoved", x, y)
end

return titlebar:new()
