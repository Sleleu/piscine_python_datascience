import sys

try:
	if len(sys.argv) == 1:
		exit(0)
	try: value = int(sys.argv[1])
	except: value = None
	assert isinstance(value, int), "argument is not an integer"
	assert len(sys.argv) == 2, "more than one argument is provided"
	print("I'm Even.") if value % 2 == 0 else print("I'm Odd.")
except AssertionError as error:
	print(f"{error.__class__.__name__}: {error}")