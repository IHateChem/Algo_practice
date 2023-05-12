# 이 개같은문제 왜자꾸 출력형식뜨죠 ㄴㅁㅅㅈ4ㄷㄴ우허ㅑㅁ
#출력오류는.. 프린트 어디따가 하나 더하신거아닌지
# ㄴ
# 채점현황 봐보셈ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
#ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
#도배를하네
# 화난다진짜... 여기 4시간갖다부음
#흠
# 9205 풀러갑니다
def solution(text):

  n=len(text)
  mid,rmid=n//2,(n+1)//2
  if n==1: 
      print(text)
      return

  sorted_text=sorted(text)
  ans=[""]*n
  if n%2==1: 
      ans[n//2]=sorted_text[n//2]

  i,j=mid-1,rmid

  while i>=0 and sorted_text[i]==sorted_text[mid]: 
      i-=1
  while j<n and sorted_text[j]==sorted_text[mid]: 
      j+=1
  i+=1
  j-=1

  i_moved,j_moved=mid-i,j-rmid+1
  for k in range(i_moved):
      j+=1
      if j>=n: 
        print(-1)
        return
      ans[rmid+k]=sorted_text[j]

  j=rmid+i_moved
  for k in range(j_moved):
      if j>=n: 
        print(-1)
        return
      ans[j]=sorted_text[rmid+k]
      j+=1

  for i in range(mid):
      ans[i]=sorted_text[i]

  while j<n:
      ans[j]=sorted_text[j]
      j+=1

  print("".join(ans))

text=input()
solution(text)