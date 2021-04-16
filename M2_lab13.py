"""
Lab 13.1 - Tính số chặng bay tối thiểu
Giới thiệu bài toán
Bạn muốn tính số chặng bay tối thiểu từ thành phố này đến thành phố khác. Với bài toán này, bạn xây dựng đồ thị vô hướng 
như sau: các đỉnh biểu diễn các thành phố, có một cạnh giữa hai đỉnh mỗi khi có chuyến bay giữa hai thành phố tương ứng. 
Sau đó, chỉ cần tìm đường ngắn nhất từ một trong những thành phố đã cho đến thành phố kia.

Mô tả bài toán
Nhiệm vụ. Cho một đồ thị vô hướng có n đỉnh, m cạnh và hai đỉnh u và v, hãy tính độ dài của đường ngắn nhất từ u đến v 
(tức là số cạnh nhỏ nhất của đường từ u đến v).

Định dạng input. Đồ thị ở định dạng chuẩn. Dòng tiếp theo chứa hai đỉnh u và v.

Định dạng output. Xuất ra số cạnh tối thiểu của đường đi từ u đến v, hoặc −1 nếu không có đường nào.
"""

"""
Lab 13.2 - Kiểm tra xem một đồ thị có phải là lưỡng phân không
Giới thiệu bài toán
Một đồ thị vô hướng được gọi là lưỡng phân nếu các đỉnh của nó có thể được chia thành hai phần sao cho mỗi cạnh của 
đồ thị nối hai đỉnh từ các phần khác nhau. Đồ thị lưỡng phân phát sinh một cách tự nhiên trong các ứng dụng mà đồ thị 
được sử dụng để mô hình hóa kết nối giữa các đối tượng thuộc hai kiểu khác nhau (ví dụ: nam và nữ; hoặc sinh viên và ký túc xá).

Một định nghĩa khác là: một đồ thị là lưỡng phân nếu các đỉnh của nó có thể được tô bằng hai màu (giả sử: đen và trắng) 
sao cho hai điểm đầu cuối của mỗi cạnh có màu khác nhau.

Mô tả bài toán
Nhiệm vụ. Cho một đồ thị vô hướng có n đỉnh và m cạnh, hãy kiểm tra xem nó có phải là lưỡng phân hay không.

+ Định dạng input. Một đồ thị ở định dạng chuẩn.

+ Định dạng output. Xuất ra 1 nếu đồ thị là lưỡng phân và 0 nếu không phải.
"""

