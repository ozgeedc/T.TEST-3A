** Dekoratörler diğer bir değişle iç içe fonksiyonlar demektir. Python’da dekoratörler “@” karakteri ile fonksiyonların veya class’ların üzerlerine konularak tanımlanır.**

# Fixture Decorator (Fixture Dekoratörü):
**```pytest.fixture``` olarak kullanılır.Testlerin çalıştırılmasını kolaylaştırmak için kullanılır.**

+ Örnek;
```
import pytest

# E-ticaret sitesi ürün sayfası için veri modeli
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# Fixture tanımı: Örnek bir ürün verisi oluşturuyoruz
@pytest.fixture
def sample_product():
    return Product(name="Example Product", price=100, stock=10)

# Test işlevi: Ürün adını kontrol ediyoruz
def test_product_name(sample_product):
    assert sample_product.name == "Example Product"

# Test işlevi: Ürün fiyatını kontrol ediyoruz
def test_product_price(sample_product):
    assert sample_product.price == 100

# Test işlevi: Ürün stok durumunu kontrol ediyoruz
def test_product_stock(sample_product):
    assert sample_product.stock > 0 
```
# Parametrized Tests Decorator (Parametreli Test Dekoratörü):
**```@pytest.mark.parametrize``` olarak kullanılır.Bir test işlevini farklı parametre setleriyle çalıştırmak için kullanılır.**

+ Örnek;
```
import pytest

# E-ticaret sitesi ürün sayfası için veri modeli
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Fixture tanımı: Örnek bir ürün verisi oluşturuyoruz
@pytest.fixture
def sample_product():
    return Product(name="Example Product", price=100)

# Parametrize edilmiş test işlevi
@pytest.mark.parametrize("product", [
    Product(name="Product A", price=50),
    Product(name="Product B", price=80),
    Product(name="Product C", price=120)
])
def test_product_price(product, sample_product):
    assert product.price == sample_product.price
```

**```sample_product``` adında bir fixture tanımladık. Bu, testlerde kullanılacak örnek bir ürün verisini oluşturur.**
**```test_product_price``` adında bir test işlevi tanımladık. Bu işlev, farklı ürün fiyatları ile sample_product’ın fiyatını karşılaştırır.**

# Skip Decorator (Atla Dekoratörü):

**```@pytest.mark.skip```  olarak kullanılır.Bir testi geçici olarak atlamak için kullanılır. Örneğin,e-ticaret verilerini test ederken fiyat güncellemeleri gibi durumlar için testleri geçici olarak atlayabilirsiniz.**

+ Örnek

```
import pytest

# Ürün sayfası için veri modeli

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Fixture tanımı: Örnek bir ürün verisi oluşturuyoruz

@pytest.fixture
def sample_product():
    return Product(name="Example Product", price=100)

# Test işlevi: Ürün fiyatını kontrol ediyoruz

@pytest.mark.skip(reason="Geçici olarak atlandı: Fiyat güncelleniyor")
def test_product_price(sample_product):
    assert sample_product.price == 100
```

# XFail Decorator (Başarısız Olması Beklenen Test Dekoratörü):
**```@pytest.mark.xfail```  olarak kullanılır.Bir testin bilinçli olarak başarısız olmasını beklediğimizi belirtmek için kullanılır.**

+ Örnek
```
import pytest

# E-ticaret sitesi ürün sayfası için veri modeli
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Fixture tanımı: Örnek bir ürün verisi oluşturuyoruz

@pytest.fixture
def sample_product():
    return Product(name="Example Product", price=100)

# Parametrize edilmiş test işlevi

@pytest.mark.parametrize("product", [
    Product(name="Product A", price=50),
    Product(name="Product B", price=80),
    Product(name="Product C", price=120)
])
@pytest.mark.xfail(reason="Geçici olarak beklenen başarısızlık: Fiyat güncelleniyor")
def test_product_price(product, sample_product):
    assert product.price == sample_product.price
```

**Bu sayede, e-ticaret verilerini test ederken fiyat güncellemeleri gibi durumlar için testleri başarısız olarak işaretleyebiliriz. Ya da bir hata düzeltildiğinde testin tekrar başarılı olması gerektiğini belirtmek için kullanılabilir.**
