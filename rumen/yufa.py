# coding: utf-8

# if 语句
print ' ---- if start ----'

x = 10
y = 15

if x == 11:
    print 'x is True'
else :
    print 'x is False'
if x == y:
    print 'x = y'    
else:
    print 'x != y'    
    
print ' ---- if end ----'    
    
print '\n#########################################\n'    



# for循环
print ' ---- for start ----'

for x in range(10):
    print x
    
print ' ---- for start ----'
    
print '\n#########################################\n'    



# 函数
print ' ---- def start ----'
def hell():
    print 'Hello def'
    
for x in range(3):
    hell()    
    
    
def add(a, b):
    return a + b

print add(1, 8) *2    

print ' ---- def end ----'
        
print '\n#########################################\n'    



# while循环
print ' ---- while start ----'        

x = 0
while x < 10:
    print x
    x += 2
    

print ' ---- while end ----'        

print '\n#########################################\n'    



# input 捕获用户输入
print ' ---- input start ----'        

name = raw_input('What\'s your name' )
print 'Hello, ' + name

a = raw_input('num1: ')
b = raw_input('num2:')
print int(a) + int(b)

print ' ---- input end ----'        
