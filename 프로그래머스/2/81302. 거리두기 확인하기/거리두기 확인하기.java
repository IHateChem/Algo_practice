import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;


class Solution {
    public int[] solution(String[][] places) {
        List<Integer> answer = new ArrayList();
        for(String[] place: places){
            if(checkPlace(place)){
                answer.add(1);
            }else{
                answer.add(0);
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
    public boolean checkPlace(String[] place){
        boolean flag = true;
        boolean[][] visited = new boolean[5][5];
        for(int n=0; n<5; n++){
            for(int m=0; m<5; m++){
                visited[n][m] = false;
            }
        }
        
        for(int n=0; n<5; n++){
            for(int m=0; m<5; m++){
                if(!place[n].substring(m, m+1).equals("P")) continue;
                visited[n][m] = true;
                List<int[]> stack = new ArrayList();
                for(int[] dndm: List.of(new int[]{1,0},new int[]{0,1}, new int[]{-1,0},new int[]{0,-1})){
                    int nn = n + dndm[0];
                    int nm = m + dndm[1];
                    if(0<=nn && nn<5 && 0<=nm && nm<5){
                        if(place[nn].substring(nm, nm+1).equals("P")) return false;
                        if(place[nn].substring(nm, nm+1).equals("O")){
                            visited[nn][nm] = true;
                            stack.add(new int[]{nn,nm});
                       }
                    }
                }
                for(int[] pos: stack){
                    for(int[] dndm: List.of(new int[]{1,0},new int[]{0,1}, new int[]{-1,0},new int[]{0,-1})){
                        int nn = pos[0] + dndm[0];
                        int nm = pos[1] + dndm[1];
                        if(0<=nn && nn<5 && 0<=nm && nm<5 && !visited[nn][nm]){
                            if(place[nn].substring(nm, nm+1).equals("P")) return false;
                        }
                    }
                }
            }
        }
        return true;
    }
}