"""
Create 10 files of 1MB size each.
"""


def main():
    try:
        #Solution 1

        data = "A"*1024*1024
        for i in range(10):
            filename = "Test_{:03d}".format(i)
            with open(filename, "w") as fh:
                fh.write(data)

    except Exception as e:
        print("Exception while executing program. Error details: {}".format(str(e)))


if __name__ == "__main__":
    main()
