import timeit

def TimeThis(code_to_run, run_count):
    return timeit.timeit(stmt = code_to_run, number = run_count)