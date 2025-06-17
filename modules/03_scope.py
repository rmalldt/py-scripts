def scope_test():
    for i in range(1, 5):
        if i == 3:
            myvar = i  # var is created in if block inside for loop
    print(f"My var: {myvar}")  # var is still available outside for loop


scope_test()
