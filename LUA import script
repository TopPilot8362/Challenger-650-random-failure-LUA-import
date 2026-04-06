```lua
local socket = require("socket")
local server = socket.udp()
server:setsockname("127.0.0.1", 49000) -- Port to listen on

while true do
    local msg = server:receive()
    if msg then
        if string.sub(msg, 1, 5) == "FAIL:" then
            local failure_type = string.sub(msg, 6)
            -- TODO: Implement failure handling based on failure_type
            if failure_type == "HYDRAULIC" then
                -- Trigger hydraulic failure
            elseif failure_type == "ELECTRICAL" then
                -- Trigger electrical failure
            end
            -- Add additional failure types as needed
        end
    end
    -- Optional: add a small delay to reduce CPU usage
end
