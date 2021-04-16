"""
Lab 12.1 - Tìm lối thoát khỏi một mê cung
Giới thiệu bài toán
Mê cung là một lưới các ô hình chữ nhật với các vách nằm giữa các ô liền kề. Bạn muốn kiểm tra xem có đường nào từ một ô nhất 
định đến một lối ra nhất định trong một mê cung hay không, trong đó lối ra cũng là một ô nằm trên cạnh của mê cung (trong ví
dụ ở bên phải có hai lối ra: một ở cạnh trái và một ở cạnh phải). Trong bài toán này, bạn cần biểu diễn mê cung dưới dạng một
đồ thị vô hướng: các đỉnh của đồ thị là các ô của mê cung, hai đỉnh được nối với nhau bằng một cạnh vô hướng nếu chúng liền kề
và không có vách ngăn nào giữa chúng. Sau đó, để kiểm tra xem có đường đi giữa hai ô đã cho trong mê cung hay không, bạn chỉ 
cần kiểm tra xem có đường nào giữa hai đỉnh tương ứng trên đồ thị hay không.

Mô tả bài toán
Nhiệm vụ. Cho một đồ thị vô hướng và hai đỉnh phân biệt 𝑢 và 𝑣, hãy kiểm tra xem có đường từ 𝑢 đến 𝑣 hay không.

+ Định dạng input. Một đồ thị vô hướng với 𝑛 đỉnh và 𝑚 cạnh. Dòng tiếp theo chứa hai đỉnh 𝑢 và 𝑣 của đồ thị.

+ Định dạng output. Xuất ra 1 nếu có đường nối từ u đến v và 0 nếu không có.
"""


"""
Lab 12.2 - Thêm lối thoát cho mê cung
Giới thiệu bài toán
Giờ bạn cần đảm bảo rằng không có ngõ cụt nào trong mê cung, hay, có ít nhất một lối thoát đối với mỗi ô. Trong trường hợp này,
bạn cần tìm các thành phần liên thông nhau trên biểu đồ vô hướng tương ứng và đảm bảo rằng mỗi thành phần chứa một ô thoát.

Mô tả bài toán
Nhiệm vụ. Cho một đồ thị vô hướng với 𝑛 đỉnh và 𝑚 cạnh, hãy tính số thành phần liên thông trong đó.

+ Định dạng input. Biểu đồ có định dạng chuẩn.

+ Định dạng output. Xuất ra số thành phần liên thông.
"""

