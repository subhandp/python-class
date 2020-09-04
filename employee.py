
class Employee:
    def __init__(self):
        self.data = []

    def search(self,val_search,field_search):
        return_form = {"status":"notfound", "index":"" }
        for i, val in enumerate(self.data):
            if val[field_search] == val_search:
                return_form["status"] = "found"
                return_form["index"] = i
                return return_form
        return return_form

    def create(self,data):
        if self.search(data["fullname"],"fullname")["status"] == "notfound":
            len_list = len(self.data)
            data["id"] = len_list+1
            self.data.append(data)
        else:
            print(self.search(data["fullname"],"fullname"))
            return False

    def delete(self,id):
        searching_data = self.search(id,"id")
        if searching_data["status"] == "found":
            del self.data[searching_data["index"]]

    def read(self):
        return self.data

    def update(self,id,data):
        data["id"] = id
        searching_data = self.search(id,"id")
        if searching_data["status"] == "found":
            self.data[searching_data["index"]] = data 
            print("data updated")
            return True
        else:
            print("data not found")
            return False

employee = Employee()
employee.create({"fullname":"ratna putri", "address":"jakarta", "salary":5000000, "phone":"099903"}) # id generate secara otomatis ketika data bertambah 	
employee.create({"fullname":"mega mendung", "address":"jakarta", "salary":10000000, "phone":"343234"})
employee.delete(2) # menghapus data employe dengan id 2
employee.read() # return semua data employee yang sudah ditambahkan
employee.update(2,{"fullname":"raisa andriana", "address":"bekasi", "salary":1000000, "phone":"9939999"}) # mengubah data dengan id 2, return semua data employee
print(employee.read())