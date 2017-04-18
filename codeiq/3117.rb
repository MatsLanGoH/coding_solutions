# ルビーでも挑戦
# Python3にて解決済みなので言語学習という意味でRubyで再挑戦

# 数学的アプローチ
def count_consec_multiple(num)
  if num % 2 == 0   # 2の倍数は連続数値では出せない ⇒ 0
    0
  else
    m = 1999999 / num
    n = (m / 2.0 + 0.5).to_i
  end
end

nums = Array.new

# TEST用
# nums.push(307)
# nums.push(456)
# nums.push(545)
# nums.push(165)

# 標準入力
while line=gets
    nums.push(line.chomp.to_i)
end

# 結果出力
nums.each { |n| puts count_consec_multiple(n) }
