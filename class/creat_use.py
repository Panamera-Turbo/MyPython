#创建一个类
class car():
    '一个类，描述车的品牌和速度'    #帮助文档，__doc__读取

    def __init__(self, brand, speed):
        #self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        #__init__()是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        
        #初始化brand和speed
        self.brand = brand
        self.speed = speed
    
    def start(self):
        print(self.brand.title(),'has started')

    def speed_up(self):
        print(self.brand.title(),'speed up!')
    
# 类中函数称为方法，如上述init,start,speed_up。
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
# 为了避免Python默认方法与其发生矛盾，通常在前后加上两个'_'

#创建实例
MyCar = car('audi',350)
#访问实例的属性
print('\n',MyCar.__doc__)
MyCar.start()

#给属性指定默认值
class car_1():
    '一个类，描述车的品牌,速度和油耗'#帮助文档，__doc__读取

    def __init__(self, brand, speed, gas):
        #self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        #__init__()是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        #初始化brand和speed
        self.brand = brand
        self.speed = speed
        self.odometer = 605   #设置行驶里程默认值
        self.gas = 60

    def getGas(self):
        print(self.brand.title(), 'has used', str(self.gas)+'L gas')

MyCar_1 = car_1('porsche', 350, 95)
print(MyCar_1.brand.title(), 'has ran', MyCar_1.odometer, 'miles in total')
MyCar_1.getGas()

#修改属性的值：
# 方法1：直接用赋值修改
# 方法2：利用方法修改


# 继承：
# 编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用继承。
# 一个类 继承 另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，而
# 新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

#创建一个子类：
# 创建子类时，父类必须包含在当前文件中，且位于子类前面
class car_eletric(car_1):
    def __init__(self, brand, speed, gas):      #初始化父类的属性
        super().__init__(brand, speed, gas)       # super()是一个特殊函数，
        # 帮助Python将父类和子类关联起来。这行代码让Python调用car_eletricelc
        # 的父类的方法 __init__()，让ElectricCar实例包含父类的所有属性。
        self.battery = 100  #添加子类的属性
    
    def getBattery(self):   #添加描述新方法
        print(self.brand, 'is now in', self.battery, 'percent battery')

    #重写父类中的方法：
    # 简而言之，就是在子类中添加新的方法，并且与父类中想要重写的方法同名，来“覆盖”父类
    # 好处：更改/去除父类中不需要/冗余的方法，避免无意义的调用
    def getGas(self):
        print('NO GAS!')
        
MyCar_2 = car_eletric('Tesla', 320, 0)
MyCar_2.getBattery()
MyCar_2.getGas()

