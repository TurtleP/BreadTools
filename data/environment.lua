return
{
    WINDOW_W = 400,
    WINDOW_H = 400,

    THEME = "light",

    VERSION = "0.1.0",

    CHECKBOUNDS = function(x, y, width, height, x2, y2, width2, height2)
        return x + width > x2 and
               x < x2 + width2 and
               y > y2 and
               y < y2 + height2
    end,

    RENDERGROUP = function(group)
        for key, value in pairs(group) do
            if value.draw then
                value:draw()
            end
        end
    end,

    MOUSEGROUP = function(group, which, x, y)
        for key, value in pairs(group) do
            if value[which] then
                value[which](value, x, y)
            end
        end
    end
}
