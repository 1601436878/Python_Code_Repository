# 字典

def sss():
    data = {"name": "Tom", "password": "123"}
    data2 = {"stunum": "123456", "grade": "100"}
    data["sex"] = "man"
    del data["sex"]
    for i, j in data.items():
        print(i, j)
    data.update(data2)
    data.pop("grade")
    print(data)


if __name__ == "__main__":
    sss()
