from models import Product
#p1 與 p2 共享objects

p1 = Product(1, "Apple", 100)
Product.objects.save(p1) #第0項

p2 = Product(2, "Banana", 200)
Product.objects.save(p2) #第1項

print('---查詢 all---')
for p in Product.objects.all():
    print(p) #__str__

print('--- 查詢 id=1 ---')
print(Product.objects.filter(id=1))