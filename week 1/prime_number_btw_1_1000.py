for num in range(1, 100):
    count = 0
    for i in range (2, num//2 +1):
        if num % i == 0:
            count += 1
            break
    if count == 0 and num != 1 :
        print("%d" %num, end = " ")
        