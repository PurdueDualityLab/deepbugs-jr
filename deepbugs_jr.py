def test(x):
    return x

def main():
    values = [3.14, 0, "Hello World", True]
    message = "Given {parameter} the function returns {value}."
    for x in values:
        data = test(x)
        print(message.format(parameter=x, value=data))

if __name__ == "__main__":
    main()
