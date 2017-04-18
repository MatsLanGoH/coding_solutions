# 自分の得意な言語で
# Let's チャレンジ！！
cards = gets.chomp.split(' ')

if ((cards[0] == cards[1]) and (cards[0] == "J"))
  cards[1] = "Q"
end

puts cards[0] + " " + cards[1]
