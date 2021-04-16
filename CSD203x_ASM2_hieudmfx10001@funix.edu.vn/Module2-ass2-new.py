"""
DOAN MINH HIEU - FX10001

Viết chương trình quản lý sản phẩm trong kho hàng của một siêu thị, 
biết rằng mỗi sản phẩm gồm có các thuộc tính: Mã sản phẩm, tên sản phẩm, đơn giá, số lượng.

Chương trình gồm các chức năng sau:

1. Đọc dữ liệu có sẵn từ file text chứa các sản phẩm rồi lưu vào Linked List
2. Nhập và thêm một sản phẩm vào cuối của danh sách Linked List
3. Hiển thị thông tin của các sản phẩm trong Linked List
4. Lưu danh sách các sản phẩm vào file
5. Tìm kiếm thông tin của sản phẩm theo ID
6. Xóa sản phẩm trong danh sách theo ID
7. Sắp xếp các sản phẩm  trong danh sách theo ID
8. Biểu diễn số lượng sản phẩm (đang ở hệ đếm cơ số 10) của phần tử đầu tiên trong Linked List về hệ đếm nhị phân bằng phương pháp đệ quy
9 Đọc dữ liệu từ file chứa các sản phẩm rồi lưu vào stack. Sau đó lấy từng sản phẩm ra khỏi stack rồi hiển thị ra màn hình
10. Đọc dữ liệu từ file chứa các sản phẩm lưu vào queue. Sau đó lấy từng sản phẩm ra khỏi queue rồi hiển thị ra màn hình

ID | Title | Quantity | price
P03 | Sugar | 12 | 25.1
P01 | Miliket | 10 | 5.2
P02 | Apple | 5 | 4.3
P05 | Rose | 7 | 15.4
P07 | Beer | 11 | 12.2
P04 | Book | 9 | 5.2
P06 | Rice | 10 | 3
P08 | French fries | 5 | 3
"""
# Hàm định nghĩa lớp Node gồm dữ liệu vào ptu null phía sau
class Node:
    def __init__(self, data):           
        self.data = data               
        self.next = None 
  
