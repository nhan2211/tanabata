#w khi viết thêm dữ liệu cũ bị mất viết bằng 'a' sẽ thêm được dữ liệu vào
file = open('hello.txt', 'w') 
file.write('Hello')
file.close()