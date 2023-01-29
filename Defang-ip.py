#Defang IP

#Given an IP Address
#address = "1.1.1.1"

#Output: "1[.]1[.]1[.]1"

given_ip="1.1.1.1"

convert_list=given_ip.split(".")

print (convert_list)

#Convert to a defanged IP
defang_str='[.]'.join(convert_list)

print (defang_str)
