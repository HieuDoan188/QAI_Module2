"""
DOAN MINH HIEU - FX10001

Assg1: Sắp xếp_tìm kiếm cơ bản
Xây dựng chương trình để thực hiện các công việc sắp xếp và tìm kiếm trên một dãy số thực. 

Chương trình gồm các chức năng sau:
    1. Nhập một dãy các số thực gồm có n số (n<=20) lưu vào tệp INPUT.TXT
    2. Đọc dữ liệu từ tệp INPUT.TXT lưu vào mảng 1 chiều a và hiển thị ra màn hình.
    3. Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần, 
theo từng bước của thuật toán Bubble Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT1.TXT
    4. Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần,
theo từng bước của thuật toán Selection Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT2.TXT
    5. Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần, 
theo từng bước của thuật toán Insert Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT3.TXT
    6. Sử dụng phương pháp tìm kiếm tuần tự, hãy liệt kê ra màn hình chỉ số các phần tử (biết rằng 
phần tử đầu tiên có chỉ số là 0) trong mảng a chưa được sắp xếp ở câu 2 có giá trị lớn hơn value 
(value là một số thực được nhập vào từ bàn phím), kết quả tìm được lưu vào dòng tiếp theo trong tệp OUTPUT4.TXT
    7. Sử dụng phương pháp tìm kiếm nhị phân, hãy tìm chỉ số phần tử đầu tiên có giá trị bằng value 
(value là một số thực được nhập vào từ bàn phím) trên mảng đã a đã được sắp xếp.
"""

# Bài làm:
def get_input(path): # Hàm get dữ liệu từ file input.txt
    file_2 = open(path,"r")
    f = file_2.readline()
    lst_1 = f.split(",")
    lst_1 = [int(i) for i in lst_1]
    return lst_1

# Hàm cho Bubble_Sort
def Bubble_Sort(lst_1):
    print("Choice 3: Bubble sort")
    f = open("OUTPUT1.TXT","w")
    break_sig = True        # tạo tín hiệu để thoái vòng lặp trong trường hợp ko còn lần đổi chỗ nào nữa
    for i in range(len(lst_1)-1):
        break_sig = True
        for j in range(len(lst_1)-1-i):    
            if lst_1[j] > lst_1[j+1]:
                a = lst_1[j]
                lst_1[j] = lst_1[j+1]
                lst_1[j+1] = a
                break_sig = False
        line = [str(i) for i in lst_1]
        line = " ".join(line)
        f.writelines(line)
        f.writelines("\n")  # thêm kí tự xuống dòng cho file txt
        print(lst_1)
        if break_sig:
            break
    f.close()

# Hàm cho Selection sort
def Selection_sort(lst_1):
    print("Choice 4: Selection sort")
    f = open("OUTPUT2.TXT","w")

    for i in range(len(lst_1)-1):
        min1 = min(lst_1[i+1:])  
        index_min = lst_1.index(min1)         
        if lst_1[i] > min1:
            a = lst_1[i]
            lst_1[i] = lst_1[index_min]
            lst_1[index_min] = a  

        line = [str(i) for i in lst_1]
        line = " ".join(line)
        f.writelines(line)
        f.writelines("\n")
        print(lst_1)
    f.close()


# hàm cho Insertion sort
def Insertion_sort(lst_1):
    print("Choice 5: Insertion sort")
    f = open("OUTPUT3.TXT","w")

    for i in range(len(lst_1)-1):
        change = min(lst_1[i+1:])
        if lst_1[i] > change:
            a = lst_1[i]
            lst_1[lst_1.index(change)] = a
            lst_1[i] = change

        line = [str(i) for i in lst_1]
        line = " ".join(line)
        f.writelines(line)
        f.writelines("\n")
        print(lst_1)
    f.close()

# Ham cho tim kiem tuan tu - linear search
def linear_search(lst_1):
    print("Choice 6: Linear Search")
    value = eval(input("Nhập vào giá trị cần tìm: "))
    f = open("OUTPUT4.TXT","w")

    lst_2 = []
    for i in lst_1:
        if i > value:
            lst_2.append(lst_1.index(i))
    if lst_2 == []:
        print("Không có giá trị nào lớn hơn value!")
    else:
        print("Vị trí phần tử lớn hơn value là: ", lst_2)

    line = [str(i) for i in lst_2]
    line = " ".join(line)
    f.writelines(line)
    f.writelines("\n")
    f.close()

def binary_search(lst_1):
    print("Choice 7: Binary Search")
    lst_1.sort()
    value = eval(input("Nhập vào giá trị cần tìm: "))

    m = len(lst_1) 
    n = 0
    while m>n:
        mid = int((m+n)/2)
        if lst_1[mid] == value:
            return mid + 1  
        elif lst_1[mid] < value:
            n = mid
        else:
            m = mid

def select_menu():
    menu = """
            +-------------------Menu------------------+\n
            |      1.Manual Input                      |\n
            |      2.File input                        |\n        
            |      3.Bubble sort                       |\n         
            |      4.Selection sort                    |\n        
            |      5.Insertion sort                    |\n
            |      6.Search > value                    |\n
            |      7.Search = value                    |\n
            |      0.Exit                              |\n
            +-----------------------------------------.+
            """
    print(menu)
    n = eval(input("Lựa chọn chế độ: "))
    return n

def main():
    if n == 1:
        try:
            print("Choice 1: Manual Input\n")
            l = eval(input("Nhập vào số phần tử của chuỗi: "))
            str1 = input("Nhập vào các giá trị của chuỗi: ")
            str1 = str1.split()
            if len(str1)==l:
                file_1 = open("INPUT.TXT", "w")
                str1 = ",".join(str1)
                file_1.write(str1)
                file_1.close()
            else:
                print("Chuỗi giá trị bạn nhập vào chưa đúng!")
        except:
            print("Bạn nhập không đúng định dạng!")
    elif n == 2:
        try:
            print("Choice 2: File input")
            path = input("Nhập vào đường dẫn file input: ")
            print("Chuỗi giá trị cần sắp xếp là: ", get_input(path))
        except:
            print("Bạn chưa nhập dữ liệu đầu vào!!")
    elif n == 3:
        try:
            lst_1 = get_input("INPUT.TXT")
            Bubble_Sort(lst_1)
        except:
            print("Bạn chưa nhập dữ liệu đầu vào!")
    elif n == 4:
        try:
            lst_1 = get_input("INPUT.TXT")
            Selection_sort(lst_1)
        except:
            print("Bạn chưa nhập dữ liệu đầu vào!")
    elif n == 5:
        try:
            lst_1 = get_input("INPUT.TXT")
            Insertion_sort(lst_1)
        except:
            print("Bạn chưa nhập dữ liệu đầu vào!")
    elif n == 6:
        try:
            lst_1 = get_input("INPUT.TXT")
            linear_search(lst_1)
        except:
            print("Bạn chưa nhập dữ liệu đầu vào!")
    elif n == 7:
        try:
            lst_1 = get_input("INPUT.TXT")
            print("Vị trí cần tìm là : ", binary_search(lst_1))
        except:
            print("Bạn chưa nhập dữ liệu đầu vào!")

while 1>0:
    n = select_menu()
    select = 1
    if select == 1:
        main()
    if n<0 or n>7:
        print("Bạn nhập chế độ chưa đúng! ")
    select = eval(input("Nhấn 1: tiếp tục \nNhấn 0: Dừng lại "))
    if n == 0 or select == 0:    
        print("Thanks!!!")
        break
# ------------END----------------------------------------------
