local queries = require("utils.queries")

function validate_arguments(piece, destination)
    if not queries.global_exists("board") then
        return "board was not established as a lua global.\nDo lua.globals().board = board"
    end

    status, value = queries.board_lookup(board, destination)
    if not status then
        local length = queries.python_getattr(board, "length")
        local width = queries.python_getattr(board, "width")
        return tostring(destination) .. " is bad destination\nboard is: " .. tostring(width).."," .. tostring(length)
    end

    if not queries.piece_type(piece, "pawn") then
        return "piece was not a pawn"
    end

    if piece.class_name ~= "Piece" then
        return "piece was not an instance of Piece"
    end

    return "good"
end

function normal_move(piece, destination)

    local move = {first_move=nil, --internal
                  validation_response=nil, --debug
                  destination=nil, --internal
                  destination_response=nil, --debug
                  legal_move=false --what to look at
                  }
    local validation_response = validate_arguments(piece, destination)
    move.validation_response = validation_response
    if validation_response ~= "good" then
        return move
    end

    local manhattan_distance = queries.manhattan_distance(piece.position, destination)

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

function capture_move(piece, destination)
    return nil
end