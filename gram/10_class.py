class Practice:

    # 클래스 속 메소드의 매개변수의 첫번째는 항상 자동으로 인스턴스 자체를 가져온다. 인스턴스를 불러올때는 self를 생략
    def __init__(self, something):
        self.something = something
    
    def some_function(self):
        print(self.something)

a = Practice('zzz')

a.some_function() # zzz