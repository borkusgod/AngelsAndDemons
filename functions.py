# functions file for angels and demons app

def list_all_dem():
    print('This will print out the list of demons.')


def list_all_ang():
    print('This will print out the list of angels.')

def get_dem_inf():
    gt_name = input("Please enter the demon name: ")
    gt_numb = input("Please enter the demon number: ")
    gt_type = input("Please enter the demon type: ")
    gt_alt_nm = input("Please enter any alternate name: ")
    gt_ang_eq = input("Please enter the angel that is equivalent: ")
    return [gt_name, gt_numb, gt_type, gt_alt_nm, gt_ang_eq]

get_from_func = get_dem_inf()

print(f"The demon's name is: {get_from_func[0]}")
print(f"The demon's number is: {get_from_func[1]}")
print(f"The demon's type is: {get_from_func[2]}")
print(f"The demon's alternate name is: {get_from_func[3]}")
print(f"The demon's angel equivalent is: {get_from_func[4]}")
