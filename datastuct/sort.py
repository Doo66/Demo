# 排序算法

def select_sort(items, comp=lambda x, y : x > y):
    """选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i+1, len(items)):
            if comp(items[j],  items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

def bubble_sort(items, comp=lambda x, y : x > y):
    """冒泡排序"""
    items=items[:]
    
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if not swapped:
           break
    return items

"""归并排序"""
def merge(items1, items2, comp=lambda x, y: x < y):
    """合并两个有序列表"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

def merge_sort(items, comp=lambda x, y : x < y):
    return _merge_sort(list(items), comp)

def _merge_sort(items, comp):
    """归并排序"""
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)

def main():
    items = [2,4,1,3,8,6,7]
    select_rets = select_sort(items)
    print(select_rets)
    bubble_rets = bubble_sort(items)
    print(bubble_rets)
    merge_rets = merge_sort(items)
    print(merge_rets)
    
if __name__ == "__main__":
    main()