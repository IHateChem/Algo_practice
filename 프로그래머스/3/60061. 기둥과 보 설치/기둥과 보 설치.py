def solution(n, build_frame):
    building = set()
    def check():
        for x, y, a in building:
            if a:
                if (x,y-1,0) in building or (x+1,y-1,0) in building or ((x-1,y,1) in building and (x+1,y,1) in building): continue
                else: return False
            else:
                if y == 0 or (x,y-1,a) in building or (x,y,1) in building or (x-1,y,1) in building: continue
                else: return False
        return True
    def build(x,y, a, b):
        building.add((x,y,a))
        if not check(): building.remove((x,y,a))
    def remove(x,y, a, b):
        building.remove((x,y,a))
        if not check(): building.add((x,y,a))
    for x,y,a,b in build_frame:
        if b: build(x,y,a,b)
        else: remove(x,y,a,b)
    return sorted(list(building))