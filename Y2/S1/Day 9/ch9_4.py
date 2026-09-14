def insertionSort(l):
    l = l[:]
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l

def median(l):
    l = insertionSort(l)
    n = len(l)
    if n % 2:
        return float(l[n // 2])
    return (l[n // 2 - 1] + l[n // 2]) / 2

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "Insertion Sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    data = []
    for e in l:
        data.append(e)
        print(f"list = {data} : median = {median(data)}")
