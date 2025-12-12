def generate_spiral(*args):
    if len(args) == 0:
        return []
    h = int(args[0])
    direction = "right"
    word = None
    if len(args) == 2:
        if args[1].lower() in ("left", "right", "up", "down"):
            direction = args[1].lower()
        else:
            word = args[1]
    elif len(args) >= 3:
        direction = args[1].lower()
        word = args[2]

    n = h
    mat = [[None for _ in range(n)] for _ in range(n)]
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    d = {"right":0,"down":1,"left":2,"up":3}[direction]

    if n % 2 == 1:
        cx = n//2
        cy = n//2
    else:
        if direction == "right":
            cx = n//2 - 1; cy = n//2 - 1
        elif direction == "down":
            cx = n//2 - 1; cy = n//2
        elif direction == "left":
            cx = n//2;     cy = n//2
        else:
            cx = n//2;     cy = n//2 - 1

    if word is None:
        seq = list(range(1, n*n + 1))
    else:
        base = word
        def shift_word(w, k):
            out = []
            for ch in w:
                oc = ord(ch)
                if 65 <= oc <= 90:
                    out.append(chr(65 + ((oc - 65 + k) % 26)))
                elif 97 <= oc <= 122:
                    out.append(chr(97 + ((oc - 97 + k) % 26)))
                else:
                    out.append(ch)
            return "".join(out)
        seq = []
        k = 0
        while len(seq) < n*n:
            block = shift_word(base, k)
            r = 0
            while r < k+1 and len(seq) < n*n:
                for ch in block:
                    seq.append(ch)
                    if len(seq) == n*n:
                        break
                r += 1
            k += 1

    mat[cx][cy] = seq[0]
    if n*n == 1:
        return mat

    idx = 1
    step_len = 1
    while idx < n*n:
        for _ in range(2):
            dx, dy = dirs[d % 4]
            s = 0
            while s < step_len and idx < n*n:
                cx += dx
                cy += dy
                mat[cx][cy] = seq[idx]
                idx += 1
                s += 1
            d += 1
        step_len += 1

    return mat


def print_spiral(matrix):
    if not matrix or not matrix[0]:
        return
    w = 1
    for row in matrix:
        for v in row:
            lw = len(str(v))
            if lw > w:
                w = lw
    for row in matrix:
        line = ""
        for v in row:
            line += str(v).rjust(w) + "  "
        print(line)


print(" *** Center-starting Spiral Rectangle XXX ***")
inp = input("Enter side [direction] [word] : ")

args = inp.split()
spiral_rectangle = generate_spiral(*args)
print_spiral(spiral_rectangle)

print("===== End of program ======")