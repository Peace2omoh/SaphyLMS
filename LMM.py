import pprint
members = {
    "member_name": ["Sylvana Ekpele","Felicia Grace"],
    "member_id": ["slms0","slms1"]
}
members_name_db = members["member_name"]
members_id_db = members["member_id"]
def member_index(member_id):
    indx = -1
    member_id = str.lower(member_id)
    for i in members_id_db:
        if (i == member_id):
            indx = members_id_db.index(i)
            break

    if indx>=0:
        print(members_name_db[indx]+" found in the Library Members Database")
    else:
        print("member with the id '"+member_id+"' not found in the Library Members Database")
        indx = -1;
    return indx
def add_member(name):
    print("adding member............................")
    members_name_db.append(name)
    members_id_db.append("slms"+str(len(members_name_db)-1))
    print("Library Members Database updated")
    pprint.pprint(members)
    print(".................................\n")