from time import time

def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1

def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

def main():
    items = [10,1,2,3,4,5,6,7,8,9]
    items.sort()
    print(items)
    index = seq_search(items, 9)
    print(index)
    index = bin_search(items, 9)
    print(index)
    
if __name__ == "__main__":
    main()