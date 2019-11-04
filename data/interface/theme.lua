theme = {}

local themes = {}
function theme:load()
    local items = love.filesystem.getDirectoryItems("data/themes")
    for i = 1, #items do
        local name = items[i]:gsub(".lua", "")
        themes[name] = require("data/themes/" .. name)
    end
end

function theme:get(theme)
    if not theme then
        theme = "light"
    end
    return themes[theme]
end

function theme:set(theme)
    local data = themes[theme]

    -- merge with globals!
    for key, value in pairs(themes.global) do
        data[key] = value
    end

    -- apply to the theme
    for key, value in pairs(data) do
        self[key] = value
    end

    -- change background color
    love.graphics.setBackgroundColor(self.Background)

    _env.THEME = theme

    if not titlebar then
        return
    end
    titlebar:onThemeChanged()

    if not menu then
        return
    end
    menu:onThemeChanged()

    love.filesystem.write("theme.txt", theme)
end

theme:load()
