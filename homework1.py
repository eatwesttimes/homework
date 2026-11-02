# Bài tập về nhà : Tưởng tượng bảng chữ cái alphabet từ a -> z như 1 vòng tròn. Hãy viết chương trình nhận vào một ký tự và hai số nguyên x, n. In ra n ký tự tiếp theo của ký tự đầu vào, mỗi ký tự cách nhau x vị trí trong bảng chữ cái. Nếu vượt quá z thì quay lại a.
char = input()
x = int(input())
n = int(input())
print('\n'.join(chr((ord(char.lower()) - ord('a') + x*(i+1)) % 26 + ord('a')) for i in range(n)))