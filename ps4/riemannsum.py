from math import cos, pi, log

def riemann_sum(func, step_type, range_start, range_end, step_size):
    delta = (range_end - range_start)/step_size
    int_pointer = 0
    running_sum = 0
    if step_type == "l":
        int_pointer = range_start
        for i in range(step_size):
            running_sum += func(int_pointer) * delta
            int_pointer += delta
    elif step_type == "r":
        int_pointer = range_start + delta
        for i in range(step_size):
            running_sum += func(int_pointer) * delta
            int_pointer += delta
    elif step_type == "m":
        int_pointer = range_start + delta / 2
        for i in range(step_size):
            running_sum += func(int_pointer) * delta
            int_pointer += delta
    else:
        raise Exception("step_type is invalid.")
    return running_sum

if __name__ == "__main__":
    for i in [10,30, 50]:
        for j in ["l","m","r"]:
            print(f"The {j} Riemann Sum with step size {i} is {riemann_sum(lambda x: log(x),j,1,4,i)}")