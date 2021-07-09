extends TileMap


const TILE_SIZE = 64
var rand_prob = 0.2

export(int) var width 
export(int) var height 

var playing = false
var temp_field


func _ready():
	var width_px = width * TILE_SIZE
	var height_px = height * TILE_SIZE

	var cam = $Camera2D

	cam.position = Vector2(width_px, height_px) / 2
	cam.zoom = Vector2(width_px, height_px) / Vector2(1920, 1080)

	temp_field = []
	for x in range(width):
		var temp_col = []
		for y in range(height):
			set_cell(x,y,0)
			temp_col.append(0)
		temp_field.append(temp_col)


func _input(event):
	if event.is_action_pressed("toggle_play"):
		playing = !playing
	if event.is_action_pressed("click"):
		var pos = (get_local_mouse_position()/TILE_SIZE).floor()
		set_cellv(pos, 1-get_cellv(pos))
	if event.is_action_pressed("randomize"):
		randomize_field(rand_prob)
	if event.is_action_pressed("blackout"):
		randomize_field(0)
	

func _process(_delta):
	update_field()


func randomize_field(prob):
	var rand_field = []
	for _x in range(width):
		var rand_field_col = []
		for _y in range(height):
			if randf() < prob:
				rand_field_col.append(1)
			else:
				rand_field_col.append(0)
		rand_field.append(rand_field_col)
	
	# update tilemap
	for x in range(width):
		for y in range(height):
			set_cell(x, y, rand_field[x][y])



func update_field():
	if !playing:
		return
	
	for x in range(width):
		for y in range(height):
			var live_neighbors = 0
			for x_off in [-1, 0, 1]:
				for y_off in [-1, 0, 1]:
					if x_off != y_off or x_off != 0:
						if get_cell(x+x_off, y+y_off) == 1:
							live_neighbors += 1
			
			if get_cell(x,y) == 1:
				if live_neighbors in [2,3]:
					temp_field[x][y] = 1
				else:
					temp_field[x][y] = 0
			else:
				if live_neighbors == 3:
					temp_field[x][y] = 1
				else:
					temp_field[x][y] = 0


	# update tilemap
	for x in range(width):
		for y in range(height):
			set_cell(x, y, temp_field[x][y])
