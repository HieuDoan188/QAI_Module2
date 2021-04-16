"""
DOAN MINH HIEU - FX10001
Mỗi hồ sơ cần những thông tin sau: Mã nhân viên, tên nhân viên, ngày sinh, nơi sinh,
trong đó các nhân viên sẽ được phân biệt nhau bởi mã nhân viên. Yêu cầu sử dụng cấu trúc
dữ liệu cây nhị phân tìm kiếm (Binary Search Tree - BST) để lưu trữ và quản lý dữ liệu.

Hãy viết chương trình gồm các chức năng sau:
1. Đưa dữ liệu từ 1 text file vào 1 BTS.
2. Thêm hồ sơ nhân viên mới vào cây BST
3. Duyệt cây BST theo thứ tự giữa (Inorder)
4. Duyệt cây BST theo chiều rộng
5. Tìm kiếm thông tin của nhân viên theo mã nhân viên trong cây BST
6. Xóa đi một hồ sơ nhân viên dựa vào mã nhân viên trong cây BST

# link tham khảo cây: https://codelearn.io/sharing/5-phut-thong-thao-binary-search-tree
"""
# định nghĩa lớp cho node 
class Node:

  def __init__(self, data):

      self.left = None
      self.right = None
      self.data = data


  # Thêm 1 node mới vào cây nhị phân
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


  # Xóa một node trong cây 
  # To find the inorder successor which is the smallest node in the subtree
  def minvalue(self):
      while self.left is not None:
          current_node = self.left
      return current_node

  def delete(self, ID_delete):
      if self.data == None:
          return
      # TH ID == root, chia lam 2 TH con:
      #   + Duoi node can xoa co 1 node con (Trai hoac phai)
      #   + Duoi node can xoa co 2 node con
      if ID_delete == self.data:     
          if self.left == None:                           # Nếu ptu chỉ có 1 node con, thì thay vị trí node con vs node cần xóa là root.right 
              self.data = self.right                           
          elif self.right == None:                        
              self.data = self.left
          else:
              temp = self.right.minvalue()                                  # Trường hợp node muốn xóa có 2 node con
              self.data = temp.data
              # Tim ptu nho nhat cua right subtree - để thay lên ptu muốn xóa
              # Đệ quy xóa node thay thế trong cây đi, vì ta đã lấy node này thay lên node xóa chính
              self.right.delete(temp.data)             

      elif ID_delete < self.data:                       # Trường hợp ID cần xóa nhỏ hơn ptu node so sánh thì đệ quy cho phần bên trái of node
          self.left.delete(ID_delete)

      else:                                               # Trường hợp ID cần xóa nhỏ hơn ptu node so sánh thì đệ quy cho phần bên trái of node
          self.right.delete(ID_delete)          

      
  # in cây nhị phân ra màn hình   
  def PrintTree(self):                  
      if self.left:
          self.left.PrintTree()
      print("\n" + self.data)
      if self.right:
          self.right.PrintTree()


  # Duyệt cây nhị phân với Inorder traversal 
  # Duyệt các nút trái -> root -> các nút phải
  def Inorder(self, root):
    inorder_lst = []
    if root:
        inorder_lst = self.Inorder(root.left)
        inorder_lst.append("\n" + root.data)
        inorder_lst = inorder_lst + self.Inorder(root.right)
    return inorder_lst


  # Tìm kiếm ptu trên cây
  def Search_ID(self, ID_search):
    if int(ID_search) == int(self.data.split()[0]):     # Kiêm tra xem ID có bằng với giá trị của node ko, nếu có thì in ra
      print("ID %s có thông tin là: " %ID_search)
      print("ID | Name | Day of Birth | Birthplace")
      print(self.data)
    elif int(ID_search) < int(self.data.split()[0]):    # trường hợp ID < giá trị node
      if self.left is not None:                         # Đệ quy tìm ptu cho phần bên trái của node trong trường hợp node khác rỗng
        return self.left.Search_ID(ID_search)
      else:
        print("Không tìm thấy ID bạn nhập! ") 
    else:                                               # Trường hợp ID > giá trị node, đệ quy tìm cho phần bên phải của node
      if self.right is not None:
        return self.right.Search_ID(ID_search)
      else:
        print("Không tìm thấy ID bạn nhập! ")

  """
  Breadth-First Traversal traverse
  https://vimentor.com/vi/lesson/duyet-cay-theo-chieu-rong-1
  """
  def Breadth_First(self):
    queue = []      # tạo hàng đợi để lưu node
    print(queue)
    pass



def menu():
  menu = """
          +-------------------Menu------------------+\n
          Person Tree:\n
          1. Load the data from the file.\n
          2. Insert a new Person.\n
          3. Inorder traverse\n
          4. Breadth-First Traversal traverse\n
          5. Search by Person ID\n
          6. Delete by Person ID\n
          Exit:\n
          0. Exit\n
          +-----------------------------------------.+
          """
  print(menu)
  n = eval(input("Nhập vào chế độ muốn chọn: "))
  return n

