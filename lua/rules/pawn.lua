local queries = require("utils.queries")
local validations = require("utils.validations")

--[[
    ordinary pawn movement, after validation of arguments.
    if first move, then pawn can go 2 spaces or just 1
    returns a Lua table of information about the move for handling
--]]
function normal_move(piece, destination)

    local move = {first_move=nil, --internal
                  validation_response=nil, --debug
                  destination=nil, --internal
                  destination_response=nil, --debug
                  legal_move=false --what to look at
                  }
    -- VALIDATING ARGUMENTS AND CHECKING GLOBALS
    local validation_table = {piece_response=validations.validate_piece(piece, "pawn"),
                              destination_response=validations.validate_destination(destination),
                              global_response=validations.validate_globals({board=""})}

    move.validation_response = validations.validation_string(validation_table)
    if move.validation_response ~= "good" then
        return move
    end
    -- VALIDATIONS PASSED


    -- LOGIC CHECKS
    local manhattan_distance = queries.manhattan_distance(piece.position, destination)

    if piece.position[1] > destination[1] then
        move.destination_response = "pawns cannot move backwards"
        return move
    end

    if queries.python_getattr(queries.python_getattr(piece, "position"), "x") ~= destination[0] then
        move.destination_response = "pawn cannot move horizontally in a normal move"
    else
        if not (manhattan_distance >= 1 and manhattan_distance <= 2) then
            move.destination_response = "bad y change in the destination"
            move.legal_move = false
        else
            move.destination_response = "good"
        end
    end

    if move.destination_response ~= "good" then
        return move
    end

    if queries.can_move(piece, board, destination) then
        local moves_made = queries.python_getattr(piece, "moves_made")
        if moves_made == 0 then
            move.first_move = true
            move.legal_move = true
        else
            move.first_move = false
            if (move.manhattan_distance == 1) then
                move.legal_move = true
            end
        end
        move.destination = destination
    end
    return move
end


--[[

--]]
function capture_move(piece_capturing, piece_to_capture)
    local move = {validation_response=nil, --debug
                  destination=nil, --internal
                  destination_response=nil, --debug
                  piece_to_capture=nil,
                  legal_capture=false --what to look at
                  }
    -- VALIDATING ARGUMENTS AND CHECKING GLOBALS
    local globals_req = {board=board,
                         tuple=tuple}

    local validation_table = {piece_capturing_response=validations.validate_piece(piece_capturing, "pawn"),
                              global_response=validations.validate_globals(globals_req),
                              piece_to_capture_response=validations.validate_piece(piece_to_capture)}

    move.validation_response = validations.validation_string(validation_table)
    if move.validation_response ~= "good" then
        return move
    end
    -- VALIDATIONS PASSED
    -- LOGIC CHECKS

    return move

end