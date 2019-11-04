registry = require "libraries.regedit"
class    = require "libraries.middleclass"
vector   = require "libraries.vector"
tween    = require "libraries.tween"
_env     = require "data.environment"

require "data.interface"

menu = require "states.menu"
titlebar = require "data.user.titlebar"

function love.load()
    menu:load()
end

function love.update(dt)
    menu:update(dt)
end

function love.draw()
    titlebar:draw()
    menu:draw()
end

function love.mousepressed(x, y, button)
    titlebar:mousepressed(x, y, button)
    menu:mousepressed(x, y, button)
end

function love.mousereleased(x, y, button)
    titlebar:mousereleased(x, y, button)
end

function love.mousemoved(x, y, dx, dy)
    titlebar:mousemoved(x, y, dx, dy)
    menu:mousemoved(x, y, dx, dy)
end
