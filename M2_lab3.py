"""
Lab 3.1 - Tìm kiếm nhị phân
Giới thiệu bài toán
Trong bài toán này, bạn sẽ triển khai thuật toán tìm kiếm nhị phân cho phép tìm kiếm 
rất hiệu quả các list (thậm chí rất lớn) với điều kiện list đó đã được sắp xếp.
Mô tả bài toán
Nhiệm vụ. Mục tiêu của bài toán này là triển khai thuật toán tìm kiếm nhị phân.

+ Định dạng input. Dòng đầu tiên của input chứa số nguyên n và dãy a0 < a1 < . . . < an−1 gồm 
n số nguyên dương khác nhau từng đôi một theo tứ tự tăng dần. Dòng tiếp theo chứa số nguyên
k và k số nguyên dương b0, b1, . . . , bk−1.


+ Định dạng output. Với mọi i từ 0 đến k − 1, xuất ra một index (chỉ mục) 0 ≤ j ≤ n − 1 sao 
cho aj = bi hoặc −1 nếu không có index nào như vậy.

"""
def binary_search(a, x):
    left, right = 0, len(a)-1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1

data_a = input("Nhap day n va n so a tang dan: ")
data_b = input("Nhap day k va k so can tim: ")
data_a = [int(i) for i in data_a.split()]
data_b = [int(i) for i in data_b.split()]
n = data_a[0]
a = data_a[1:]
b = data_b[1:]
for x in b:
    print(binary_search(a, x), end = ' ')

# test
# 5 1 5 8 12 13
# 5 8 1 23 1 11

"""
Lab 3.2 - “Phần tử đa số”
Giới thiệu bài toán
Một phần tử của dãy có độ dài n được gọi là “phần tử đa số” nếu nó xuất hiện trong dãy nhiều hơn n/2 lần.
Mô tả bài toán
Nhiệm vụ. Mục tiêu của bài toán này là kiểm tra xem một dãy input có chứa “phần tử đa số” hay không.

+ Định dạng input. Dòng đầu tiên chứa số nguyên n, dòng tiếp theo chứa dãy n số nguyên không âm a0, a1, . . . , an−1.

+ Định dạng output. Xuất ra 1 nếu dãy chứa “phần tử đa số” và 0 nếu ngược lại.
"""
def getMajorityElement(a):
    candidate = -1
    count = 0
    for t in a:
        if count == 0:
            candidate, count = t, 1
            continue
        if t == candidate: count += 1
        else: count -= 1
    recount = 0
    for x in a:
        if x == candidate:
            recount += 1
    if recount > len(a) // 2 :
        return candidate
    return -1


n = int(input("Nhap vao so n: "))
a = input("nhap vao day so a: ")
a = [int(i) for i in a.split()]
if n == len(a):
    if getMajorityElement(a) != -1:
        print(1)
    else:
        print(0)
# test
# 5
# 2 3 9 2 2

