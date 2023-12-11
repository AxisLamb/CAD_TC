import string
import random

# s = string.ascii_letters
# r = random.choice(s)
# #航班号用CPA+4位整数和一个随机字母
# Flight_1 = "CPA"+str(randint(1000, 9999))+r
# Flight_2 = "CPA"+str(randint(1000, 9999))+r
# print(Flight_1,Flight_2)
# #TemplateName 随机生成数
# TemplateName = "Test"+str(random.uniform(1, 1000))
# print(TemplateName)

num = random.randint(0, 9)
random_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
random_flght = str(num) + random_str
print(random_flght)
