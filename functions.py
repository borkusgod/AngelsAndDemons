# functions file for angels and demons app

def list_all_dem():
    print('This will print out the list of demons.')


def list_all_ang():
    print('This will print out the list of angels.')

def get_dem_inf():
    gt_name = input("Please enter the demon name: ")
    gt_numb = input("Please enter the demon name: ")
    gt_type = input("Please enter the demon name: ")
    gt_alt_nm = input("Please enter the demon name: ")
    gt_ang_eq = input("Please enter the demon name: ")
    return list(gt_name, gt_numb, gt_type, gt_alt_nm, gt_ang_eq)
