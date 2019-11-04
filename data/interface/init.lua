local PATH = (...):gsub("%.init$", "")

require(PATH .. ".theme")

if love.filesystem.getInfo("theme.txt") then
    _env.THEME = love.filesystem.read("theme.txt")
end

theme:set(_env.THEME)

require(PATH .. ".images")
require(PATH .. ".fonts")
