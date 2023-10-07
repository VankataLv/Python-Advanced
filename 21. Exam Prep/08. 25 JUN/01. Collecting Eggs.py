from collections import deque

egg_sizes = deque([int(el) for el in input().split(", ")])
paper_sizes = deque([int(el) for el in input().split(", ")])
filled_boxes = 0

while egg_sizes and paper_sizes:
    cur_egg_size = egg_sizes.popleft()
    if cur_egg_size <= 0:
        continue
    else:
        if cur_egg_size == 13:
            last_paper = paper_sizes.pop()
            first_paper = paper_sizes.popleft()
            paper_sizes.append(first_paper)
            paper_sizes.appendleft(last_paper)
            continue
        else:
            cur_paper_size = paper_sizes.pop()
            if cur_paper_size + cur_egg_size <= 50:
                filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_sizes:
    egg_sizes = [str(el) for el in egg_sizes]
    print(f"Eggs left: {', '.join(egg_sizes)}")

if paper_sizes:
    paper_sizes = [str(el) for el in paper_sizes]
    print(f"Pieces of paper left: {', '.join(paper_sizes)}")
