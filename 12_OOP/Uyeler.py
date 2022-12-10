class Uyeler:
    user_name = str()
    password = str()
    name = str()
    last_name = str()
    phone = str()

    def info(self):
        userinfo = dict()
        userinfo["user_name"] = self.user_name
        userinfo["password"] = self.password
        userinfo["name"] = self.name
        userinfo["las_name"] = self.last_name
        userinfo["phone"] = self.phone

        return userinfo

    @classmethod  # cls => cls ifadesi Class üzerinden çağrılabileceğini belirtir.
    def ara(cls, user_name, liste):

        for i in liste:
            if i.user_name == user_name:
                userinfo = dict()
                userinfo["user_name"] = i.user_name
                userinfo["password"] = i.password
                userinfo["name"] = i.name
                userinfo["las_name"] = i.last_name
                userinfo["phone"] = i.phone
                return userinfo
