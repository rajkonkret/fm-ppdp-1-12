def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2)
allparams(1, 2, 3)
allparams(1, 2, 3, d=8)
allparams(1, 2, c=8, d=9)
# TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / argumenty po lewej stronie musza byc podane po pozycji
# allparams(a=4, b=3, c=8, d=8)
allparams(1, 2, c=8, d=9, a=9)  # kwargs {'a': 9}
allparams(1, 2, 8, 7, 8, 9, 5, 3, 1, d=9, a=9)  # args (7, 8, 9, 5, 3, 1)

