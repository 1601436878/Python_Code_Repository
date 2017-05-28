# encoding=utf-8
# 读取手机信息和邮箱信息，合并后再写入新的文件
import os


def fun():
    telefile = open("TeleAddressBook.txt", "rb")
    emailfile = open("EmailAddressBook.txt", "rb")

    telefile.readline()
    emailfile.readline()

    teledata = telefile.readlines()
    emaildata = emailfile.readlines()

    tele_name = []
    tele_phone = []
    tele_email = []
    email_name = []
    email_email = []

    for i in teledata:
        temp = str(i.decode("utf-8"))[:-2]
        list = temp.split()
        tele_name.append(list[0])
        tele_phone.append(list[1])

    for i in emaildata:
        temp = str(i.decode("utf-8"))[:-2]
        list = temp.split()
        email_name.append(list[0])
        email_email.append(list[1])

    print(tele_name)
    print(tele_phone)
    print(email_name)
    print(email_email)

    # 处理数据
    for i in range(len(tele_name)):
        if tele_name[i] in email_name:
            j = email_name.index(tele_name[i])
            tele_email.append(email_email[j])
        else:
            tele_email.append("----")

    for i in range(len(email_name)):
        if email_name[i] not in tele_name:
            tele_name.append(email_name[i])
            tele_email.append(email_email[i])
            tele_phone.append("----")

    list = []
    list.append("姓名\t手机号\t邮箱\n")

    for i in range(len(tele_name)):
        list.append(tele_name[i] + "\t" + tele_phone[i] + "\t" + tele_email[i] + "\n")

    fileout = open("AddressBook2.txt", "w")
    fileout.writelines(list)

    print(tele_email)


if __name__ == "__main__":
    fun()
