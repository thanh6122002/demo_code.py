
'''
Viết phần lõi (core) trong 1 lớp riêng "MyBigNumber", method String sum(String stn1, String stn2) để cài đặt cộng 2 số giống như các học sinh Tiểu học
thực hiện như sau:
Duyệt đồng thời chuỗi stn1, stn2 từ phải sang trái, lấy ra từng kí tự (character), chuyển thành kí số (digit).
Cộng từng kí số.
Ví dụ lệnh sum("1234", "897") sẻ được thực hiện như sau:
Bước 1: Lấy 4 cộng với 7 được 11.
Lưu 1 vào kết quả và nhớ 1.
Bước 2: Lấy 3 cộng với 9 được 12. Cộng tiếp với nhớ 1 được 13
Lưu 3 vào kết quả được kết quả mới là "31"
Ghi nhớ 1.
Lặp lại các bước trên (nhớ lại học sinh lớp 3 đã cộng như thế nào thì lập trình tương tự như vậy)
'''
class MyBigNumber():
    def __init__(self, a, b):
        self.a = str(a)
        self.b = str(b)

    def sum(self):
        lista = [int(i) for i in self.a]
        listb = [int(j) for j in self.b]
        ketqua = []
        du = 0

        for u, v in zip(range(len(lista) - 1, -1, -1), range(len(listb) - 1, -1, -1)):
            tong = lista[u] + listb[v] + du
            ketqua.append(tong % 10)
            du = tong // 10
        for i in range(0, len(lista)-len(listb)):
            tong = lista[i] + du
            ketqua.append(tong % 10)
            du = tong // 10
        if du > 0:
            ketqua.append(du)

        final = ''.join(map(str, ketqua[::-1]))
        return int(final)
my_number = MyBigNumber(2234, 298)
result = my_number.sum()
print(result)