# Định nghĩa lớp linkedlist  
class LinkedList:
    def __init__(self):                 # Hàm khởi tạo linked list
        self.head = None                # giá trị đầu của linked list là null

    # load file vào linked list và thông báo ra màn hình
    def load_file(self, path):
        f = open(path, "r")
        lst = f.readlines()
        lst_value = lst[1:]                         # chỉ lấy dữ liệu từ hàng thứ 2
        for i in range(len(lst_value)):
            new_node_temp = Node(lst_value[i])
            self.add_product(new_node_temp)         # Add từng data vào trong list


    # Add thêm sản phẩm vào linked list
    def add_product(self, new_node):
        if self.head is None:
            self.head = new_node             # Nếu linked list chưa có ptu nào thì add node vua tao là node dau tien được móc nối ns ptu None ở head
            return
        else:
            last = self.head                # Nếu linked list đã có ptu rồi thì duyệt tìm ptu cuối cùng trong linked list
            while last.next != None:          # ptu cuối cùng khi last.next = None
                last = last.next
            last.next = new_node             # gán ptu newnode link vs ptu cuoi vưa tìm được

    # Hiển thị ra giá trị trong linked list
    def Display_data(self):         
        temp = self.head
        while temp:                      # Duyệt và in từng ptu trong linked cho tới khi chạm tới null -> None
            print(temp.data)             # In ra dữ liệu của node đang đứng
            temp = temp.next             # đi tới node tiếp theo


    # Hàm tìm ID trong linked list
    def Search_ID(self, ID_search):
        temp = self.head
        index = 0
        while temp:
            if temp.data[:3] == ID_search:
                return [index, temp.data]          # trả về list index và giá trị của ptu có chứa ID_search
            temp = temp.next
            index = index + 1
        return -1


    # Hàm lưu linked list vào file 
    def Save_product(self, outpath):
        try:
            f = open(outpath, "w")
            f.write("ID | Title | Quantity | price\n")
            temp = self.head
            while temp:                             # Duyệt và in từng ptu trong linked cho tới khi chạm tới null -> None
                f.write(temp.data)
                temp = temp.next   
            self.Display_data()            
            print("File được lưu thành công!")
        except:
            print("Chưa lưu được file !")


    # Hàm xóa ID tìm thấy trong linked list 
    def Deleted_ID(self, ID_delete):            
        temp = self.head                             # gán ptu tạm thời là ptu đầu tiên của linked list
        if temp is not None:             
            if temp.data[:3] == ID_delete:           # nếu ptu đầu tiên = ID sẽ bị thay thế bằng phần tử kế tiếp
                self.head = temp.next
                temp = None                          # gán temp = None để trả về vòng lặp
                return
        while temp is not None:                      # trong khi tìm ID cần delete đổi vị trí của ptu đã bị xóa
            if temp.data[:3] == ID_delete:
                break
            prev = temp                     
            temp = temp.next
        if temp == None:                        # ko trả về gì cả nếu ID không có trong linked list 
            return
        prev.next = temp.next                   # Unlink the node from linked list
        temp = None


    # Hàm convert số lượng của ID được tìm thấy thành binary    
    def Convert(self, ID_cov):
        index = self.Search_ID(ID_cov)
        if index == -1:
            print("Không tìm thấy ptu cần chuyển đổi")
        else:
            # print(index[1])
            conv_data = index[1].split(" | ")[2]
            print("ID ", ID_cov, "có Quantity ",conv_data, "chuyển sang nhị phân là: ")
            conv(int(conv_data))

    # -------------------- Merge sort ---------------------------------------
    # Tìm phần tử giữa của merge sort linedlist
    def getMiddle(self, head):
        if head == None:
            return head
        slow = head
        fast = head
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow      
     
    def sortedMerge(self, a, b):
        result = None
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, h):
        
        if h == None or h.next == None:      # Base case if head is None
            return h
        middle = self.getMiddle(h)          # Tìm ptu ở giữa lst
        next_mid = middle.next              # set the next of middle node to None
        middle.next = None
        left = self.mergeSort(h)                     # Đệ quy merge sort cho list bên trái
        right = self.mergeSort(next_mid)             # Đệ quy merge sort cho list bên phải
        sortedlist = self.sortedMerge(left, right)          # Merge 2 list lại với nhau
        return sortedlist
    # --------------------END merge sort --------------------------------

