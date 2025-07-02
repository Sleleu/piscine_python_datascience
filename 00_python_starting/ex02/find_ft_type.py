def all_thing_is_obj(object: any) -> int:
	if isinstance(object, str):
		print(f"{object} is in the kitchen : {object.__class__}")
	elif isinstance(object, dict) or isinstance(object, list) or isinstance(object, tuple) or isinstance(object, set):
		print(f"{object.__class__.__name__.capitalize()} : {object.__class__}")
	else:
		print("Type not found")
	return 42