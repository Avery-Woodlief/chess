local queries = {}

-- Safely checks whether an object exposes an attribute/index.
function queries.hasattr(object, attribute)
    local success, value = pcall(function()
        return object[attribute]
    end)

    return success
end

-- Like hasattr(), but also requires the value to be non-nil.
function queries.has_value(object, attribute)
    local success, value = pcall(function()
        return object[attribute]
    end)

    return success and value ~= nil
end

-- Safely retrieves an attribute/index.
-- Returns: success, value
function queries.getattr(object, attribute)
    return pcall(function()
        return object[attribute]
    end)
end

-- Forces Python attribute access when running through Lupa.
-- Useful for Python objects that also define __getitem__.
-- Returns: success, value
function queries.python_getattr(object, attribute)
    if python == nil or python.as_attrgetter == nil then
        return false, "python.as_attrgetter is unavailable"
    end

    local success, value = pcall(function()
        return python.as_attrgetter(object)[attribute]
    end)

    if success then
        return value
    end
    return tostring(attribute).." is not an attribute of "..tostring(object)
end

-- Safely looks up a square on a Python-backed board.
-- destination is expected to be a Python tuple/list using indexes 0 and 1.
-- Returns: success, target
function queries.board_lookup(board, destination)
    local success, target = pcall(function()
        return board[destination[0]][destination[1]]
    end)

    if not success then
        print("Board lookup failed:", target)
    end

    return success, target
end

-- Returns true when the board lookup succeeds.
function queries.valid_destination(board, destination)
    local success, target = queries.board_lookup(board, destination)
    return success
end

-- Returns true when a square exists and contains no piece.
-- Returns nil if the destination itself is invalid.
function queries.empty_square(board, destination)
    local success, target = queries.board_lookup(board, destination)

    if not success then
        return nil
    end

    return target == nil
end

-- Returns true when a square exists and contains something.
-- Returns nil if the destination itself is invalid.
function queries.occupied_square(board, destination)
    local success, target = queries.board_lookup(board, destination)

    if not success then
        return nil
    end

    return target ~= nil
end

-- Compares teams safely.
function queries.same_team(piece_a, piece_b)
    if piece_a == nil or piece_b == nil then
        return false
    end

    if not queries.has_value(piece_a, "team") or not queries.has_value(piece_b, "team") then
        return false
    end

    return piece_a.team == piece_b.team
end

-- Returns true when destination contains a friendly piece.
-- Returns nil for an invalid destination.
function queries.friendly_square(piece, board, destination)
    local success, target = queries.board_lookup(board, destination)

    if not success then
        return nil
    end

    if target == nil or not queries.has_value(target, "team") then
        return false
    end

    return target.team == piece.team
end

-- Returns true when destination contains an enemy piece.
-- Returns nil for an invalid destination.
function queries.enemy_square(piece, board, destination)
    local success, target = queries.board_lookup(board, destination)

    if not success then
        return nil
    end

    if target == nil or not queries.has_value(target, "team") then
        return false
    end

    return target.team ~= piece.team
end

-- General movement query:
-- invalid destination -> false
-- empty square        -> true
-- friendly piece      -> false
-- enemy piece         -> true
function queries.can_move(piece, board, destination)
    local success, target = queries.board_lookup(board, destination)

    if not success then
        return false
    end

    if target == nil or not queries.has_value(target, "team") then
        return true
    end

    return target.team ~= piece.team
end

-- Checks a piece's custom "type" attribute.
function queries.piece_type(piece, query_type)
    if queries.has_value(piece, "type") then
        return piece.type == query_type
    end

    return false
end

-- Checks a piece's position against a destination.
function queries.at_position(piece, destination)
    if not queries.has_value(piece, "position") then
        return false
    end

    local success, result = pcall(function()
        return piece.position[0] == destination[0]
            and piece.position[1] == destination[1]
    end)

    return success and result
end

-- Returns a coordinate offset from a Python tuple/list.
-- The result is a Lua table with 0-based keys to match your Python coordinates.
function queries.offset(destination, dx, dy)
    return {
        [0] = destination[0] + dx,
        [1] = destination[1] + dy
    }
end

-- Manhattan distance between two Python-style coordinates.
function queries.manhattan_distance(a, b)
    return math.abs(a[0] - b[0]) + math.abs(a[1] - b[1])
end

-- Chebyshev distance; useful for king/queen-style grid movement.
function queries.grid_distance(a, b)
    return math.max(
        math.abs(a[0] - b[0]),
        math.abs(a[1] - b[1])
    )
end

-- Checks whether a Lua global exists.
function queries.global_exists(name)
    return _G[name] ~= nil
end

-- Safely retrieves a Lua global.
-- Returns nil when it does not exist.
function queries.get_global(name)
    return _G[name]
end

-- Returns a readable coordinate string for errors/debugging.
function queries.destination_string(destination)
    local success, value = pcall(function()
        return string.format("(%s, %s)", tostring(destination[0]), tostring(destination[1]))
    end)

    if success then
        return value
    end

    return "<bad destination>"
end

return queries
