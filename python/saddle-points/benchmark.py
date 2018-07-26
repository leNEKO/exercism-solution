from timeit import timeit


matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]

for f in ("saddle_points", "saddle_points_alexhans"):
    setup = f"from {f} import saddle_points"
    cmd = f"saddle_points({matrix})"
    r = timeit(cmd, setup, number=10000)
    print(cmd, setup, r)
