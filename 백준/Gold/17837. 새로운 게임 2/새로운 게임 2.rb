WHITE = 0
RED = 1
BLUE  = 2
$dirc = {1 => [0, 1], 2 => [0, -1], 3 => [-1, 0], 4 => [1, 0]}
$reverse = {1 => 2, 2 => 1, 3 => 4, 4 => 3}
$N,$K = gets.split.map(&:to_i)
$MAP_C = Array.new($N) { gets.split.map(&:to_i) }
$MAP = Array.new($N) { Array.new($N) { [] } }
$positions = {}
def out?(x,y)
  return !(0<=x && x <$N && 0<=y && y<$N) || $MAP_C[x][y] == BLUE
end
def rePosition(horses, x,y)
  horses.each do |i|
    $positions[i][0] = x
    $positions[i][1] = y
  end
end
def move(x,y,d, n, horses)
  dx, dy = $dirc[d]
  nx, ny = x+dx, y+dy
  if out?(nx,ny)
    if n == 0
      $MAP[x][y] += horses
      return x, y, d
    end
    return move(x,y,$reverse[d], 0, horses)
  elsif $MAP_C[nx][ny] == WHITE
    $MAP[nx][ny]+= horses
  else
    $MAP[nx][ny]+= horses.reverse!
  end
  rePosition(horses,nx,ny)
  return nx, ny, d
end
i = 0
for _ in 0...$K
  r,c,d = gets.split.map(&:to_i)
  $MAP[r-1][c-1].push _
  $positions[i] = [r-1,c-1,d]
  i += 1
end

for _ in 1..1000
  for i in 0...$K
    t = []
    x, y, d = $positions[i]
    while $MAP[x][y].last != i
      t.push($MAP[x][y].pop)
    end
    t.push($MAP[x][y].pop).reverse!
    x,y,d = move(x,y,d,1,t)
    $positions[i][2] = d
    if $MAP[x][y].length > 3
      puts _
      exit
    end
  end
end
puts -1
