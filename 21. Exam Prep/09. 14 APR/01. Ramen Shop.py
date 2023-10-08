from collections import deque

bowls_ramen = [int(el) for el in input().split(", ")]
customer_queue = deque([int(el) for el in input().split(", ")])

while bowls_ramen and customer_queue:
    cur_ramen = bowls_ramen.pop()
    cur_customer = customer_queue.popleft()
    if cur_ramen == cur_customer:
        continue
    elif cur_ramen > cur_customer:
        cur_ramen -= cur_customer
        bowls_ramen.append(cur_ramen)
    elif cur_customer > cur_ramen:
        cur_customer -= cur_ramen
        customer_queue.appendleft(cur_customer)

if customer_queue:
    print("Out of ramen! You didn't manage to serve all customers.")
    customer_queue = [str(el) for el in customer_queue]
    print(f"Customers left: {', '.join(customer_queue)}")
else:
    print("Great job! You served all the customers.")
    if bowls_ramen:
        bowls_ramen = [str(el) for el in bowls_ramen]
        print(f"Bowls of ramen left: {', '.join(bowls_ramen)}")
