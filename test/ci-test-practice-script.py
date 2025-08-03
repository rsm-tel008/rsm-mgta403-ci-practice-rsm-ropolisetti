if "local_test" not in locals():
    local_test = False

if not local_test:
    file_name = "code-template.py"
    with open(file_name) as f:
        exec(f.read())

if "x" not in locals():
    raise NameError("Did you name the variable `x`?")
else:
    if x == 3:
        print("x was set to 3. Nice work!")
    else:
        raise Exception("Is the value `x` equal to 3?")

if "y" not in locals():
    raise NameError("Did you name the variable `y`?")
else:
    if y == 7:
        print("y was set to 7. Nice work!")
    else:
        raise Exception("Is the value `y` equal to 7?")

if "z" not in locals():
    raise NameError("Did you name the variable `z`?")
else:
    if z == 10:
        print("z was set to 10 (x + y). Nice work!")
    else:
        raise Exception("Is the value `z` equal to 10 (x + y)?")

print("\n\nMake sure to also fix the other template files!")
