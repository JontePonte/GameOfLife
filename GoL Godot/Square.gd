extends Control

onready var ColorRect = get_node("ColorRect")

var size = GlobalVar.rect_size


func _ready():
	rect_scale.x = size
	rect_scale.y = size
	ColorRect = Color(0,100,100)


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
