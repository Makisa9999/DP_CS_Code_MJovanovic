def are_all_elements_unique(l):
    seen = set()
    for x in l:
        if x in seen:
            return False
        seen.add(x)
    return True
myfile = open("DP_CS_Code_MJovanovic/tools/MarioCTF/text.txt", "r")
lst = []
item = myfile.read().split('\n')

# print(are_all_elements_unique(item))
print(len( set(item) ) == len ( item ))