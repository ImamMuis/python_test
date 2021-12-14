# 1,2,Frontend,4,Backend,Frontend,7,8,Frontend,Backend,11,Frontend,13,14,Frontend, Backend,16,17,
# Frontend,19,Backend,Frontend,22,23,Frontend,Backend,26,Frontend,28,29,Frontend
# Backend,31,32,Frontend,34,Backend,Frontend,37,38,Frontend,Backend,41,Frontend,43,44,Frontend Backend,46,47,
# Frontend,49,Backend
# Untuk yang bagian angka sudah benar, tinggal bagian teks nya dapat dicoba dihilangkan tanda petik '
# Oh ya, juga mohon diperiksa string yang dibuat sesuai dengan soal nya,
# sesuai dengan indeks masing-masing teks
n = 50
hasil = []
for i in range(1, n+1):
    if i % 3 == 0:
        # hasil.append('Frontend')
        print('Frontend', end=',')
    elif i % 5 == 0:
        # hasil.append('Backend')
        print('Backend', end=',')
    else:
        # print(i)
        print(i, end=',')
        # hasil.append(i)
