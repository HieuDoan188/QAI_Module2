"""
Lab 8.1 - Tính chiều cao của cây
Giới thiệu bài toán
Cây được sử dụng để thao tác với dữ liệu phân cấp chẳng hạn như hệ thống phân cấp các danh mục 
của một nhà bán lẻ hoặc cấu trúc thư mục trên máy tính của bạn. Chúng cũng được sử dụng trong
phân tích dữ liệu và học máy cho cả phân cụm thứ bậc và xây dựng các mô hình dự đoán phức tạp,
bao gồm một số thuật toán hoạt động tốt nhất trong thực tế như Gradient Boosting trên Decision 
Trees (cây quyết định) và Random Forests (Rừng ngẫu nhiên). Trong các học phần sau của khóa học này,
chúng tôi sẽ giới thiệu Cây tìm kiếm nhị phân cân bằng (BST) - một loại cây đặc biệt cho phép lưu trữ,
thao tác và truy xuất dữ liệu rất hiệu quả. Do đó, các BST cân bằng được sử dụng trong cơ sở dữ liệu 
để lưu trữ hiệu quả và trong hầu hết các chương trình không tầm thường nữa, thường là thông qua cấu
trúc dữ liệu tích hợp sẵn của ngôn ngữ lập trình.

Trong bài toán này, mục tiêu của bạn là làm quen với cây. Bạn sẽ cần đọc mô tả cây từ input, triển 
khai cấu trúc dữ liệu cây, lưu trữ cây và tính chiều cao của nó.

Mô tả bài toán
Nhiệm vụ. Bạn được cung cấp mô tả về một cây có gốc. Nhiệm vụ của bạn là tính và xuất ra chiều cao của nó.
Nhớ rằng chiều cao của cây (có gốc) là độ sâu tối đa của một node (nút), hoặc khoảng cách tối đa từ lá đến 
gốc. Bạn được cung cấp một cây bất kỳ, không nhất thiết phải là một cây nhị phân.

+ Định dạng input. Dòng đầu tiên chứa số đỉnh 𝑛. Dòng thứ hai chứa 𝑛 số nguyên từ −1 đến 𝑛 − 1 - parent (cha) 
của các đỉnh. Nếu đỉnh thứ i trong số chúng (0 ≤ 𝑖 ≤ 𝑛 - 1) là −1, thì đỉnh 𝑖 là gốc, nếu không thì nó
là index bắt đầu từ 0 của parent của đỉnh thứ 𝑖. Đảm bảo rằng chỉ có một gốc. Đảm bảo rằng input biểu diễn một cây.

+ Định dạng output. Xuất ra chiều cao của cây.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):                 
        if self.data:
            if int(data) < int(self.data):        # so sánh ID của các node thêm mới với các node cha để sắp xếp vào cây
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif int(data) > int(self.data):
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def maxDepth(node):
    if node is None:
        return 0
 
    else :
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

n = int(input("Nhap vao so nguyen n: "))
data = input("Nhap vao cac ptu cua cay: ")
data = [int(i) for i in data.split()]
if n == len(data):
    root = Node(data[0])
    for i in range(1, len(data)):
        root.insert(data[i])
print ("Chieu cao cua cay la %d" %(maxDepth(root)))

# test
# Input:
# 5
# 4 -1 4 1 1
# Output:
# 3