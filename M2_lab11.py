"""
Lab 11.1 – Danh bạ điện thoại
Giới thiệu bài toán
Trong bài toán này, bạn sẽ triển khai một trình quản lý danh bạ điện thoại đơn giản.

Mô tả bài toán
Nhiệm vụ. Trong bài toán này, mục tiêu của bạn là triển khai một trình quản lý danh bạ điện thoại đơn giản.
Nó sẽ có thể xử lý các loại truy vấn sau của người dùng:

add number name. Có nghĩa là người dùng thêm một người với tên name và số điện thoại number vào danh bạ. Nếu 
đã tồn tại một người dùng với số như vậy thì trình quản lý của bạn phải ghi đè tên tương ứng.
del number. Có nghĩa là trình quản lý xóa một người có số điện thoại number khỏi danh bạ. Nếu không có người 
nào như vậy thì nó chỉ cần bỏ qua truy vấn.
find number. Có nghĩa là người dùng tìm kiếm một người với số điện thoại number. Trình quản lý nên phản hồi tên
thích hợp hoặc string “not found" (không tìm thấy - không có dấu ngoặc kép) nếu không có người như vậy trong danh bạ.

+ Định dạng input. Có duy nhất số nguyên 𝑁 trong dòng đầu tiên tương ứng với số lượng truy vấn. Tiếp theo là 𝑁 dòng, 
mỗi dòng chứa một truy vấn ở định dạng được mô tả ở trên.

+ Định dạng output. In kết quả của từng truy vấn find - tên tương ứng với số điện thoại hoặc “not found" (không có dấu ngoặc kép) 
nếu không có người nào trong danh bạ có số điện thoại đó. Xuất ra một kết quả trên mỗi dòng theo thứ tự giống thứ tự các truy 
vấn find trong input.
"""




"""
Lab 11.2 - Hashing (Băm) với chain (chuỗi)
Giới thiệu bài toán
Trong bài toán này, bạn sẽ triển khai một hash table (bảng băm) bằng cách sử dụng chaining scheme (lược đồ nối kết chuỗi). 
Đây là một trong những cách phổ biến nhất để triển khai hash table trong thực tế. Hash table mà bạn sẽ triển khai có thể 
được sử dụng để triển khai danh bạ trên điện thoại của bạn hoặc để lưu trữ bảng mật khẩu máy tính hoặc dịch vụ web của bạn 
(nhưng đừng quên lưu trữ các mã băm mật khẩu thay vì chính mật khẩu, nếu không bạn sẽ bị hack!).

Mô tả bài toán
Nhiệm vụ. Trong bài toán này, mục tiêu của bạn là triển khai một hash table với list chaining. Bạn đã được cung cấp 𝑚 bucket
 và 𝑚 hash function (hàm băm). Nó là một hash function đa thức:

add string — chèn string vào bảng. Nếu đã có string đó trong hash table thì chỉ cần bỏ qua truy vấn.
del string — xoá string khỏi bảng. Nếu không có string đó trong hash table thì chỉ cần bỏ qua truy vấn.
find string — xuất “yes" hoặc “no" (không có dấu ngoặc kép) tùy thuộc bảng có chứa string hay không.
check 𝑖 — xuất nội dung của list thứ 𝑖 trong bảng. Sử dụng dấu cách để phân tách các phần tử của list. Nếu list thứ 𝑖 trống, 
xuất ra một dòng trống.
Khi chèn một string mới vào hash chain, bạn phải chèn nó vào đầu chain.

+ Định dạng input. Có duy nhất số nguyên 𝑚 trong dòng đầu tiên ứng với số lượng bucket bạn cần có. Dòng tiếp theo chứa 
số truy vấn 𝑁. Tiếp theo là 𝑁 dòng, mỗi dòng chứa một truy vấn ở định dạng được mô tả ở trên.

+ Định dạng output. In kết quả của từng truy vấn find và check, một kết quả trên một dòng theo thứ tự tương ứng như thứ tự 
của các truy vấn này trong input.
"""


"""
Lab 11.3 - Tìm pattern (mẫu string) trong văn bản
Giới thiệu bài toán
Trong bài toán này, mục tiêu của bạn là triển khai thuật toán Rabin–Karp.

Mô tả bài toán
Nhiệm vụ. Trong bài toán này, mục tiêu của bạn là triển khai thuật toán Rabin–Karp để tìm kiếm pattern trong văn bản đã cho.

+ Định dạng input. Có hai string trong input: pattern 𝑃 và văn bản 𝑇.

+ Định dạng output. In tất cả các vị trí xuất hiện của 𝑃 trong 𝑇 theo thứ tự tăng dần. Sử dụng index của các vị trí 
trong văn bản 𝑇 bắt đầu từ 0.
"""

