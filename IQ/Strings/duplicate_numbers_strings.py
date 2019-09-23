# Inplace remove duplicate characters of string


def main():
    try:
        w = "shdhssdhhsgdhsdhdsdhsdghsdgsdhsdgshdsgdsk"
        for i in w[:]:
            cnt = w.count(i)
            if cnt > 1:
                w = w.replace(i, "", (cnt - 1))

        print(w)

    except Exception as e:
        print("Exception while executing program. Error details: {}".format(str(e)))


if __name__ == "__main__":
    main()
