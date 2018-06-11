

str1 = "clint eastwood"
str2 = "old west action"

str1 = str1.replace(" ",'').lower()
str2 = str2.replace(" ",'').lower()

if len(str1) != len(str2):
    print("False")

# print(str1)
# print(str2)
map = {}
for x in range(len(str1)):
    if map.__contains__(str1[x]):
        map[str1[x]] += 1
    else:
        map[str1[x]] = 1
    
    if map.__contains__(str2[x]):
        map[str2[x]] -= 1
    else:
        map[str2[x]] = -1


found = True
for x,y in map.items():
    if y != 0:
        found = False
        break

if found:
    print("True")
else:
    print("False")


def print_arr(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num,target), max(num,target)))

    return output



print(print_arr([1,2,2,3,4,5,6],4))
