"""You are given a list of integers that is not sorted, along with a set of queries. Your task is to sort the list and then perform a Binary Search for each query to check whether a specific number exists in the list or not. You must print the search process for each query, showing details of each round of the binary search.
Input:

A single line of input containing two parts separated by a / :

    First part: a list of unsorted integers.

    Second part: a list of integers representing the numbers you want to search for.
    
Hint:

To print each round of the search, use the following code:

print(f"round|\tleft|\tright|\tmiddle|")

print(f"{count:>5}|\t{left:>4}|\t{right:>5}|\t{mid:>6}|")

    f-string: This is a way to embed variables directly into a string. In this case, {count}, {left}, {right}, and {mid} are inserted into the output.

    \t: Inserts a tab space between columns to align the text.

    {count:>5}: Formats the variable count to be right-aligned (>) and occupy a total width of 5 characters.

    {left:>4}, {right:>5}, {mid:>6}: Similarly, these format left, right, and mid to be right-aligned with widths of 4, 5, and 6 characters, respectively, ensuring that the numbers align neatly in columns.


The provided structure is sufficient for completing the task. However, feel free to modify or rewrite it as needed to suit your preferences or to enhance functionality.

You are not allowed to use built-in functions for sorting. You can implement your own sorting algorithm, such as Bubble Sort, Selection Sort, or any other sorting method of your choice, but you must write it yourself.
    
    """


def sort(inp):

   # built-in sort function e.g. inp.sort() not allowed

   for i in range(len(inp) - 1):

       for j in range(len(inp) - 1 - i):

           if inp[j] > inp[j + 1]:

               inp[j], inp[j + 1] = inp[j + 1], inp[j]

   return inp


def binary_search(inp, q):

   print(f"Searching for {q}")

   print(f"round|\tleft|\tright|\tmiddle|")

   count, left, right = 0, 0, len(inp) - 1

   while left <= right:

       count += 1

       mid = (left + right) // 2

       print(f"{count:>5}|\t{left:>4}|\t{right:>5}|\t{mid:>6}|")

       if inp[mid] == q:

           return [mid, count, left, right]

       if inp[mid] < q:

           left = mid + 1

       else:

           right = mid - 1

   return [-1, count,left,right] # base case


inp,q = input("Enter list of numbers: ").split('/')

inp = [int(i) for i in inp.split()]

q = [int(i) for i in q.split()]

inp = sort(inp)

print(f"Sorted list: ",end='')

print(*inp)

for i in range(len(q)):

   res = binary_search(inp, q[i])

   if res[0] == -1:

       print(f"Not found {q[i]} in the list")

   else:

       print(f"Found {q[i]} at index {res[0]}")

       print(f"[round/left/right] : {res[1]} {res[2]} {res[3]}")

   print()