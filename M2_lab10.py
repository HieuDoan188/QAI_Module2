"""
Lab 10.1 - Chuyển đổi mảng thành heap
Giới thiệu bài toán
Trong bài toán này, bạn sẽ chuyển một mảng các số nguyên thành heap. Đây là một bước quan trọng của 
thuật toán sắp xếp có tên HeapSort. Nó đảm bảo thời gian chạy trong trường hợp xấu nhất của (𝑛 log 𝑛)
so với thời gian trung bình chạy QuickSort của (𝑛 log 𝑛). QuickSort thường được sử dụng trong thực tế,
vì nó thường nhanh hơn, nhưng HeapSort được sử dụng để sắp xếp bên ngoài khi bạn cần sắp xếp các tệp 
lớn không vừa với bộ nhớ của máy tính.

Mô tả bài toán
Nhiệm vụ. Bước đầu tiên của thuật toán HeapSort là tạo một heap từ mảng bạn muốn sắp xếp. Nhân tiện, bạn 
có biết rằng các thuật toán dựa trên Heap được sử dụng rộng rãi để sắp xếp bên ngoài, khi bạn cần sắp xếp 
các tệp lớn không vừa với bộ nhớ của máy tính không?

Nhiệm vụ của bạn là thực hiện bước đầu tiên này và chuyển đổi một mảng số nguyên đã cho thành một heap. 
Bạn sẽ làm điều đó bằng cách áp dụng một số lần swap (hoán đổi) nhất định trên mảng. Swap là một phép toán 
hoán đổi các phần tử 𝑎𝑖 và 𝑎𝑗 của mảng 𝑎 để lấy 𝑖 và 𝑗 nào đó. Bạn sẽ cần phải chuyển đổi mảng thành một heap
chỉ sử dụng (𝑛) swap, như đã mô tả trong bài giảng. Lưu ý rằng bạn sẽ cần sử dụng min-heap thay vì max-heap
trong bài toán này.

+ Định dạng input. Dòng đầu tiên của input chứa duy nhất số nguyên n. Dòng tiếp theo chứa n số nguyên 𝑎𝑖 được 
ngăn bởi dấu cách.

+ Định dạng output. Dòng đầu tiên của output chứa một số nguyên 𝑚 tương ứng với tổng số lần hoán đổi. 𝑚 phải 
thỏa mãn điều kiện 0 ≤ 𝑚 ≤ 4𝑛. Những dòng 𝑚 tiếp theo chứa các phép toán hoán đổi được sử dụng để chuyển 
mảng 𝑎 thành một heap. Mỗi hoán đổi được mô tả bằng một cặp số nguyên 𝑖, 𝑗 tương ứng với các index bắt đầu 
từ 0 của các phần tử được hoán đổi. Sau khi áp dụng tất cả các hoán đổi theo thứ tự đã chỉ định, mảng phải 
trở thành một heap, nghĩa là, với mỗi 𝑖 trong đó 0 ≤ 𝑖 ≤ 𝑛 - 1, các điều kiện sau phải đúng:
1. Nếu 2𝑖 + 1 ≤ 𝑛 − 1 thì 𝑎𝑖 < 𝑎2𝑖+1.
2. Nếu 2𝑖 + 2 ≤ 𝑛 − 1 thì 𝑎𝑖 < 𝑎2𝑖+2.

Lưu ý rằng tất cả các phần tử của mảng input đều khác nhau. Lưu ý rằng bất kỳ dãy hoán đổi nào cũng có độ dài
tối đa là 4𝑛 và sau đó mảng ban đầu trở thành một heap đúng sẽ được đánh giá là đúng.
"""
  

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]

  def FastGenerateSwaps(self):
    for i in range(len(self._data)//2,-1,-1):
      self.SiftDown(i)

  def SiftDown(self, i):
    minIndex = i
    l = 2*i + 1
    if(l < len(self._data) and self._data[l] < self._data[minIndex]):
      minIndex = l
    r = 2*i + 2
    if(r < len(self._data) and self._data[r] < self._data[minIndex]):
      minIndex = r
    if(i!=minIndex):
      self._swaps.append((i, minIndex))
      self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
      self.SiftDown(minIndex)

  def Solve(self):
    self.ReadData()
    # self.GenerateSwaps()
    self.FastGenerateSwaps()
    self.WriteResponse()

heap_builder = HeapBuilder()
heap_builder.Solve()

# Input:
# 5
# 5 4 3 2 1
# Output:
# 3
# 1 4
# 0 1
# 1 3
  
"""
Lab 10.2 - Xử lý song song
Giới thiệu bài toán
Trong bài toán này, bạn sẽ mô phỏng một chương trình xử lý song song một list các công việc. Hệ thống vận hành như Linux,
 MacOS hay Window đều có chương trình đặc biệt gọi là schedulers thực hiện chính xác điều này với các chương trình trong 
 máy tính của bạn.

Mô tả bài toán
Nhiệm vụ. Bạn có một chương trình song song và sử dụng n thread (luồng) độc lập để xử lý list chứa m công việc.
Thread sắp xếp các công việc theo thứ tự đã cho ở input. Nếu có một thread tự do, nó sẽ ngay lập tức lấy công 
việc tiếp theo từ list. Nếu một thread đã bắt đầu xử lý một công việc, nó sẽ không gián đoạn hoặc dừng cho đến
khi hoàn thành quá trình xử lý công việc đó. Nếu một vài thread lấy công việc từ list cùng một lúc, thread có
index nhỏ hơn sẽ lấy công việc đó. Với từng công việc, bạn biết chính xác một thread bất kỳ cần bao lâu để xử 
lý công việc này, và lần này mọi thread đều như nhau. Bạn cần xác định thread nào sẽ xử lý công việc nào và khi 
nào bắt đầu xử lý.

+ Định dạng input. Dòng đầu tiên của input chứa các số nguyên n và m.
Dòng thứ hai chứa m số nguyên ti – thời gian theo giây mà một thread bất kỳ cần để xử lý công việc thứ i.
Thời gian được đưa ra theo thứ tự như trong list mà thread lấy các công việc.
Các thread được đánh số bắt đầu từ 0.

+ Định dạng output. Xuất ra chính xác m dòng. Dòng thứ i (nơi index bắt đầu từ 0 được sử dụng) chứa hai số nguyên được ngăn bởi dấu cách – index bắt đầu từ 0 của thread xử lý công việc thứ i và thời gian theo giây cần thiết để xử lý công việc đó.
"""

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def heapify102(arr, i=0):# MIN HEAP

    #  0 --> time, 1 --> worker

    smallest = i
    l = 2*i + 1 # left child of node i
    r = 2*i + 2 # right child of node i
    if l < len(arr)  and arr[l][0] < arr[smallest][0]:
        smallest = l
    if r < len(arr)  and arr[r][0] < arr[smallest][0]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify102(arr, smallest)
    return arr[0][1] # worker whose time is lowest (top of min-heap)


def assign_jobs(n_workers, jobs):

    result = []
    next_free_time = [0] * n_workers

    for job in jobs:
        zip_time_workers = list(zip(next_free_time, [i for i in range(n_workers)]))
        #list of tuples --> (time, worker)

        next_worker = heapify102(zip_time_workers)
        # get worker with highest priority
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    assigned_jobs = assign_jobs(n_workers, jobs)
    for job in assigned_jobs:
        print(job.worker, job.started_at)

main()

# Input:
# 2 5
# 1 2 3 4 5
# Output:
# 0 0
# 1 0
# 0 1
# 1 2
# 0 4