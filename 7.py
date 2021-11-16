import xlrd
d = xlrd.open_workbook(filename=r'C:\Users\lenovo\Desktop\day08【excel表读写】\2020年每个月的销售情况.xls',encoding_override=True)

sheet = d.sheet_by_index(0)

rows = sheet.nrows
cols = sheet.ncols

sum_sale = 0
ko = 0
for j in range(0,12):

    for i in range(1,rows):
        data = sheet.row_values(i)
        sum_sale += data[2] * data[4]


    # print(sum_sale)
        ko += sum_sale
print(ko)
ai=0
ad={}
j = 0
l=0
o = 0
u=0
t=0
r=0
e=0
w=0
for k in range(1,rows):
    data = sheet.row_values(k)
    ai += data[4]
    asd = (data[1])
    print(asd)

    if '羽绒服' in asd:
        j += data[4]
        # print(j)

        ad[asd] = j
    if '牛仔裤' in asd:
        l += data[4]
        ad[asd] = l
    if '风衣' in  asd:
        o += data[4]
        ad[asd] = o
    if '皮草' in asd:
        u += data[4]
        ad[asd] = u
    if 'T血' in asd:
        t += data[4]
        ad[asd] = t
    if '马甲' in asd:
        r += data[4]
        ad[asd] = r
    if '小西装' in asd:
        e += data[4]
        ad[asd] = e
    if '皮衣' in asd:
        w += data[4]
        ad[asd] = w
print(ad['羽绒服']/ai)
print(ad['牛仔裤']/ai)
print(ad['风衣']/ai)
print(ad['皮草']/ai)
print(ad['T血']/ai)
print(ad['马甲']/ai)
print(ad['小西装']/ai)
print(ad['皮衣']/ai)
print(ad)

# def zhonlei(a):
#     if a in dict1:
#         a += dict1[key]
#         dict1[key] = values
#     print(dict1)
# while True:
#     if a == '羽绒服'：
#         zhonlei(data[1])

