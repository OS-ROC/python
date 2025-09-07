from my_utils.file_util import print_file_info, append_to_file  # 导入自定义包和模块
from my_utils.str_util import str_reverse, substr

s1 = str_reverse("booker tao")
s2 = substr("booker tao",3,10)
print(s1)
print(s2)

print_file_info("bill.txt")
append_to_file("123.txt","iaijdaooaj")