"""
namedtuple：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。

deque：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，
而deque底层是双向链表，因此当你需要在头尾添加和删除元素是，deque会表现出更好的性能，渐近时间复杂度为$O(1)$。

Counter：dict的子类，键是元素，值是元素的计数，
它的most_common()方法可以帮助我们获取出现频率最高的元素。
Counter和dict的继承关系我认为是值得商榷的，按照CARP原则，Counter跟dict的关系应该设计为关联关系更为合理。

OrderedDict：dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为。

defaultdict：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的setdefault()方法，这种做法更加高效。
"""

"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
counter = Counter(words)
print(counter.most_common(3))