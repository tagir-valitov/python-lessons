import collections
def binary_search(list, elem):
    low = 0
    high = len(list) - 1
    while low <= high:
        middle = (low + high)//2
        if list[middle] == elem:
            return middle
        elif list[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1


my_list = [1, 3, 4, 5, 6, 7]
print(binary_search(my_list, 3))
default_dict = collections.defaultdict(list)
default_dict[1].append(1)
print(dict(default_dict))
counter = collections.Counter([1, 2, 3, 3, 4, 5, 4, 5])
for elem, count in counter.items():
    print('{}: {}'.format(elem, count))
class Histori_Chat:
    def __init__(self):
        self.messages = []
    def append_message(self,message):
        self.messages.append(message)


class Message:
    def __init__(self, autor, text):
        self.autor = autor
        self.text = text

client = Histori_Chat()
client.append_message(112)
print(client.messages)


with open('name.txt', 'w', encoding='utf8') as f:
    print(f.write('u7yy8t7'))
    f.close()