def main():

  # Chức năng 1 lưu dữ liệu trong file được cấp vào cây và hiển thị ra màn hình
  if n == 1:
    print("Choice 1: Load data from file and display")
    path = input("Nhập vào file input: ")
    try:
      f = open(path, "r")
      lst = f.readlines()
      value = lst[1:]                        # Bỏ ptu đầu tiên of list là title
      tree = Node(value[0])                  # Lấy ptu đầu tiên để tạo root cho cây nhị phân
      for i in range(1, len(value)):
          tree.insert(value[i])
      print("ID | Name | Day of Birth | Birthplace\n")
      tree.PrintTree()
      print("File được load thành công vào cây nhị phân!")
    except:
      print("Chưa load được file!")

  elif n == 2:
    # Chức năng 2 add 1 thông tin nhân viên ko trùng vào cây có sẵn
    # Đọc và add ptu có sẵn vào tree
    print("Choice 2: Insert a new Person")
    f = open("DATA3.TXT", "r")
    lst = f.readlines()
    value = lst[1:]                        # Bỏ ptu đầu tiên of list là title
    tree = Node(value[0])                  # Lấy ptu đầu tiên để tạo root cho cây nhị phân
    for i in range(1, len(value)):
        tree.insert(value[i])

    # Nhập giá trị cho ptu mới
    new_ID = input("Vui lòng nhập ID mới:")

    # Kiểm tra xem new_ID có trùng không và tiến hành tiếp thao tác
    check = False
    for j in value:
      if j[0] == new_ID:
        check = True
    
    # Tiếp tục insert giá trị nếu new_ID không trùng    
    if check == False:
      name = input("Vui lòng nhập tên:")
      bplace = input("Vui lòng nhập nơi sinh:")
      bday = input("Vui lòng nhập ngày sinh:")
      value_new = [new_ID, name, bplace, bday]
      name_value = ["New ID: ","Name: ","Birthplace: ","Day of birth: "]
      value_new_str = " ".join(value_new)
      for k in range(len(value_new)):
        print(name_value[k] + value_new[k])
      tree.insert(value_new_str)
      print("cây sau khi được thêm phần tử")
      print("ID | Name | Day of Birth | Birthplace\n")
      tree.PrintTree()                       # in ra cây mới được insert
    else:
      print("ID bạn nhập đã tồn tại!")

    # Lưu cây nhị phân tìm kiếm mới vào file ???


  elif n == 3:
    print("Choice 3: Inorder traverse")
    f = open("DATA3.TXT", "r")
    lst = f.readlines()
    value = lst[1:]                        # Bỏ ptu đầu tiên of list là title
    tree = Node(value[0])                  # Lấy ptu đầu tiên để tạo root cho cây nhị phân
    for i in range(1, len(value)):
        tree.insert(value[i])
    order_lst = tree.Inorder(tree)
    f_1 = open("DATA_OUT.TXT", "w")
    print("ID | Name | Day of Birth | Birthplace\n")
    f_1.write("ID | Name | Day of Birth | Birthplace\n")
    for j in order_lst:
      print(j)
      f_1.write(j)

  # Duyệt cây nhị phân với Breadth-First Traversal
  elif n == 4:
    print("Choice 4: Breadth-First Traversal")



  # Tìm thông tin ptu trong cây nhị phân bởi ID
  elif n == 5:
    # Thêm thông tin từ file vao cây
    print("Choice 5: Search by Person ID")
    f = open("DATA3.TXT", "r")
    lst = f.readlines()
    value = lst[1:]                        # Bỏ ptu đầu tiên of list là title
    tree = Node(value[0])                  # Lấy ptu đầu tiên để tạo root cho cây nhị phân
    for i in range(1, len(value)):
        tree.insert(value[i])
    
    # Nhập thông tin cần tìm    
    ID_search = input("Nhập vào ID cần tìm thông tin: ")
    tree.Search_ID(ID_search)               # In ra ptu được tìm thấy

  elif n == 6:
    print("Choice 6: Delete by Person ID")
    ID_delete = input("Nhập vào ID cần xóa: ")
    lst = f.readlines()
    value = lst[1:]                        # Bỏ ptu đầu tiên of list là title
    tree = Node(value[0])                  # Lấy ptu đầu tiên để tạo root cho cây nhị phân
    for i in range(1, len(value)):
        tree.insert(value[i])
    tree.delete(ID_delete)
    tree.PrintTree()

while 1>0:
    try:
        n = menu()
        select = 1
        if select == 1:
            main()
        if n<0 or n>10:
            print("Bạn nhập chế độ chưa đúng! ")
        select = eval(input("Nhấn 1: Tiếp tục \nNhấn 0: Dừng lại "))
        if n == 0 or select == 0:    
            print("Thanks!!!")
            break
    except:
        print("bạn nhập lựa chọn chưa đúng!")