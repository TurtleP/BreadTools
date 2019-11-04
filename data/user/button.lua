button = class("button")

function button:initialize(x, y, flags)
    self.x = x
    self.y = y

    self.hover = false
    self.content = vector(self.x, self.y)

    if not flags then
        flags = {}
    end

    self.width = flags.width or 42
    self.height = flags.height or 32

    self.image = flags.image or nil
    self.background = flags.background or {1, 1, 1}
    self.foreground = flags.color or {1, 1, 1}
    self.hoverBackground = flags.hover or {1, 1, 1}
    self.callback = flags.callback or function() end

    self.text = flags.text or nil

    if flags.toggled then
        self.toggle = false
    end

    if flags.center then
        self:centerContent()
    end

    if flags.sizeContent then
        self:sizeToContent()
    end

    self.flags = flags
end

function button:onThemeChanged()
    self:initialize(self.x, self.y, self.flags)
end

function button:centerContent()
    local width, height = nil

    if self.image then
        width, height = self.image:getWidth(), self.image:getHeight()
    elseif self.text then
        width, height = self.text.font:getWidth(self.text.string), Fonts.Title:getHeight()
    end

    local x, y = self.x + (self.width - width) / 2, self.y + (self.height - height) / 2

    self.content = vector(x, y)
end

function button:sizeToContent()

end

function button:setImage(image)
    self.image = image
end

function button:draw()
    local color = self.background
    if self.hover then
        color = self.hoverBackground
    end
    love.graphics.setColor(color)

    love.graphics.rectangle("fill", self.x, self.y, self.width, self.height)

    love.graphics.setColor(self.foreground)
    if self.image then
        love.graphics.draw(self.image, self.content.x, self.content.y)
    end

    if not self.text then
        return
    end

    love.graphics.setColor(theme.Interface)
    love.graphics.setFont(self.text.font)
    love.graphics.print(self.text.string, self.content.x, self.content.y)
end

function button:mousemoved(x, y)
    self.hover = _env.CHECKBOUNDS(x, y, 1, 1, self.x, self.y, self.width, self.height)
end

function button:mousepressed()
    if self.toggle ~= nil then
        self.toggle = not self.toggle
    end

    if self.hover then
        self.callback(self)
    end
end
