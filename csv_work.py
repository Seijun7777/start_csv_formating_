# --->>> Levenshtein <<<---

# input_word1 = input(">>> ")
# input_word2 = input(">>> ")
#
# def input_(p1, p2):
#     num = 0
#     if len(p1) == len(p2):
#         for i in range(len(p1)):
#             if p1[i] != p2[i]:
#                 num += 1
#             else:
#                 num = num
#     else:
#         return ">>> Error!"
#     return num
# ii = input_(input_word1, input_word2)
# print(ii)


# --->>> csv_formating <<<---

# def data_transform(p1):
#     dict_information = {
#         "Gender":{},
#         "Email":{},
#         "Age":{},
#         "City":{},
#         "Device":{},
#         "Order At":{}}
#     first_index = p1[0].split(',')
#     for i in p1[1:]:
#         a = i.split(',')
#
#         for keys in dict_information.keys():
#             if a[first_index.index(keys)] not in dict_information[keys]:
#                 dict_information[keys][a[first_index.index(keys)]] = 1
#             else:
#                 dict_information[keys][a[first_index.index(keys)]] += 1
#     return dict_information
#
#     #second variant
#                 # dict_info['Gender'] = {'Male': a.count('Male'), 'Female': a.count('Female')}
#                 # dict_info['Email'] = {'yahoo.com': a.count('yahoo.com'), 'hotmail.com': a.count('hotmail.com')}
#                 # dict_info['Age'] = {'21->40': a.count('21->40'),'66->99': a.count('66->99'),'41->65': a.count('41->65')}
#                 # dict_info['City'] = {'Seattle': a.count('Seattle'),'Detroit': a.count('Detroit'), 'Las Vegas': a.count('Las Vegas'), 'Chicago': a.count('Chicago')}
#                 # dict_info['Device'] = {'Safari iPhone': a.count('Safari iPhone'), 'Chrome Android': a.count('Chrome Android'), 'Chrome': a.count('Chrome')}
#                 # dict_info['Order At'] = {'afternoon': a.count('afternoon'), 'moring': a.count('morning')}
#
#
#         # return i
#
#
# def run():
#     info = ["Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At", "Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon", "Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon", "Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon", "Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning", "Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon"]
#     return data_transform(info)
# print(run())







# --->>> My_roman_numerals <<<---
#
# input_r_num = int(input(">>> Enter number: "))
#
#
# def roman_numbers(p1):
#     return_ = ""
#     roman_translate = {
#         1000 : "M",
#          900 : "CM",
#          500 : "D",
#          400 : "CD",
#          100 : "C",
#          90 : "XC",
#          50 : "L",
#          40 : "XL",
#          10 : "X",
#          9 : "IX",
#          5 : "V",
#          4 : "IV",
#          1 : "I"}
#     for keys, values in roman_translate.items():
#         division = p1 // keys
#         if p1 > 0:
#             return_ += values * division
#             p1 -= division * keys
#     return return_
# print(roman_numbers(input_r_num))

# --->>> csv_formating <<<---

# from datetime import datetime
#
# def gmail(inpu):
#     return inpu.split("@")[1]
#
# def time(inpu):
#     d = datetime.strptime(inpu, '%Y-%m-%d %H:%M:%S').hour
#     if 6 < d < 12:
#         return "morning"
#     elif 12 < d < 18:
#         return "afternoon"
#     elif 18 < d < 24:
#         return "evening"
#
# def age(inpu):
#     if 0 < inpu < 21:
#         return "1->20"
#     elif 20 < inpu < 41:
#         return "21->40"
#     elif 40 < inpu < 66:
#         return "41->65"
#     elif 65 < inpu < 100:
#         return "66->99"
#
# def my_data_transform(param_1):
#     res = ["Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At"]
#     for i in param_1.split("\n")[1:-1]:
#         ar = i.split(",")
#         ar[4] = gmail(ar[4])
#         ar[5] = age(int(ar[5]))
#         ar[9] = time(ar[9])
#         res.append(",".join(ar))
#     return res
#
#
# def join():
#     inpu = "Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At\nMale,Carl,Wilderman,carl,wilderman_carl@yahoo.com,29,Seattle,Safari iPhone,2,2020-03-06 16:37:56\nMale,Marvin,Lind,marvin,marvin_lind@hotmail.com,77,Detroit,Chrome Android,2,2020-03-02 13:55:51\nFemale,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21,Las Vegas,Chrome,1,2020-03-05 17:53:05\nFemale,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,81,Seattle,Chrome,2,2020-03-04 10:33:53\nMale,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,47,Chicago,Chrome Android,1,2020-03-05 15:19:48\n"
#     return my_data_transform(inpu)
# print(join())