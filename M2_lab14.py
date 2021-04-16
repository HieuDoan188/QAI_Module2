"""
Lab 14.1 - Tính chi phí tối thiểu cho một chuyến bay
Giới thiệu bài toán
Giờ bạn không chỉ muốn giảm chi phí mỗi chặng bay mà là tổng chi phí của một chuyến bay. Trong bài toán này, 
bạn sẽ xây dựng một đồ thị trọng số: trọng số của một cạnh từ thành phố này sang thành phố kia là chi phí của chuyến bay tương ứng.

Mô tả bài toán
Nhiệm vụ. Cho một đồ thị có hướng với các trọng số cạnh dương với n đỉnh và m cạnh cũng như hai đỉnh u và v, 
hãy tính trọng số của đường đi ngắn nhất giữa u và v (nghĩa là tổng trọng số nhỏ nhất của đường đi từ u đến v ).

+ Định dạng input. Biểu đồ ở định dạng chuẩn. Dòng tiếp theo chứa hai đỉnh u và v.

+ Định dạng output. Xuất ra trọng số tối thiểu của một đường đi từ u đến v, hoặc −1 nếu không có đường nào cả.
"""



"""
Lab 14.2 - Phát hiện sự bất thường trong tỷ giá hối đoái
Bạn được cho một list các đơn vị tiền tệ c1, c2 ,. . . , cn cùng với list tỷ giá hối đoái: rij là số đơn vị tiền tệ cj 
mà người ta nhận được cho một đơn vị ci. Bạn muốn kiểm tra xem liệu với một đơn vị tiền tệ nào đó, có thể thực hiện một 
chuỗi hoán đổi và nhận về nhiều hơn một đơn vị của cùng một loại tiền tệ hay không. Nói cách khác, bạn muốn tìm 
tiền tệ ci1, ci2 ,. . . , cik sao cho ri1, i2 · ri2, i3 · rik − 1, ik, rik, i1> 1. Trong bài toán này, bạn xây dựng 
đồ thị sau: các đỉnh là các đơn vị tiền tệ c1, c2 ,. . . , cn, trọng số của một cạnh từ ci đến cj bằng - log rij. Chỉ 
cần kiểm tra xem có chu kỳ âm nào trên biểu đồ này hay không. Thật vậy, giả sử chu trình ci → cj → ck → ci có trọng số âm.
Tức là - (log cij + log cjk + log cki) <0 và do đó log cij + log cjk + log cki> 0. Điều này có nghĩa là:

Mô tả bài toán
Nhiệm vụ. Cho một biểu đồ có hướng với trọng số cạnh có thể âm và với n đỉnh và m cạnh, hãy kiểm tra xem liệu nó có chứa 
chu kỳ có trọng số âm hay không.

+ Định dạng input. Một biểu đồ ở định dạng chuẩn.

+ Định dạng output. Xuất ra 1 nếu biểu đồ có chứa chu kỳ trọng số âm và xuất ra 0 trong trường hợp ngược lại.
"""

