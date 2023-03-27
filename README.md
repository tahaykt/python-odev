Pytest, Python’da bir test çerçevesidir ve testlerinizi yazmanıza, çalıştırmanıza ve yönetmenize olanak tanır. Pytest, bir dizi özellik sunar ve bu özelliklerden biri de dekoratörlerdir.

Dekoratörler, test fonksiyonlarına veya sınıflarına özel davranışlar eklemek için kullanılır. Bir dekoratör, bir test fonksiyonu veya sınıfı önceden belirlenmiş bir şekilde değiştirir veya genişletir. İşlevsellik eklemek, parametreleri veya çıktıları değiştirmek, hataları ele almak, test verilerini önceden işlemek veya belirli koşullar altında testi atlamak gibi birçok şey yapabilirsiniz.

Pytest’teki en yaygın kullanılan dekoratörler şunlardır:

@pytest.fixture: Test fonksiyonlarına veya sınıflarına bir bağımlılık eklemek veya belirli bir bağımlılığı her test için bir kere çağırmak için kullanılır.

@pytest.mark.parametrize: Test fonksiyonlarına veya sınıflarına farklı giriş değerleri sağlamak için kullanılır. Bu, bir testi, birden fazla giriş değeriyle çalıştırmak için kullanışlıdır.

@pytest.mark.skip: Belirli bir testi atlamak için kullanılır.

@pytest.mark.xfail: Belirli bir testin başarısız olması bekleniyorsa ve başarısızlık raporlanmasına izin verilmemesi gerekiyorsa kullanılır.

@pytest.mark.timeout: Belirli bir testin maksimum süresini belirlemek için kullanılır.
