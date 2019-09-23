# Inplace remove duplicate elements from list


def main():
    try:
        z = [1, 2, 1, 2, 3, 2, 1, 3, 3, 2, 1, 2, 1, 2, 1, 2, 3, 4, 3, 4, 3]

        for i in z[:]:
            if z.count(i) > 1:
                z.remove(i)

        print(z)

    except Exception as e:
        print("Exception while executing program. Error details: {}".format(str(e)))


if __name__ == "__main__":
    main()
