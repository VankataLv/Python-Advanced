file = open("numbers.txt", "r")
nums = file.read().split("\n")
nums = [int(x) for x in nums]
print(sum(nums))
file.close()
