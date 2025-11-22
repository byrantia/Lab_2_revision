def display_main_menu():
    print("display_menu_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    x = input()
    List_of_text = x.split(",")
    #print(List_of_text)

    List_of_Num = []
    for x in List_of_text:
        x = float(x)
        List_of_Num.append(x)

    #print(List_of_Num)

    return List_of_Num
def  calc_avergae(list):
    x=0.0
    for number in list:
        x = x + number
    x = x/len(list)
    return x
    

def find_min_max(list):
    y = []
    y.append(round(min(list)))
    y.append(round(max(list)))
    return y


def main():
    print("ET0735 -- (DevOps for AIOT)")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    avergae = calc_avergae(num_list)
    print(avergae)
    min_max = find_min_max(num_list)
    print(min_max)

if __name__ == "__main__":
    main()