#region debai
"""
--- ma debai / id
hi(name)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310102022hiname

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/UuuL3NCyCKLVFPiF8

--- debai / problem
Hay viet ham hi(name) xuat ra cau chao theo mota benduoi

--- vidu mau / testcase
Khi chay voi input           | Ketqua output
---------------------------- | -----------------
hi('Mom')                    | Hi Mom!
hi('')                       | Hi!
hi()                         | Hi!
hi(None)                     | Hi!
hi(name='Mom')               | Hi Mom!

------------------- mucdo: kho -----------------
hi('Mom', 'Dad')             | Hi Mom, and Dad!
hi('A', 'B', 'C')            | Hi A, B, and C!
hi('1', '22', '333', '4444') | Hi A, B, and C!
"""
#endregion debai

#region bailam
#             **kwargs to allow calling hi(name='xx') without error > TypeError: hi() got an unexpected keyword argument 'name'
def hi(*args, **kwargs):
  a=[None]*100
  nam=kwargs.get('name')
  tf=False
  i=-1
  if len(args)!=0:
    for i in range(len(args)):
      a[i]=args[i]

  if nam!=None:
      i+=1
      a[i]=nam
      
  if i==-1:
    return 'Hi!'
    
  elif i==0:
    return 'Hi '+a[i]+'!'
    
  else:
    p=0
    s='Hi'
    for j in range(i+1):
      if j!=i:
        s=f"{s} {a[j]},"
      else:
        s=f"{s} and {a[j]}!"
    return s
  
#endregion bailam
