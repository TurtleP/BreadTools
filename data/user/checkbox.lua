checkbox = class("checkbox")

local PADDING = 8
function checkbox:initialize(x, y, flags)
    self.x = x
    self.y = y

    self.width = 16
    self.height = 16

    self.checked = false
    self.hovered = false

    if not flags then
        flags = {}
    end

    self.text = flags.text or nil
end

function checkbox:draw()
    love.graphics.setColor(theme.Checkbox)
    love.graphics.rectangle("line", self.x, self.y, self.width, self.height)

    if self.text then
        love.graphics.setColor(theme.Interface)
        love.graphics.setFont(Fonts.Title)
        love.graphics.print(self.text, self.x + self.width + PADDING, self.y + (self.height - Fonts.Title:getHeight()) / 2)
    end

    if not self.checked then
        return
    end

    love.graphics.setColor(theme.Interface)
    love.graphics.draw(Images.Check, self.x, self.y)
end

function checkbox:mousepressed(x, y)
    if self.hovered then
        self.checked = not self.checked
    end
end

function checkbox:mousemoved(x, y)
    self.hovered = _env.CHECKBOUNDS(x, y, 1, 1, self.x, self.y, self.width, self.height)
end
