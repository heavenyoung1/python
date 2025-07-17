def foo(name_look: str):
    list_default = []
    list_modify = []
    for i in name_look:
        list_default.append(i)

    for i in list_default.reverse():
        list_modify.append(i)

    return 'yes' if list_default == list_default else 'no'




name_1 = 'топот'
listing = []
listing_1 = []
for i in name_1:
    #print(i)
    listing.append(i)


for i in listing:
    listing.reverse()
    listing_1.append(i)

    #print(i)

print(listing)
print(listing_1)
print('yes' if listing == listing_1 else 'no')
