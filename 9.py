

############     生产着消费者模型       ##########

from threading import Thread


cabinet = 500
import time
qwe = time.time()
class Chef(Thread):
    username = ''
    num = 0
    def run(self) -> None:
        global cabinet
        while True:
            asd = time.time()
            if cabinet < 500 and asd - qwe < 10:
                cabinet = cabinet + 1
                self.num += 1
                print('%s做了%s个' % (self.username,self.num))

            elif asd - qwe < 10:
                time.sleep(3)
            else:

                print('%s做了%s个挣了%s元' % (self.username,self.num,self.num*1.5))
                # print('{}做了{}个'.format (self.username,self.num))
                break


class User(Thread):
    username = ''
    num = 0
    money = 5000
    def run(self) -> None:
        global cabinet
        while True:
            asd = time.time()
            if cabinet > 0 and asd - qwe < 10  and self.money > 3:
                self.money -= 3
                cabinet = cabinet - 1
                self.num += 1
            elif asd - qwe < 10:
                time.sleep(2)
            else:

                # print('%s买了%s个' % (self.username,self.num))
                print('{}买了{}个'.format (self.username,self.num))
                break








p1 = User()
p2 = User()
p3 = User()
p4 = User()
p5 = User()
p6 = User()
p1.username = '1'
p2.username = '2'
p3.username = '3'
p4.username = '4'
p5.username = '5'
p6.username = '6'

c3 = Chef()
c2 = Chef()
c1 = Chef()
c3.username = '流畅'
c2.username = '流畅1'
c1.username = '流畅2'



p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()


c3.start()
c2.start()
c1.start()


















