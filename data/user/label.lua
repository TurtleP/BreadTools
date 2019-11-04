label = class("label")

function label:initialize(x, y, text, flags)
    self.x = x
    self.y = y

    self.width = 0
    self.height = 0

    if not flags then
        flags = {}
    end

    self.font = flags.font or Fonts.Title
    self.text = love.graphics.newText(self.font, text)
end

function label:draw()
    love.graphics.setColor(theme.Interface)
    love.graphics.setFont(self.font)

    love.graphics.draw(self.text, self.x, self.y)
end
