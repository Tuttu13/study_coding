# クラスの定義
class Neko:
  
  def __init__(self, breed, color, tail, neko_skill):
    self.breed = breed             # 猫種
    self.color = color             # 毛の色
    self.tail  = tail              # しっぽの有無
    self.neko_skill = neko_skill   # ねこ技を設定

  # 属性に対して操作を行うメソッドの定義
  def hissatsu(self):
    print(f'{self.breed}の必殺技{self.neko_skill}!')

neko1 = Neko('マンチカン', '真っ白', '長い', 'ネコパンチ')
print(neko1.color)
neko2 = Neko('スコティッシュフォールド', '三毛猫', 'ふさふさ', 'ネコキック')
print(neko2.tail)
print(neko1.hissatsu())
print(neko2.hissatsu())

class Koneko(Neko):
  
  def __init__(self, color, tail, name, neko_skill):
    super().__init__('マンチカン', color, tail, neko_skill)

    self.name = name

  def hissatsu(self):
    print(f'{self.color}色の赤ちゃんマンチカンの必殺技{self.neko_skill}') 
  
  def say_hello(self):
    print(f'はじめまして、私の名前は{self.name}だにゃ')

koneko = Koneko('オフホワイト', '短い', 'しろねこ', 'ねこじゃらし攻撃')
print(koneko.tail)
print(koneko.breed)
print(koneko.hissatsu())
print(koneko.say_hello())
