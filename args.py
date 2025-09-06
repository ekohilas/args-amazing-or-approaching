def foo(*args: tuple[int, str, int, ...]):
    print(args)

foo(1)
foo(1, "a")
foo(1, "a", 2)
foo(1, "a", 2, 3)

foo("a")
foo("a", "b")
foo("a", "b", "c")
foo(1, 2)
foo(1, 2, "a")
foo(1, "a", 2, "b")
