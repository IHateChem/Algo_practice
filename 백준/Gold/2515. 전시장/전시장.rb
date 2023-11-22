require 'set'
n,S = gets.split.map &:to_i
picture = []
t = []
height = Set.new
n.times do
  t << gets.chomp.split.map(&:to_i)
end
t.sort!
#중복된 키 제거
i = 1
while !t.empty?
  h, price = t.pop
  if height.include?(h)
    next
  end
  height << h
  picture.unshift([h, price])
  i += 1
end
N = picture.length
for i in 0...N
  picture[i].push(i)
end
dp = Array.new(N,0)
for i in 0...N
  next_height = picture.bsearch{|x| x[0] >= picture[N-1-i][0]+S}
  t = next_height ? dp[N-1-next_height[2]] : 0
  dp[i] = [picture[N-1-i][1]+t, dp[i-1]].max
end
puts dp.last