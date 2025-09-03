def sum(*args):
    total = 0
    for item in args:
        total += item
    return total    

if __name__ == '__main__':
     print(sum(2,3,4,5))
