class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):                 
        if self.data:
            if int(data.split()[0]) < int(self.data.split()[0]):        # so sánh ID của các node thêm mới với các node cha để sắp xếp vào cây
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif int(data.split()[0]) > int(self.data.split()[0]):
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def Breadth_first_search(self, root):
        visited = []                      # Tạo list hàng đợi để lưu trữ ptu
        
        if root :                          # root != None => thêm root vào đầu hàng đợi
            visited.append(root)            # Đầu tiên duyệt node gốc (mức 0) và in ra dữ liệu của node
            print(root.data)                      # in ptu dau tien
        current = root                      # gán ptu tạm bằng ptu gốc
        while current:                      # trong khi ptu tam != None
            if current.left:                    # Xét trái và phải of ptu để thêm vào lst
                print(current.left.data)
                visited.append(current.left.data)
            if current.right:
                print(current.right.data)
                visited.append(current.right.data)
            visited.pop(0)                          # Xóa node ở leve thấp
            if not visited:
                break
            current = visited[0]

f = open("DATA3.TXT", "r")
lst = f.readlines()
value = lst[1:]                      
tree = Node(value[0])                  
for i in range(1, len(value)):
    tree.insert(value[i])
tree.Breadth_first_search(tree)
