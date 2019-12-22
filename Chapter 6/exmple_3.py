friends_language =  {
    "Nini" : "Python",
    "Junjun": "Chinese",
    "Xiaogou": "Wangwang",
    "Xiaomao": "Miaomiao"
}

my_list = ["Xiaogou", "Nini"]

for name in friends_language.keys():
    if name in my_list:
        print("Hi " + name + " your favorate language is " + friends_language[name] + ".")
