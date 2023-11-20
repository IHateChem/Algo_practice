require 'set'
A,B,C = gets.split.map &:to_i
visited = Set["0,0,#{C}"]
stack = [[0,0,C]]
while not stack.empty?
  a,b,c = stack.pop
  t = [B-b, a].min
  if !visited.include?("#{a-t},#{b+t},#{c}")
    visited.add("#{a-t},#{b+t},#{c}")
    stack.push([a-t,b+t,c])
  end

  t = [C-c, a].min
  if !visited.include?("#{a-t},#{b},#{c+t}")
    visited.add("#{a-t},#{b},#{c+t}")
    stack.push([a-t,b,c+t])
  end
  t = [C-c, b].min
  if !visited.include?("#{a},#{b-t},#{c+t}")
    visited.add("#{a},#{b-t},#{c+t}")
    stack.push([a,b-t,c+t])
  end

  t = [A-a, b].min
  if !visited.include?("#{a+t},#{b-t},#{c}")
    visited.add("#{a+t},#{b-t},#{c}")
    stack.push([a+t,b-t,c])
  end

  t = [B-b, c].min
  if !visited.include?("#{a},#{b+t},#{c-t}")
    visited.add("#{a},#{b+t},#{c-t}")
    stack.push([a,b+t,c-t])
  end

  t = [A-a, c].min
  if !visited.include?("#{a+t},#{b},#{c-t}")
    visited.add("#{a+t},#{b},#{c-t}")
    stack.push([a+t,b,c-t])
  end
end
answer = Set.new
visited.each do |v|
  a,b,c = v.split(",").map &:to_i
  if a == 0
    answer.add(c)
  end
end
puts answer.sort.join(" ")