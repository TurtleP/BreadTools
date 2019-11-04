scrollbar = class("scrollbar")

function scrollbar:initialize(x, y, flags)
    self.x = x
    self.y = y

    self.width = 2
    self.open = false

    if not flags then
        flags = {}
    end

    self.height = flags.height or 32
    self.openTween = tween.new(0.10, self, {x = x - 8, width = 12}, "linear")

    self.progressHeight = self.height / 2
end

function scrollbar:update(dt)
    if self.open then
        self.openTween:update(dt)
    else
        self.openTween:reset()
    end
end

function scrollbar:draw()
    love.graphics.setColor(theme.Scrollbar.Background)
    if self.open then
        love.graphics.rectangle("fill", self.x, self.y, self.width, self.height)
    end

    love.graphics.setColor(theme.Scrollbar.Body)
    love.graphics.rectangle("fill", self.x, self.y, self.width, self.progressHeight)
end

function scrollbar:mousemoved(x, y)
    self.open = _env.CHECKBOUNDS(x, y, 1, 1, self.x - 2, self.y, self.width + 4, self.height)
end
