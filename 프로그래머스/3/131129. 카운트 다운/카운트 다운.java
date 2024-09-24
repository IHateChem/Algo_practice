import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
class Solution {
    public int[] solution(int target) {
        List<Integer> single = new ArrayList();
        List<Integer> doub = new ArrayList();
        List<Integer> triple = new ArrayList();
        int[] answer = {};
        
        for(int i =1; i< 21; i++){
            single.add(i);
        }
        single.add(50);
        for(int i =1; i< 21; i++){
            if(single.contains(i*2)) continue;
            doub.add(i*2);
        }
        for(int i =1; i< 21; i++){
            if(single.contains(i*3)) continue;
            if(doub.contains(i*3)) continue;
            triple.add(i*3);
        }
        List<Integer> notSingle = new ArrayList();
        notSingle.addAll(doub);
        notSingle.addAll(triple);
        notSingle.sort((s1, s2) -> s1.compareTo(s2));
        int dp[][] = new int[target+1][2];
        
        // 초기화
        for(int i=1; i< target+1; i++){
            dp[i][0] = 1000000000;
            dp[i][1] = 0;
        }
        
        for(int i=0; i< target; i++){
            for(int s: single){
                if(i+s>target) break;
                if(dp[i+s][0]>dp[i][0]+1){
                    dp[i+s][0] = dp[i][0] + 1;
                    dp[i+s][1] = dp[i][1] + 1;
                }
                else if(dp[i+s][0] == dp[i][0] + 1 && dp[i+s][1] < dp[i][1]+1){
                    dp[i+s][0] = dp[i][0] + 1;
                    dp[i+s][1] = dp[i][1] + 1;
                }
            }
            
            for(int s: notSingle){
                if(i+s>target) break;
                if(dp[i+s][0]>dp[i][0]+1){
                    dp[i+s][0] = dp[i][0] + 1;
                    dp[i+s][1] = dp[i][1];
                }
                else if(dp[i+s][0] == dp[i][0] + 1 && dp[i+s][1] < dp[i][1]){
                    dp[i+s][0] = dp[i][0] + 1;
                    dp[i+s][1] = dp[i][1];
                }
            }
        }
        return dp[target];
    }
}