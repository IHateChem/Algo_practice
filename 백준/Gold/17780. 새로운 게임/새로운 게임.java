import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

class Main {
    public static void move(String[][] MAP, List<Integer>[][] unitMap, Integer[] unitDir, Integer K, Integer N){
        Integer [][] directions = {{0,1},{0,-1},{-1,0},{1,0}};
        for(int unit=0; unit<K; unit ++){
            boolean flag = false;
            for(int i=1; i<N+1; i++){
                for(int j=1; j<N+1; j++){
                    if(unitMap[i][j] == null || unitMap[i][j].size() == 0 || !unitMap[i][j].get(0).equals(unit)){
                        continue;
                    }
                    List<Integer> unitList = unitMap[i][j];
                    int ni, nj;
                    ni = i + directions[unitDir[unit]][0];
                    nj = j + directions[unitDir[unit]][1];
                    switch(MAP[ni][nj]){
                        case "0":
                            if(unitMap[ni][nj] == null){
                                unitMap[ni][nj] = new ArrayList<>();
                            }
                            for(int k=0; k<unitList.size(); k++){
                                unitMap[ni][nj].add(unitList.get(k));
                            }
                            unitMap[i][j] = new ArrayList<>();
                            break;
                        case "1":
                            if(unitMap[ni][nj] == null){
                                unitMap[ni][nj] = new ArrayList<>();
                            }
                            for(int k=unitList.size()-1; k>=0; k--){
                                unitMap[ni][nj].add(unitList.get(k));
                            }
                            unitMap[i][j] = new ArrayList<>();
                            break;
                        case "2":
                            ni = i - directions[unitDir[unit]][0];
                            nj = j - directions[unitDir[unit]][1];
                            int dir = unitDir[unit];
                            dir = (dir%2 == 0) ? dir+1 : dir-1;
                            unitDir[unit] = dir;
                            if(MAP[ni][nj].equals("0")){
                                if(unitMap[ni][nj] == null){
                                    unitMap[ni][nj] = new ArrayList<>();
                                }
                                for(int k=0; k<unitList.size(); k++){
                                    unitMap[ni][nj].add(unitList.get(k));
                                }
                                unitMap[i][j] = new ArrayList<>();
                            }else if(MAP[ni][nj].equals("1")){
                                if(unitMap[ni][nj] == null){
                                    unitMap[ni][nj] = new ArrayList<>();
                                }
                                for(int k=unitList.size()-1; k>=0; k--){
                                    unitMap[ni][nj].add(unitList.get(k));
                                }
                                unitMap[i][j] = new ArrayList<>();

                            }
                    }
                    flag = true;
                    break;

                }
                if(flag){
                    break;
                }
            }
        }

    }

    public static boolean check(List<Integer>[][] unitMap, Integer N) {
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(unitMap[i+1][j+1] != null && unitMap[i+1][j+1].size() >= 4){
                    return true;
                }
            }
        }
        return false;
    }
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s = bf.readLine();
        int N,K;
        N = Integer.parseInt(s.split(" ")[0]);
        K = Integer.parseInt(s.split(" ")[1]);
        String[][] MAP = new String[N+2][N+2];
        List<Integer>[][] unitMap = new ArrayList[N+2][N+2];
        Integer [] unitDir = new Integer[K];
        for(int i=0; i<N+2; i++){
            for(int j=0; j<N+2; j++){
                MAP[i][j] = "2";
            }
        }
        for(int i=0; i<N; i++){
            String[] split = bf.readLine().split(" ");
            for(int j=0; j<N; j++){
                MAP[i+1][j+1] = split[j];
            }
        }
        for(int i=0; i<K; i++){
            s = bf.readLine();
            unitDir[i] = Integer.parseInt(s.split(" ")[2])-1;
            int x = Integer.parseInt(s.split(" ")[0]);
            int y = Integer.parseInt(s.split(" ")[1]);
            unitMap[x][y] = new ArrayList<>();
            unitMap[x][y].add(i);
        }
        for(int i=0; i<1000; i++){
            move(MAP, unitMap, unitDir, K, N);
            if(check(unitMap, N)){
                System.out.println(i+1);
                return;
            }
        }
        System.out.println(-1);
    }
}