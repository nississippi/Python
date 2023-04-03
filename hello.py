# 辞書
scores = {
    "国語":80,
    "数学":100,
    "化学":70
}

print(scores["国語"])

money = 130

# 数値と文字列の連結
if money >= 10000:
    print(str(money) + '円でディスニーランドに行く')
elif money >= 2000 :
    print(str(money) + '円で映画を見に行く')
else:
    print("たりません")

# タブルは上書き不可、リストは上書き可能
color = (255,255,0)
# color[1] = 0

ink = [255,255,0]
ink[1] = 0

print(color)
print(ink)

# 文字列連結joinメソッド（数値が混ざるとエラーが出る）
print("".join(["Apple", "Orange", "Lemon"]))
print(",".join(("Blue", "Red", "Green")))

# 繰り返し
num = 1
print("Start")

while num < 6:
    print("num = " + str(num))
    num += 1

print("End")