# TIL(08/24-데이터베이스 만들기)

#### (1) render & redirect 차이

- render : html 파일을 바로 보여주고 싶을 때
- redirect : view를 거쳐서 (함수를 실행해서) html 파일을 보여주고 싶을 때



#### (2) calss 정의

```python
class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    products=models.CharField(max_length=20)
    
class Product_Bybrand(models.Model):
    Product=models.OneToOneField(Product,on_delete=models.CASCADE,primary_key=True)
    Starbucks=models.CharField(max_length=30, null=True)
    Twosome=models.CharField(max_length=30, null=True)
    TomandToms=models.CharField(max_length=30, null=True)
    Ediya=models.CharField(max_length=30, null=True)
    Mega=models.CharField(max_length=30, null=True)
    Hollys=models.CharField(max_length=30, null=True)
    Coffeebean=models.CharField(max_length=30, null=True)
    Coffeebay=models.CharField(max_length=30, null=True)
    Angelinus=models.CharField(max_length=30, null=True)
    Pascucci=models.CharField(max_length=30, null=True) 
    
class Price_Bybrand(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE,primary_key=True)
    Starbucks=models.IntegerField(null=True)
    Twosome=models.IntegerField(null=True)
    TomandToms=models.IntegerField(null=True)
    Ediya=models.IntegerField(null=True)
    Mega=models.IntegerField(null=True)
    Hollys=models.IntegerField(null=True)
    Coffeebean=models.IntegerField(null=True)
    Coffeebay=models.IntegerField(null=True)
    Angelinus=models.IntegerField(null=True)
    Pascucci=models.IntegerField(null=True)
    
    
```



- OneToOneField : 일대일참조.
- on_delete=models.CASCADE : 모델의 Product 테이블의 Primary Key가 지워지면, 그 외래키를 포함하는 Product_Bybrand의 행을 삭제한다.



#### (3) CSV 파일 Import하기

- DB Browser의 메뉴 **File > Import > Table from CSV file**

데이터를 DB에 Import하기 위해서는 DB가 생성되어있고, 해당 DB가 DB Browser에서 Open된 상태여야 한다.

- null값을 True로 주지 않는다면 빈칸의 숫자는 0으로 표기된다.

