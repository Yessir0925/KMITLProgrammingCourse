print(" *** File Error Handling ***")
filename, word = input("Enter file name and word : ").split()

count_lines = 0
sum_line_nums = 0
total_lines = 0

try:
    f = open(filename, 'r', encoding="utf-8")
    for idx, line in enumerate(f, start=1):
        total_lines += 1
        if word in line:          
            count_lines += 1
            sum_line_nums += idx
    f.close()

    print(f'Number of lines having "{word}" => {count_lines}')
    print(f"Sum of line number => {sum_line_nums:,}")
    print(f"Total lines => {total_lines:,}")

except FileNotFoundError:
    print(f'Error can not open file => {filename}')

print("===== End of program =====")