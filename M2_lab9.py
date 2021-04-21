"""
Lab 9.1 - Duyệt cây nhị phân
Giới thiệu bài toán
Trong bài toán này, bạn sẽ triển khai duyệt cây nhị phân theo thứ tự giữa, thứ tự trái và thứ tự phải. 
Các phép duyệt này đã được định nghĩa trong bài giảng ở tuần 1 về duyệt cây, nhưng sẽ rất hữu ích nếu 
bạn thực hành triển khai chúng để hiểu hơn về cây tìm kiếm nhị phân.

Mô tả bài toán
Nhiệm vụ. Bạn có một cây nhị phân có gốc. Xây dựng và xuất ra các phép duyệt cây theo thứ tự giữa,
thứ tự trái và thứ tự phải.

+ Định dạng input. Dòng đầu tiên chứa số đỉnh 𝑛. Các đỉnh của cây được đánh số từ 0 đến 𝑛 − 1. Đỉnh 0 là gốc.
𝑛 dòng tiếp theo chứa thông tin về các đỉnh 0, 1, ..., 𝑛−1 theo thứ tự. Mỗi dòng này chứa ba số nguyên 𝑘𝑒𝑦𝑖,
𝑙𝑒𝑓𝑡𝑖 và 𝑟𝑖𝑔ℎ𝑡𝑖 — 𝑘𝑒𝑦𝑖 là key (khoá) của đỉnh thứ 𝑖, 𝑙𝑒𝑓𝑡𝑖 là index con trái của đỉnh thứ 𝑖 và 𝑟𝑖𝑔ℎ𝑡𝑖 là index 
con phải của đỉnh thứ 𝑖. Nếu 𝑖 không có con trái hoặc phải (hoặc cả hai) thì 𝑙𝑒𝑓𝑡𝑖 hoặc 𝑟𝑖𝑔ℎ𝑡𝑖
(hoặc cả hai) tương ứng sẽ bằng −1.

+ Định dạng output. In ra ba dòng. Dòng đầu chứa các key của các đỉnh theo phép duyệt cây theo thứ tự giữa. 
Dòng thứ hai chứa các key của các đỉnh theo phép duyệt cây theo thứ tự trái. Dòng thứ ba chứa các key của 
các đỉnh theo phép duyệt cây theo thứ tự phải.
"""
class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    # Thêm 1 node mới vào cây nhị phân
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

    # Duyệt cây nhị phân với Inorder traversal 
    # Duyệt các nút trái -> root -> các nút phải
    def Inorder(self, root):
        inorder_lst = []
        if root:
            inorder_lst = self.Inorder(root.left)
            inorder_lst.append(root.data)
            inorder_lst = inorder_lst + self.Inorder(root.right)
        return inorder_lst

    # Duyet cay nhi phan voi Preorder traversal
    # Duyet theo thu tu Root -> trai -> phai
    def Preorder(self, root):
        Preorder_lst = []
        if root:
            Preorder_lst.append(root.data)
            Preorder_lst = Preorder_lst + self.Preorder(root.left)
            Preorder_lst = Preorder_lst + self.Preorder(root.right)
        return Preorder_lst

    # Duyet cay nhi phan voi Postorder traversal
    # Duyet theo thu tu trai -> phai -> Root
    def Postorder(self, root):
        Postorder_lst = []
        if root:
            Postorder_lst = self.Postorder(root.left)
            Postorder_lst = Postorder_lst + self.Postorder(root.right)
            Postorder_lst.append(root.data)
        return Postorder_lst


n = int(input("Nhập vào số node: "))
node = []
left_right = []
key = []

for i in range(n):
    value = input("Nhập vào giá trị: ")
    value = [int(i) for i in value.split()]
    node.append(value[0])
    left_right.append(value[1])
    key.append(value[2])

root_node = Node(node[0])
root_left_right = Node(left_right[0])
root_key = Node(key[0])

for i in range(1, n):
    root_node.insert(node[i])
    root_left_right.insert(left_right[i])
    root_key.insert(key[i])

print(root_node.Inorder(root_node))
print(root_node.Preorder(root_node))
print(root_node.Postorder(root_node))

# Input:
# 5
# 4 1 2
# 2 3 4
# 5 -1 -1
# 1 -1 -1
# 3 -1 -1
# Output:
# 1 2 3 4 5
# 4 2 1 3 5
# 1 3 2 5 4