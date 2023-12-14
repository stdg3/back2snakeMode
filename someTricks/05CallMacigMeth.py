int_num = 4
float_num = 5.5

print(int_num.__mul__(float_num))
# NotImplemented => __mul__ => int

print(float_num.__rmul__(int_num))
# 22.0

# print(int_num + float_num)

# magic methodlar cagilmasi esnasinda NotImplemented geri degfer gelirse yerleri degistitilip r ile baslayan method casgrilir
