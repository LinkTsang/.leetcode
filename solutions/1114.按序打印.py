#
# @lc app=leetcode.cn id=1114 lang=python3
#
# [1114] 按序打印
#

# @lc code=start
from threading import Lock


class Foo:
  def __init__(self):
    self.firstLock = Lock()
    self.secondLock = Lock()
    self.firstLock.acquire()
    self.secondLock.acquire()

  def first(self, printFirst: 'Callable[[], None]') -> None:

    # printFirst() outputs "first". Do not change or remove this line.
    printFirst()
    self.firstLock.release()

  def second(self, printSecond: 'Callable[[], None]') -> None:
    self.firstLock.acquire()
    # printSecond() outputs "second". Do not change or remove this line.
    printSecond()
    self.secondLock.release()

  def third(self, printThird: 'Callable[[], None]') -> None:
    self.secondLock.acquire()
    # printThird() outputs "third". Do not change or remove this line.
    printThird()
# @lc code=end


def printFirst():
  print('first')


def printSecond():
  print('second')


def printThird():
  print('third')


foo = Foo()
