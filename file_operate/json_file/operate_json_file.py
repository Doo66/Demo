import json
import requests
# 序列化:把对象转换为字节序列的过程称为对象的序列化
# 反序列化:把字节序列恢复为对象的过程称为对象的反序列化
def main():
    mydict = {
        'name': 'hinata',
        'age': 16,
        'lover': 'Naruto',
        'friends': ['Shikamaru', 'Sakura', 'Sasuke'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('hinata.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')

if __name__ == '__main__':
    main()
else:
    print("error")