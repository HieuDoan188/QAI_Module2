"""
Lab 4.1 - Máy tính nguyên thủy
Giới thiệu bài toán
Bạn được cung cấp một máy tính nguyên thủy có thể thực hiện ba phép tính sau với số x 
hiện tại: nhân x với 2, nhân x với 3 hoặc cộng 1 vào x. Cho một số nguyên dương n, 
mục tiêu của bạn là tìm số phép toán tối thiểu cần thiết để có được số n, bắt đầu từ số 1.
Mô tả bài toán
Nhiệm vụ. Cho một số nguyên dương n, tính số phép toán tối thiểu để có được số n bắt đầu từ số 1.

+ Định dạng input. Input chứa duy nhất một số nguyên thỏa mãn 1 ≤ n ≤ 10^6.

+ Định dạng output. Ở dòng đầu tiên, xuất ra số phép tính tối thiểu cần thiết k để thu được 
giá trị n từ 1. Ở dòng thứ hai, xuất ra một dãy các số trung gian. Hay, dòng thứ hai chứa 
các số nguyên dương a0, a1, . . . , ak−1 sao cho 0 = 1, ak−1= n và với mọi 0 ≤ i < k − 1, ai+1 bằng ai + 1,
2ai hoặc 3ai. Nếu tồn tại nhiều dãy như vậy, xuất ra một dãy bất kỳ.
"""
def findmin(a, b, c):
    if a == -1:
        return findmin(c + 1, b, c)
    if b == -1:
        return findmin(a, c + 1, c)
    return min(a, b, c)

def DPoptimal(n):
    optimalnum =n * [0]
    for i in range(2, n+1):
        n1, n2, n3 = -1, -1, -1
        if i % 3 == 0:
            n3 = optimalnum[i // 3 - 1]
        if i % 2 == 0:
            n2 = optimalnum[i // 2 - 1]
        n1 = optimalnum[i - 1 - 1]
        optimalnum[i - 1] = findmin(n3, n2, n1) + 1
    return optimalnum

def optimal_sequence(n):
    sequence = []
    optimalnum = DPoptimal(n)
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0 and optimalnum[n-1] == optimalnum[n // 3 -1] + 1:
            n = n // 3
        elif n % 2 == 0 and optimalnum[n-1] == optimalnum[n // 2 -1] + 1:
            n = n // 2
        else:
            n -= 1
    return reversed(sequence)

n = int(input("Nhap vao so n: "))
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

# Input:
# 5
# Output:
# 3
# 1 2 4 5

"""
Lab 4.2 - Lấy nhiều vàng nhất có thể
Giới thiệu bài toán
Bài toán này là về việc triển khai một thuật toán cho bài toán cái túi không lặp lại.

Mô tả bài toán
Nhiệm vụ. Trong bài toán này, bạn có một chồng các thỏi vàng và mục tiêu của bạn là cho 
càng nhiều vàng vào túi càng tốt. Mỗi thỏi chỉ có một bản sao và bạn chỉ có thể chọn
lấy hoặc không (do đó bạn không thể lấy một phần của một thỏi vàng).

+ Định dạng input. Dòng đầu tiên bao gồm sức chứa W của cái túi và số lượng n thỏi vàng.
Dòng tiếp theo chứa n số nguyên w0, w1, . . . , wn−1 biểu thị trọng lượng của các thỏi vàng.

+ Định dạng output. Xuất ra trọng lượng tối đa của các thỏi vàng có thể cho vừa vào túi với sức chứa W.
"""

def optimal_weight(W, w):
    n = len(w)
    value = [[0 for col in range(W + 1)] for row in range(n + 1)]
    for i in range(1, n + 1):
        for cp in range(1, W + 1):
            value[i][cp] = value[i-1][cp]
            if w[i-1] <= cp:
                val = value[i-1][cp - w[i-1]] + w[i - 1]
                if val > value[i][cp]:
                    value[i][cp] = val
    return value[-1][-1]

data1 = input("Nhap lan luot suc chua va so luong thoi vang: ")
data1 = [int(i) for i in data1.split()]
W = data1[0]
n = data1[1]
data2 = input("Nhap vao trong luong cac thoi vang:  ")
data2 = [int(i) for i in data2.split()]
if n == len(data2):
    print(optimal_weight(W, data2))

# Input:
# 10 3
# 1 4 8
# Output:
# 9