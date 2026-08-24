local validations = {}
local queries = require("utils.queries")

--checks if the globals inside of the table 'args' are active
function validations.validate_globals(args)
    for key, value in pairs(args) do
        if not queries.global_exists(tostring(key)) then
            return tostring(key).." was not established as a global variable and it is required."
        end
    end

    return "good"
end

--[[checks if the piece is of type queried (matches type of piece_type if specified) or is a valid type (if not specified)
--    checks if the piece is an instance of the Piece class--]]
function validations.validate_piece(piece, piece_type)
    if queries.python_getattr(piece, "class_name") ~= "Piece" then
        return tostring(piece).." is not an instance of Piece"
    end
    local valid_pieces = {pawn=true,
                          rook=true,
                          bishop=true,
                          knight=true,
                          king=true,
                          queen=true}

    if piece_type ~= nil then
        if valid_pieces[piece_type] == nil then
            return tostring(piece_type).." is not a recognized type of piece"
        end

        if not queries.piece_type(piece, piece_type) then
            return "piece was not a "..tostring(piece_type)
        end
    else
        if valid_pieces[piece.type] == nil then
            return tostring(piece.type).." is not a recognized type of piece"
        end
    end

    return "good"
end


--[[checks if destination fits within the board's dimensions
--    checks if the global variable board exists--]]
function validations.validate_destination(destination)
    local _, destination_length = queries.len(destination)
    if destination_length > 2 then
        return "too many dimensions specified in "..tostring(destination).." only 2 allowed"
    end

    if not queries.global_exists("board") then
        return "validations.validate_destination(destination) requires global variable board to be used"
    end

    local status, value = queries.board_lookup(board, destination)
    if not status then
        local length = queries.python_getattr(board, "length")
        local width = queries.python_getattr(board, "width")
        return tostring(destination) .. " is bad destination\nboard is: " .. tostring(width).."," .. tostring(length)
    end

    return "good"
end

--[[
    checks for validations of piece, piece_type, destination, args for global variables
--]]
function validations.validate_arguments(piece, destination, piece_type, args)
    local global_response = validations.validate_globals(args) -- only the key is used
    if global_response ~= "good" then
        return global_response
    end

    local piece_response = validations.validate_piece(piece, piece_type)
    if piece_response ~= "good" then
        return piece_response
    end

    local destination_response = validations.validate_destination(destination)
    if destination_response ~= "good" then
        return destination_response
    end

    return "good"
end


function validations.validation_string(validation_table)
    for key, value in pairs(validation_table) do
        if value ~= "good" then
            return value
        end
    end
    return "good"
end

return validations