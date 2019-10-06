class EvenList(list):
    def append(self, value):
        if not isinstance(value, int):
            raise TypeError("Error! You can only add integer to this list.")
        if value % 2:
            raise ValueError("Error! You can only append even to this list.")
        super().append(value)


def main():
    try:
        my_list = EvenList()
        my_list.append(3)
        my_list.append(2)
        return
    except ValueError as e:
        print(f"Exception caught!: {e.args[0]}")
    except TypeError as e:
        print(f"Exception caught!: {e.args[0]}")
    except Exception as e:
        print(f"Exception caught!: {e.args[0]}")
    else:
        # I can continue my list operation.
        print(my_list)
    finally:
        # it will be always run.
        # clean up code
        # deallocating memory
        # close
        print("always finally.")

if __name__ == "__main__":
    main()