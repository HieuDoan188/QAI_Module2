"""
Lab 2.1 - Đổi tiền
Lab 2.1 Giới thiệu bài toán
Trong bài toán này, bạn sẽ thiết kế và triển khai một thuật toán “tham lam” sơ cấp
 được các nhân viên thu ngân trên toàn thế giới sử dụng hàng triệu lần mỗi ngày.
Mô tả bài toán
Nhiệm vụ. Mục tiêu của bài toán này là tìm ra số lượng đồng xu tối thiểu cần thiết 
để đổi giá trị input (một số nguyên) thành tiền xu với mệnh giá 1, 5 và 10.

Định dạng input. Input gồm duy nhất một số nguyên 𝑚.
Ràng buộc. 1 ≤ 𝑚 ≤ 10^3.

Định dạng output. Xuất ra số lượng đồng xu tối thiểu với mệnh giá 1, 5, 10 khiến m thay đổi.
Mẫu 1.
Input:
2
Output:
2
Giải thích:
2 = 1 + 1.
"""

def coin_change_greedy(n):
    coins = [10, 5, 1]
    i = 0
    result = []
    while(n>0):
        if(coins[i] > n):
            i = i+1
        else:
            result.append(coins[i])
            n = n-coins[i]
    return len(result)

n = int("Nhập vào giá trị cần đổi: ")
print(coin_change_greedy(n))


"""
Lab 2.2 - Tối đa giá trị của chiến lợi phẩm
Giới thiệu bài toán
Một tên trộm tìm được nhiều vật phẩm hơn sức chứa của cái túi. Hãy giúp hắn ta tìm ra cách kết
hợp các vật phẩm có giá trị nhất giả sử bất kỳ phần nào của một chiến lợi phẩm cũng đều có thể cho vào túi.

Mô tả bài toán
Nhiệm vụ. Mục tiêu của bài toán này là triển khai một thuật toán cho bài toán cái túi dạng phân số.
+ Định dạng input. Dòng đầu tiên của input chứa n số vật phẩm và sức chứa W của cái túi.
Các dòng n tiếp theo biểu thị giá trị và trọng lượng của các vật phẩm. Dòng thứ i chứa các số nguyên
vi và wi —tương ứng với giá trị và trọng lượng của vật phẩm thứ i.

+ Định dạng output. Xuất ra giá trị phân số tối đa của các vật phẩm có thể cho vừa vào cái túi. 
Giá trị tuyệt đối của hiệu giữa kết quả từ chương trình của bạn và giá trị tối ưu lớn nhất là 
10^−3. Để đảm bảo điều này, xuất ra kết quả với ít nhất 4 chữ số sau dấu thập phân (nếu không,
kết quả của bạn, dù được tính toán chính xác, vẫn có thể bị sai do làm tròn).
"""
def fractional_knapsack(value, weight, capacity):
    index = list(range(len(value)))
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)        # xếp lại chỉ số index theo thứ tự của của tỷ trọng giá trị và cân nặng
    max_value = 0
    for i in index:
        if weight[i] <= capacity:
            max_value += value[i]
            capacity -= weight[i]
        else:
            max_value += value[i]*capacity/weight[i]
            break
    return max_value
 
data1 = input("Nhập vào số vật phẩm và sức chứa của túi: ") 
n, capacity = int(data1.split()[0]), int(data1.split()[1])
value = []
weight = []
for i in range(n):
    data2 = input("Nhập vào giá trị và trọng lượng của vật phẩm: ")
    data2 = data2.split()
    value.append(data2[0])
    weight.append(data2[1])
value = [int(i) for i in value]
weight = [int(i) for i in weight]
max_value = fractional_knapsack(value, weight, capacity)
print('Giá trị tối đa túi chứa được là: ', max_value)

# 3 50
# 60 20
# 100 50
# 120 30


"""
Lab 2.3 Tối đa doanh thu từ vị trí đặt quảng cáo trực tuyến

Giới thiệu bài toán
Bạn có n quảng cáo cần bố trí trên một trang mạng nổi tiếng. Với từng quảng cáo,
bạn biết người quảng cáo sẽ sẵn sàng chi trả bao nhiêu tiền cho một cú nhấp chuột 
vào quảng cáo. Bạn đã thiết lập n vị trí trên trang mạng và ước tính số lượng cú
nhấp chuột mỗi ngày vào từng quảng cáo ở mỗi vị trí. Mục tiêu của bạn là phân bổ
các quảng cáo ở các vị trí khác nhau để tối đa doanh thu.

Mô tả bài toán
Nhiệm vụ. Cho hai dãy 𝑎1, 𝑎2, . . . , 𝑎𝑛 (ai là lợi nhuận trên một cú nhấp chuột vào quảng
cáo thứ i) và b1, b2, ..., bn (bi  là số lượng cú nhấp chuột trung bình một ngày vào vị 
trí thứ i), chúng ta cần chia chúng thành n cặp (ai, bj) sao cho tổng của các sản phẩm là tối đa.

+ Định dạng input. Dòng đầu tiên chứa một số nguyên n, dòng thứ hai chứa 1 dãy các số nguyên
a1, a2, …, an, dòng thứ ba chứa một dãy các số nguyên 𝑏1, 𝑏2, . . . , 𝑏𝑛.

+ Định dạng Output. Xuất ra giá trị tối đa của tổng aici khi i chạy từ 1 đến n và c1, c2, … cn 
là một hoán vị của 𝑏1, 𝑏2, . . . , 𝑏𝑛.
"""

