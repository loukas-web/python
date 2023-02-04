count = 1

while True:
    if count % 2 == 0 and count % 3 == 0 and count % 4 == 2 and count % 5 == 4:
        print(count)
        break
    count += 1
