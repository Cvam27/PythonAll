# add_num = input("Enter a number")
# series_num = int(input("Enter for series"))
# for i in range(series_num):
#     total = add_num*i
#     add_num = total
#     print(total)

n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq = start + sum_seq
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)



