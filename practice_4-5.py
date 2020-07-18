import time

nums = [i for i in range(1, 1000001)]
print(min(nums))
print(max(nums))
start_time = time.time()
print(sum(nums))
end_time = time.time()
time_taken_in_micro = (end_time - start_time) * (10 * 10)
print("time taken in micro-second:\t{0} ms".format(time_taken_in_micro))
