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
# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    contactsDA = [None for i in range(0, 10000000)]
    for cur_query in queries:
        if cur_query.type == 'add':
##            # if we already have contact with such number,
##            # we should rewrite contact's name
##            for contact in contacts:
##                if contact.number == cur_query.number:
##                    contact.name = cur_query.name
##                    break
##            else: # otherwise, just add it
##                contacts.append(cur_query)
            contactsDA[cur_query.number] = cur_query
        elif cur_query.type == 'del':
##            for j in range(len(contacts)):
##                if contacts[j].number == cur_query.number:
##                    contacts.pop(j)
##                    break
            contactsDA[cur_query.number] = None
        else:
            response = 'not found'
##            for contact in contacts:
##                if contact.number == cur_query.number:
##                    response = contact.name
##                    break
            if(contactsDA[cur_query.number] != None):
                response = contactsDA[cur_query.number].name
            result.append(response)
    return result

write_responses(process_queries(read_queries()))

# Input
# 12
# add 911 police
# add 76213 Mom
# add 17239 Bob
# find 76213
# find 910
# find 911
# del 910
# del 911
# find 911
# find 76213
# add 76213 daddy
# find 76213
# Output:
# 3
# Mom
# not found
# police
# not found
# Mom
# daddy


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
class Query1:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.hashTable = [[]] * bucket_count

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query1(input().split())

    def process_query_naive(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.hashTable[query.ind])
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.hashTable[self._hash_func(query.s)].index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.hashTable[self._hash_func(query.s)].append(query.s)
            else:
                if ind != -1:
                    self.hashTable[self._hash_func(query.s)].pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

bucket_count = int(input())
proc = QueryProcessor(bucket_count)
proc.process_queries()

# Input:
# 5
# 12
# add world
# add HellO
# check 4
# find World
# find world
# del world
# check 4
# del HellO
# add luck
# add GooD
# check 2
# del good
# Output:
# HellO world
# no
# yes
# HellO
# GooD luck

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
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences_naive(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def poly_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
    	ans = (ans * x + ord(c)) % prime
    return ans

def precompute_hashes(text, plength, p, x):
    H = [0] * (len(text) - plength + 1)
    s = text[-plength:]
    H[len(text)-plength] = poly_hash(s, p, x)
    y = 1
    for i in range(1, plength+1):
        y = (y * x) % p
    for i in reversed(range(len(text) - plength)):
        prehash = x * H[i + 1] + ord(text[i]) - y * ord(text[i + plength])
        while(prehash < 0):
            prehash += p
        H[i] = prehash % p
    return H

def get_occurrences(pattern, text):
    p = 1000000007
    x = random.randint(1, p)
    # tlength = len(text) 
    plength = len(pattern)
    phash = poly_hash(pattern, p, x)
    H = precompute_hashes(text, plength, p, x)
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if phash == H[i] and text[i:i + len(pattern)] == pattern
    ]

print_occurrences(get_occurrences(*read_input()))

# Input:
# aba
# abacaba
# Output:
# 0 4