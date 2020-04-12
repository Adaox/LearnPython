def tables(wedding_party, nonox):
    table_new = [x for x in wedding_party if x not in nonox[-1]]
    table = table_new[:5]
    for y in table:
        if y in wedding_party:
            wedding_party.remove(y)
    return table, wedding_party


wedding_party = ['John', 'Mike', 'Bill', 'Alice', 'Michele', 'Ron', 'Alex',
                 'Jessica', 'Tom', 'Becky', 'Erica', 'Rob', 'Ingrid', 'Brad',
                 'Mitch']

nono1 = ['Mike', 'Bill']
nono2 = ['Ron', 'Alex']
nono3 = ['Ingrid', 'Erica']


table1, wedding_party = tables(wedding_party, nono1)
table2, wedding_party = tables(wedding_party, nono2)
table3, wedding_party = tables(wedding_party, nono3)

print('Table 1: ', table1)
print('Table 2: ', table2)
print('Table 3: ', table3)