# Hàm đệ quy convert decima sang nhị phân 
def conv(n):
    if n > 1:
        conv(n//2)  
    print(n % 2, end = '')

# ---------------------stack & queue------------
def load_stack():
    f = open("DATA.TXT", "r")
    lst_stack = []
    lst = f.readlines()
    lst_content = lst[1:]
    for i in lst_content:
        lst_stack.append(i)
    print("ID  | Title | Quantity | price")
    for j in range(len(lst_stack)):
        print(lst_stack.pop())

def load_queue():
    f = open("DATA.TXT", "r")
    lst_queue = []
    lst = f.readlines()
    lst_content = lst[1:]
    for i in lst_content:
        lst_queue.append(i)
    print("ID  | Title | Quantity | price")
    for j in range(len(lst_queue)):
        print(lst_queue.pop(0))
# -------------------------------------------------

# Hàm chọn menu
def menu():
    menu =  """
            +-------------------Menu------------------+\n
            1. Load data from file and display.\n
            2. Input & add to the end.\n
            3. Display data\n
            4. Save product list to file.\n
            5. Search by ID.\n
            6. Delete by ID.\n
            7. Sort by ID.\n
            8. Convert to Binary.\n 
            9. Load to stack and display.\n
            10. Load to queue and display.\n
            Exit:\n
            0. Exit\n
            +-----------------------------------------.+
            """
    print(menu)
    n = eval(input("Nhập vào chế độ muốn chọn: "))
    return n
    
def main():
    mylinkedlist = LinkedList()
    # Choice 1. Đọc dữ liệu có sẵn từ file text chứa các sản phẩm rồi lưu vào Linked List
    if n == 1:
        try:
            print("Choice 1: Load data from file and display")
            path = input("Nhập vào file input: ")
            mylinkedlist.load_file(path)
            print("File được load thành công vào linked list!")
            mylinkedlist.Display_data()
        except:
            print("Chưa thành công load dữ liệu vào linked list!")

    # Choice 2. Nhập và thêm một sản phẩm vào cuối của danh sách Linked List
    elif n == 2:
        import re
        print("Choice 2: Input & add to the end")
        mylinkedlist.load_file("data.txt")
        try:
            ID = input("Nhập vào ID sản phẩm: ") 
            if re.search("^P[0-9]+$", ID) == None:
                print("Bạn nhập giá trị chưa đúng!")
            else:
                name = input("Nhập vào tên sản phẩm: ")
                quantity = int(input("Nhập vào số lượng sản phẩm: "))
                price = float(input("Nhập vào giá trị sản phẩm: "))
                lst_add = [ID, name, quantity, price]
                lst_add = [str(i) for i in lst_add]
                line = " | ".join(lst_add)
                line = "\n" + line
        except:
            print("Bạn nhập giá trị chưa đúng ! ")
        newnode = Node(line)
        mylinkedlist.add_product(newnode)
        mylinkedlist.Save_product("DATA.TXT")
        mylinkedlist.Display_data()

    # Choice 3: Hiển thị thông tin của các sản phẩm trong Linked List
    elif n == 3:
        print("Choice 3: Display data")
        mylinkedlist.load_file("data.txt")
        print("ID | Title | Quantity | price")
        mylinkedlist.Display_data()

    # Choice 4. Lưu danh sách các sản phẩm vào file
    elif n == 4:
        print("Choice 4: Save product list to file")
        mylinkedlist.load_file("data.txt")
        outpath = input("Nhập đường dẫn lưu file: ")    # example: D:\QAI\file_save.txt
        mylinkedlist.Save_product(outpath)

    # 5. Tìm kiếm thông tin của sản phẩm theo ID
    elif n == 5:
        mylinkedlist.load_file("data.txt")
        print("Choice 5: Search by ID")
        ID = input("Nhập vào ID của sản phẩm cần tìm: ")
        index = mylinkedlist.Search_ID(ID)
        if index == -1:
            print("Không tìm thấy thông tin từ ID bạn nhập")
        else:
            print("Thông tin của ID cần tìm là \n", index[1])


    # 6. Xóa sản phẩm trong danh sách theo ID  -> lưu vào file + in ra màn hình
    elif n == 6:
        mylinkedlist.load_file("data.txt")
        print("Choice 6: Deleted by ID")
        ID = input("Nhập vào ID cần xóa: ")
        mylinkedlist.Deleted_ID(ID)
        mylinkedlist.Save_product("DATA.TXT")   # save đè lên file cũ và in ra màn hình


    # 7. Sắp xếp các sản phẩm  trong danh sách theo ID
    elif n == 7:
        mylinkedlist.load_file("data.txt")
        print("Choice 7: Sorted by ID with merge sort in linked list ")
        mylinkedlist.mergeSort(mylinkedlist.head)
        mylinkedlist.Display_data()

    # 8. Biểu diễn số lượng sản phẩm (đang ở hệ đếm cơ số 10) của phần tử đầu tiên trong Linked List về hệ đếm nhị phân bằng phương pháp đệ quy
    elif n == 8:
        mylinkedlist.load_file("data.txt")
        print("Choice 8: Convert to Binary")
        ID = input("Nhập vào ID cần chuyển quantity sang hệ nhị phân: ")
        mylinkedlist.Convert(ID)
    

    # 9 Đọc dữ liệu từ file chứa các sản phẩm rồi lưu vào stack. Sau đó lấy từng sản phẩm ra khỏi stack rồi hiển thị ra màn hình
    elif n == 9:
        print("Choice 9: Load to stack and display")
        load_stack()

    # 10. Đọc dữ liệu từ file chứa các sản phẩm lưu vào queue. Sau đó lấy từng sản phẩm ra khỏi queue rồi hiển thị ra màn hình  
    elif n == 10:
        print("Choice 10: Load to queue and display")
        load_queue()

    
while 1>0:
    try:
        n = menu()
        select = 1
        if select == 1:
            main()
        if n<0 or n>10:
            print("Bạn nhập chế độ chưa đúng! ")
        select = eval(input("\nNhấn 1: Tiếp tục \nNhấn 0: Dừng lại "))
        if n == 0 or select == 0:    
            print("Thanks!!!")
            break
    except:
        print("bạn nhập lựa chọn chưa đúng!")
# ------------END----------------------------------------------
