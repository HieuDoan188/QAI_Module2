"""
Lab 7.1 - Kiểm tra các dấu ngoặc trong đoạn mã
Giới thiệu bài toán
Trong bài toán này, bạn sẽ triển khai một tính năng cho trình soạn thảo văn bản để tìm lỗi sử dụng các dấu ngoặc 
trong đoạn mã.

Mô tả bài toán
Nhiệm vụ. Bạn của bạn đang tạo một trình soạn thảo văn bản cho các lập trình viên. Anh ấy hiện đang nghiên cứu một 
tính năng tìm lỗi khi sử dụng các loại dấu ngoặc khác nhau. Đoạn mã có thể chứa bất kỳ dấu ngoặc nào từ tập hợp
 []{}(), trong đó các dấu mở ngoặc là [, {, ( và các dấu đóng ngoặc tương ứng là ], }, ).

Để thuận tiện, trình soạn thảo văn bản không chỉ thông báo cho người dùng biết có lỗi sử dụng các dấu ngoặc, mà 
còn chỉ ra vị trí chính xác trong đoạn mã chứa dấu ngoặc có vấn đề. Ưu tiên hàng đầu là tìm dấu đóng ngoặc đầu 
tiên không có dấu mở ngoặc tương ứng trước đó, như ] trong ](), hoặc dấu đóng ngoặc không khớp với dấu mở ngoặc, 
như } trong ()[}. Nếu không có lỗi nào như vậy thì nó sẽ tìm dấu mở ngoặc đầu tiên không có dấu đóng ngoặc tương
ứng ở sau, như ( trong {}([]. Nếu không có lỗi nào, trình soạn thảo văn bản phải thông báo cho người dùng rằng 
các dấu ngoặc đã được sử dụng chính xác.

Ngoài các dấu ngoặc, đoạn mã có thể chứa các chữ cái La-tinh hoa và thường, chữ số và dấu câu.

Ở dạng chính thức hơn, tất cả các dấu ngoặc trong đoạn mã phải được chia thành các cặp phù hợp, sao cho trong mỗi
cặp, dấu mở ngoặc đi trước dấu đóng ngoặc và với bất kỳ hai cặp dấu ngoặc nào, một trong hai phải được lồng vào
trong một cặp khác chẳng hạn như trong (foo[bar]) hoặc chúng phải được đặt riêng biệt như trong f(a,b)-g[c].
Dấu mở ngoặc [ tương ứng với dấu đóng ngoặc ], { tương ứng với } và ( tương ứng với ).

+ Định dạng input. Input chứa một string 𝑆 bao gồm các chữ cái La-tinh hoa và thường, chữ số, dấu câu và các dấu 
ngoặc từ tập hợp []{}().

+ Định dạng output. Nếu đoạn mã trong 𝑆 sử dụng đúng các dấu ngoặc, xuất “Success” (Thành công) (không có dấu ngoặc kép).
Nếu không, xuất index của dấu đóng ngoặc chưa khớp đầu tiên (bắt đầu từ 1) và nếu không có dấu đóng ngoặc chưa khớp nào,
hãy xuất index của dấu mở ngoặc đầu tiên không khớp (bắt đầu từ 1).
"""
# Can cai thien them
# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/

# Python3 code to Check for 
# balanced parentheses in an expression
def check(expression):
      
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))
    queue = []
  
    for i in expression:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
    if not queue:
        return "Balanced"
    else:
        return "Unbalanced"
  
# Driver code
string = "{[]{()}}"
print(string, "-", check(string))
  
string = "((()"
print(string,"-",check(string))

# test
# Input:
# {[]}()
# Output:
# Success