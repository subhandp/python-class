data = [
    {
	    "id" : 1,
        "username": "ratna",
        "fullname" : "ratna putri",
        "address" : "jakarta",
        "salary" : 5000000,
        "phone" : '099903',
        "password": "secret"
    },
    {
	    "id" : 2,
        "username": "hamish",
        "fullname" : "hamish daud",
        "address" : "jakarta",
        "salary" : 2000000,
        "phone" : '34232949',
        "password": "secret2"
    },
]

class Auth:
    data = []
    logged_user = False


    @classmethod
    def search(cls,val_search,field_search):
        for i, val in enumerate(cls.data):
            if val[field_search] == val_search:
                return cls.data[i]
        return False

    @classmethod
    def check(cls,user):
        for i,val in enumerate(cls.data):
            if val["username"] ==  user["username"] and val["password"] == user["password"]:
                return True
        return False
    
    @classmethod
    def validate(cls,user):
        if cls.check(user):
            print("user axist")
        else:
            print("user not found")

    @classmethod
    def login(cls,user):
        if  cls.check(user):
            cls.logged_user = user["username"]
            print("found")
            return True
        else:
            return False

    @classmethod
    def logout(cls):
        cls.logged_user = False
        
    @classmethod
    def insert_data(cls,data):
        cls.data.append(data)

    @classmethod
    def user(cls):
        if cls.logged_user:
            user = cls.search(cls.logged_user,"username")
            print(f"username: {user['username']}, fullname: {user['fullname']}")
        else:
            print("logged user not found")

    @classmethod
    def id(cls):
        if cls.logged_user:
            user = cls.search(cls.logged_user,"username")
            print(f"Id user logged in: {user['id']}")
        else:
            print("logged user not found")

    @classmethod
    def read(cls):
        print(cls.data)
    

Auth.insert_data(data[1])
Auth.read()
Auth.id()
Auth.login({"username" : "hamish", "password":"secret2"})
Auth.id()
Auth.user()

