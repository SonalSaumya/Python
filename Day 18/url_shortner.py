


#Siddhi
class URLShortner:
    url_dict = {}
    base_url = "xyz"

    def add_url(self,ourl):
        if ourl not in URLShortner.url_dict:

            for i in range (len(URLShortner.url_dict)+1):
                URLShortner.url_dict[ourl] = f"{URLShortner.base_url}/{i+1}"
        else:
            print("Already exists")
            print(URLShortner.url_dict[ourl])


u = URLShortner()
u.add_url("example.com")

v = URLShortner()
v.add_url("exams.com")

w= URLShortner()
w.add_url("java.com")


z = URLShortner()
z.add_url("examsapplication.com")


for i in URLShortner.url_dict:
    print(f"{i} -> {URLShortner.url_dict[i]}")



