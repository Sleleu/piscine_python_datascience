def NULL_not_found(object: any) -> int:
	if object is None:
		print(f"Nothing: {object} {object.__class__}")
	elif isinstance(object, float) and object != object:
		print(f"Cheese: {object} {object.__class__}")
	elif isinstance(object, int) and object == 0:
		print(f"Zero: {object} {object.__class__}")
	elif isinstance(object, str) and object == '':
		print(f"Empty: {object} {object.__class__}")
	elif isinstance(object, bool) and object == False:
		print(f"Fake: {object} {object.__class__}")
	else:
		print("Type not found")
		return 1
	return 0