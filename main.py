def define_array(SInputFile):  # заполнение массива числами из файла

    a = []
    emp = 0

    try:
        with open(SInputFile) as f:
            while True:
                s = f.readline()  # считываем символ

                if not s:  # выходим, если конец
                    break

                s = s.split()

                for i in range(len(s)):
                    a.append(int(s[i]))
                    emp += 1

    except ValueError:
        print("Error: bad value.")
        f.close()
        return -1
    except FileNotFoundError:
        print("Error: file not found.")
        f.close()
        return -1

    if emp == 0:
        print("Error: file is empty.")
        return -1

    return a


def change_min(a):
    if a[0] < a[1]:
        a[0] = 0

    count_del = 0

    for i in range(1, len(a) - 1):
        if i + 1 >= len(a):
            if count_del > 0:
                for j in range(i, i - count_del, -1):
                    a.pop(j)

                i = i - count_del
                a[i] = 0
            break

        if a[i - 1] > a[i] or count_del > 0:
            if a[i] < a[i + 1] or i + 1 == len(a):
                if count_del > 0:
                    for j in range(i, i - count_del, -1):
                        a.pop(j)
                    i = i - count_del
                    count_del = 0
                a[i] = 0
                continue

            if a[i] == a[i + 1]:
                count_del += 1
                continue

    if a[len(a) - 2] > a[len(a) - 1]:
        a[len(a) - 1] = 0

    return a


def main():
    arr = define_array("1.txt")

    if not isinstance(arr, int):
        print("-------------------")
        print("The original array:")
        print(arr)
        print("-------------------")

        arr = change_min(arr)

        print("--------------")
        print("Changed array:")
        print(arr)
        print("--------------")

    return 0


main()