#Uses python3
def max_dot_product(a, b):
    res = 0
    a = sorted(a)
    b = sorted(b)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

n = int(input("Nhập vào số nguyen n: "))
a = input("Nhập vào số nguyen n: ")
a = a.split()
a = [int(i) for i in a]
b = input("Nhập vào số nguyen n: ")
b = b.split()
b = [int(i) for i in b]

print(max_dot_product(a, b))

# Input:
# 1
# 23
# 39
# Output:
# 897

"""
Lab 2.4 - Thu thập chữ ký
Giới thiệu bài toán
Bạn có trách nhiệm thu thập chữ ký của tất cả những người thuê nhà trong một tòa nhà nào đó.
Với mỗi người thuê nhà, bạn biết thời gian họ có mặt ở nhà. Bạn muốn thu thập toàn bộ chữ ký
sao cho bạn chỉ cần đến tòa nhà ít lần nhất có thể. Mô hình toán học cho bài toán này như
sau: Cho một tập hợp các đoạn trên một đường và mục tiêu của bạn là đánh dấu ít điểm nhất 
có thể trên một đường sao cho mỗi đoạn chứa ít nhất một điểm.


Mô tả bài toán
Nhiệm vụ. Cho một tập hợp n đoạn {[𝑎0, 𝑏0], [𝑎1, 𝑏1], . . . , [𝑎𝑛−1, 𝑏𝑛−1]} với các tọa độ số 
nguyên trên một đường, hãy tìm số điểm m tối thiểu sao cho mỗi đoạn chứa ít nhất 1 điểm. Hay,
tìm tập hợp các số nguyên 𝑋 nhỏ nhất sao cho trên mỗi đoạn [𝑎𝑖, 𝑏𝑖] có một điểm 𝑥 ∈ 𝑋 thỏa mãn 𝑎𝑖 ≤ 𝑥 ≤ 𝑏𝑖.

+ Định dạng input. Dòng đầu tiên của input chứa số đoạn n. Mỗi dòng trong n dòng tiếp theo chứa 2
số nguyên ai và bi (được ngăn bởi dấu cách) biểu thị tọa độ hai điểm đầu cuối của đoạn thứ i.


+ Định dạng output.  Xuất ra số điểm m tối thiểu trên dòng đầu tiên và tọa độ của m điểm (được 
ngăn bởi dấu cách) trên dòng thứ hai. Bạn có thể xuất ra các điểm theo thứ tự bất kỳ. Nếu có nhiều
tập hợp điểm như vậy, bạn có thể xuất ra một tập hợp bất kỳ. (Không khó để nhận ra rằng luôn luôn
tồn tại những tập hợp điểm nhỏ nhất sao cho tất cả các tọa độ của các điểm đều là số nguyên.)
"""

def optimal_points(segments):
    points = []
    sortedsegs = sorted(segments, key = lambda t: t[1])
    point = sortedsegs[0]
    points.append(point)
    for s in sortedsegs:
        if s > point:
            points.append(s)
            point = s
    return points

n = input("Nhap sao so n: ")
Segment = []
for i in range(int(n)): 
    data = input("Nhap vao day so: ")
    data = data.split()
    Segment.append(data)

points = optimal_points(Segment)
print(len(points))
for p in points:
    print(p, end=' ')

# Input:
# 3
# 1 3
# 2 5
# 3 6
# Output:
# 1
# 3

"""
2.5 Giải thướng đối đa của 1 cuộc thi
Giới thiệu bài toán
Bạn sắp tổ chức một cuộc thi thú vị cho trẻ em. Quỹ giải thưởng bạn có là n chiếc kẹo. Bạn muốn dùng những 
chiếc kẹo này để trao cho 𝑘 vị trí dẫn đầu trong cuộc thi với điều kiện là vị trí cao hơn sẽ nhận được 
nhiều kẹo hơn. Để khiến nhiều đứa trẻ vui vẻ nhất có thể, bạn sẽ phải tìm ra giá trị k lớn nhất.

Mô tả bài toán
Nhiệm vụ. Mục tiêu của bài toán này là biểu diễn một số nguyên dương n dưới dạng tổng của nhiều số 
nguyên dương khác nhau từng đôi một nhất có thể. Hay, tìm số k lớn nhất sao cho n có thể viết thành 
𝑎1 + 𝑎2 + · · · + 𝑎𝑘 trong đó 𝑎1, . . . , 𝑎𝑘 là các số nguyên dương và 𝑎𝑖 ̸= 𝑎𝑗 với mọi 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.

+ Định dạng input. Input chứa duy nhất một số nguyên n.

Ràng buộc. 1 ≤ 𝑛 ≤ 10^9

+ Định dạng output. Ở dòng đầu tiên, xuất ra giá trị k lớn nhất sao cho n có thể biểu diễn dưới 
dạng tổng của k số nguyên dương khác nhau từng đôi một. Ở dòng thứ hai, xuất ra k số nguyên dương 
khác nhau từng đôi một có tổng là n (nếu có nhiều trường hợp như vậy, hãy xuất ra bất kỳ giá trị nào).
"""
def summands(n):
    summands = []
    sumall = 1
    start = 1
    summands.append(start)
    while n - sumall > summands[-1]:
        summands.append(summands[-1] + 1)
        sumall += summands[-1]
    summands[-1] += (n - sumall)
    return summands

n = int(input("Nhap vao so n: "))
summands = summands(n)
print(len(summands))
for x in summands:
    print(x, end=' ')

# Mẫu 1.
# Input:
# 6
# Output:
# 3
# 1 2 3
