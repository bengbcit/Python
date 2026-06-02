def main():
    # loop functions
    # loops()

    # dictionary
    dict_fn()


# def loops():
#     # 1 while Loop
#     i = 3
#     while i > 0:
#         print(i)
#         i -= 1

#     # 2 for Loop
#     for i in range(3, 0, -1):
#         print(i)

#     # for list in [3, 2, 1]:
#     for i in [3, 2, 1]:
#         print(i)

#     # _ : variable that is not used again
#     for _ in range(3):
#         print("Hello")

#     # 3 break and continue
#     i = 0
#     while i < 5:
#         if i == 3:
#             break
#         print(i)
#         i += 1

#     j = 0
#     while j < 5:
#         j += 1
#         if j == 3:
#             continue
#         print(j)

#     while True:
#         n = int(input("Enter a number: "))
#         if n > 0:
#             break

#     for _ in range(n):
#         print("Hello")



def dict_fn():
    # dictionary
    d = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": None}
    ]

    print(d[0]["name"])

    # print(d.get("age"))
    # print(d.get("country", "USA"))

    for person in d:
        print(person["name"], person["age"], person["city"], sep=" | ")


main()
