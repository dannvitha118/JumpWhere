list1 = [{},{},{}]
list2 = [{'a': 1}, {}, {}]
def all_dict_empty(lst):
    return all(len(d) == 0 for d in lst)

print(all_dict_empty(list1))
print(all_dict_empty(list2))
