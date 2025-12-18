#No using the built in type check function
#https://www.w3schools.com/python/python_try_except.asp
from os import strerror


def sum(arr : list) -> int:
    """
    Modify the function such that it returns the sum of all numbers within the given list.
    :param arr:
    :return:
    """
    i = 0
    n = 0
    while i < len(arr):
        try:
            n += arr[i]
        except :
            pass
        i+=1
    return n
#print(sum([0,2,3,6,1, "hello"]))

def cleanData(rawData : list) ->list:
    """
    modify the function such that it takes in a list as an argument will return a new list that
     contains only the valeus that can be typecast to a float.
    :param rawData:
    :return:
    """
    p = 0
    newlist = []
    while p <len(rawData):
        try:
            newlist.append(float(rawData[p]))
        except :
            pass
        p +=1
    return newlist
#print(cleanData([1,6,2,6,"cat","14.5"]))
def unreliableCalculator(divisors : list) -> list:
    """
    Modify the function such that it takes in a list as an argument and returns a new list where each
    index is 100 divided by the values from the input list.
    If division ever causes an error instead have the value be the type of error as a string.
    Example the list [100,50,25,"5"] as an argument would return [1, 2, 4, "TypeError"]
    :param divisors:
    :return:
    """
    i = 0
    newer = []
    while i < len(divisors):
        try:
            newer.append(100/divisors[i])
        except TypeError:
            newer.append("TypeError")
        except ZeroDivisionError:
            newer.append("ZeroDivisionError")
        except AssertionError:
            newer.append("AssertionError")
        except:
            pass
        i +=1
    return newer
#print(unreliableCalculator([10,2,4,"6"]))
def upperAll(arr : list) -> None:
    """
    Modiy the function such that is uppercases all strings within the given argument list.
    The string method .upper() turns all characters in as string uppercase.
    You should modify the original list not return a new list.
    :param arr:
    :return:
    """
    i = 0
    while i < len(arr):
        try:
            arr[i] = arr[i].upper()
        except:
            arr[i] = arr[i]
        i +=1
    x = "hello"
    print(x)
    x = x.upper()
    print(x)
print(upperAll(["cat",1, "dog", "fish"]))
def firstItems(arr : list) -> list:
    """
    Modify the function below such that given a list of values. Many of the list elements will be lists
    themselves. For any list element that is a list grab the first element from that list. If the list
    element is not a list then just grab the value itself.
    Create a new list of all the first indexes of inner lists or just values themselves.
    Example firstItems( [[1,2],[3,4],[5,6],[7,8]],9 ) == [1,3,5,7,9]
    :param arr:
    :return:
    """
    i = 0
    newlist = []
    while i < len(arr):
        try:
            item = arr[i]
            x = item[0]
            newlist.append(x)
        except:
            newlist.append(arr[i])
        i+=1
    return newlist
print(firstItems([[1,2],[3,4],[5,6],[7,8],9]))
