def zeros_new_list(numbers):
    new_list = []
    zero_count = 0
    for num in numbers:
        if num!=0:
            new_list.append(num)
        else:
            zero_count +=1
            for i in range(zero_count):
                new_list.append(0)
                return new_list
            numbers=[0,1,0,3,12,0,5]
            print(zeros_new_list(numbers))