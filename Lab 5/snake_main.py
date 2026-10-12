
import random
from snake_view import draw_board

def app_started(app):

    app.direction = 'east'
    app.info_mode = True

    app.board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0,-1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
    app.snake_size = 3
    app.head_pos = (3, 4)
    app.state = 'active'
    app.timer_delay = 300
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    ...

def timer_fired(app):

    if app.info_mode == False and app.state == 'active':
        move_snake(app)
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    ...

def key_pressed(app, event):
    if (event.key == 'i'):
        if app.info_mode == True:
            app.info_mode = False
        elif app.info_mode == False:
            app.info_mode = True
    if app.state == 'active':
        
     if (event.key == 'Up'):
         app.direction = 'north'
     if (event.key == 'Down'):
         app.direction = 'south'
     if (event.key == 'Left'):
         app.direction = 'west'
     if (event.key == 'Right'):
         app.direction = 'east'

     if (event.key == 'Space'):
         move_snake(app)
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    ...

def redraw_all(app, canvas):
    if app.state == 'active':
        if app.info_mode == True:
            canvas.create_text(app.width/2, 15,
                                text = f'{app.state =} {app.head_pos =} {app.snake_size =} {app.direction=}')
    elif app.state == 'gameover':
        if app.info_mode == True:
            canvas.create_text(app.width/2, 15,
                               text ='gameover')
    draw_board(canvas, 25, 25, app.width -25, app.height - 25, app.board, app.info_mode )
    

    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    ...

def move_snake(app):
    app.head_pos = get_next_head_position(app.head_pos, app.direction)
    row, col = app.head_pos
    if is_legal_move(app.head_pos, app.board) == False:
        app.state = 'gameover'
        return

    
    
    if app.board[row][col] < 0:
         app.snake_size +=1
         add_apple_at_random_location(app.board)
    else:
        subtract_one_from_all_positives(app.board)
    app.board[row][col] = (app.snake_size)
    


def get_next_head_position(head_pos, direction):
    x, y = head_pos
    if direction == 'north':
        x -=1
    if direction == 'south':
        x +=1
    if direction == 'east':
        y +=1
    if direction == 'west':
        y -=1
    head_pos = x, y
    return(head_pos)


def subtract_one_from_all_positives(grid):
    grid == []
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] > 0:
                grid[row][col]= grid[row][col] -1
    return(grid)


def add_apple_at_random_location(grid):
    grid ==[]
    rows = len(grid)
    cols = len(grid[0])
    while True:
        row =random.choice(range(rows))
        col = random.choice(range(cols))
        if grid[row][col] ==0:
            grid[row][col] = grid[row][col]-1
            return(grid)




def is_legal_move(pos, board):
    board ==[]
    pos == ()
    x, y =pos
    rows = len(board) 
    cols = len(board[0]) 
    while x>=0 and x <rows and y>=0 and y <cols:
            if board[x][y] == 0 or board[x][y] == -1:
                return(True)    
            else:
                return(False)
    else:
        return(False)



if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    run_app(width=500, height=400, title='Snake')