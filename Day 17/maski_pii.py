# def mask_sensitive_info(info,info_type):
#     if info_type == "email":
#         email_id, domain = info.split("@")
#         masked_email_id = email_id[0] + "***" + email_id[-1]
#         return masked_email_id + "@" + domain
#
#     elif info_type == "credit_card":
#         masked_card = "***8" * (len(info))//4 + info(-4)
#         return masked_card
# print (mask_sensitive_info())



# def mask(info,type):
#     new_str = ""
#     if type=="email":
#         info=list(info)
#         new_str+=info[0]
#
#         for i in range(1,len(info)):
#             if(info[i] != "@"):
#                 new_str+="*"
#             else:
#                 #new_str += info[i]
#     print(new_str)
#
#

#
# def mask(info,type):
#     new_str=""
#
#     if type=="email":
#         info = list(info)
#         new_str+=info[0]
#
#         for i in range(1,len(info)):
#             if info[i] != "@":
#                 #new_str += info[i]
#                 new_str += "*"
#             else:
#                 j=i
#                 for j in range(i,)
#     return  new_str
#
#
# info = "abc@gmail.com"
# type = "email"
# print(mask(info,type))








