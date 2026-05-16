
# M-TASK (PYTHON)

# Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham, orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin.
# MASALAN: palindrom_check("dad") return True;  palindrom_check("son") return False;

def palindrom_check(mit: str) -> bool:

    return mit == mit[::-1]


print(palindrom_check("dad"))  
print(palindrom_check("son"))  






# G-TASK (PYTHON)

# Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.


# def get_highest_index(nums):
#     max_val = nums[0]
#     max_idx = 0
    
#     for i, val in enumerate(nums):
#         if val > max_val:
#             max_val = val
#             max_idx = i
            
#     return max_idx

# print(get_highest_index([2, 23, 12, 34, 8])) 
