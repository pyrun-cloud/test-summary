import lithops

def sqrt_map(number):
    return number * number


if __name__ == "__main__":
    iterdata = [2, 4, 6, 8, 10]
    fexec = lithops.FunctionExecutor()
    futures = fexec.map(sqrt_map, iterdata)
    print(fexec.get_result(futures))