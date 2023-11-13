n = gets.to_i
tabs = gets.split.map &:to_i
tabs_correct = gets.split.map &:to_i
tabs_dif = tabs_correct.zip(tabs).map {|x,y| x- y}
dp = Array.new(n, 0)
dp[0] = tabs_dif[0].abs
current_type = tabs_dif[0] > 0
for i in 1...n
  if current_type == tabs_dif[i] > 0
    if tabs_dif[i].abs <= tabs_dif[i-1].abs
      dp[i] = dp[i-1]
    else
      dp[i] = dp[i-1] + (tabs_dif[i-1]-tabs_dif[i]).abs
    end
  else
    current_type = tabs_dif[i] > 0
    dp[i] = dp[i-1] + tabs_dif[i].abs
  end
end
puts dp[n-1]