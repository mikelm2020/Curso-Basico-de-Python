def run():
    LIMIT = 1000

    counter = 0
    print(counter)
    while counter < LIMIT:
        counter +=1
        if counter % 5 != 0:
            continue
        if counter > 900:
            break
        print(counter)


if __name__ == '__main__':
    run()
