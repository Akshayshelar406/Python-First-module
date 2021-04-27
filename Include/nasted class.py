class Demo:
    def method1(self):
        print('This is Demo class Method 1')

    class User:
        def method2(self):
            print('This is User class Method 2')

d = Demo()
d.method1()

d1 = Demo.User()
d1.method2()