def comparison(pos, neg):
    if pos > abs(neg):
        return f"The positives are stronger than the negatives"
    else:
        return f"The negatives are stronger than the positives"


nums = [int(x) for x in input().split()]
pos_nums = [x for x in nums if x > 0]
neg_nums = [x for x in nums if x < 0]

pos_sum = sum(pos_nums)
neg_sum = sum(neg_nums)
print(neg_sum)
print(pos_sum)
print(comparison(pos_sum, neg_sum))
