"""
Lab 5.1 - Sắp xếp 3-phân đoạn
Giới thiệu bài toán
Mục tiêu trong bài toán này là thiết kế lại một triển khai đã cho của 
thuật toán Quick Sort (sắp xếp nhanh) ngẫu nhiên để nó thao tác nhanh 
ngay cả trên các chuỗi chứa nhiều phần tử bằng nhau.

Mô tả bài toán
Nhiệm vụ. Để buộc triển khai đã cho của thuật toán Quick Sort xử lý hiệu quả
các chuỗi có ít phần tử duy nhất, mục tiêu của bạn là thay thế sắp xếp 2-phân
đoạn bằng sắp xếp 3-phân đoạn. Tức là, thủ tục sắp xếp mới của bạn sẽ sắp xếp
mảng thành ba phần: phần < x, phần = x và phần > x.

+ Định dạng input. Dòng đầu tiên của input chứa số nguyên n. Dòng tiếp theo chứa một dãy n số nguyên a0, a1, . . . , an−1.

+ Định dạng output. Xuất ra chuỗi này sắp xếp theo thứ tự không giảm dần.
"""

def partition3(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    lj = j
    while x == a[lj] and lj > -1:
        lj -= 1
    return lj + 1, j

n = int(input("Nhap vao so n: "))
a = input("Nhap vao day a can sap xep: ")
a = [int(i) for i in a.split()]
if len(a) == n:
    partition3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

# test
# Input:
# 5
# 2 3 9 2 2
# Output:
# 2 2 2 3 9