import java.util.*
fun find(parent: IntArray, x: Int): Int {
    if (parent[x] == x) return x
    parent[x] = find(parent, parent[x])
    return parent[x]
}
fun union(parent: IntArray, a: Int, b: Int): Boolean {
    // a,b를 정렬한다.
    if (a > b) return union(parent, b, a)
    val rootA = find(parent, a)
    val rootB = find(parent, b)
    if (rootA == rootB) return false
    // 무조건 더 작은쪽이 부모가 된다.
    if (rootA < rootB) parent[rootB] = rootA
    else parent[rootA] = rootB
    return true
}
fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val n = br.readLine().toInt()
    val visited = BooleanArray(n)
    val pq = PriorityQueue<List<Int>>(compareBy { it[0] })
    val parent = IntArray(n) { it }

    fun string2IntArray(str: String): IntArray {
        val intArray = IntArray(str.length)
        for (i in str.indices) {
            intArray[i] = when{
                (str[i] in 'a'..'z') -> str[i].code - 96
                (str[i] in 'A'..'Z') -> str[i].code - 38
                else -> 0
            }
        }
        return intArray
    }

    val rooms = mutableListOf<IntArray>()
    for(i in 1..n){
        val room = br.readLine()
        val roomArray = string2IntArray(room)
        rooms.add(roomArray)
    }
    var ans = (0 until n).sumOf {
        rooms[it][it]
    }
    if (n== 1) {
        print(ans)
        return
    }


    (0 until n).flatMap{
        i -> (0 until n).map{
            j -> if(i != j && rooms[i][j] > 0) listOf(rooms[i][j], i, j) else null
        }
    }.filterNotNull().forEach{pq.add(it)}

    while(pq.isNotEmpty()){
        val (cost, start, end) = pq.poll()
        if(union(parent, start, end)){
            visited[start] = true
            visited[end] = true
        }else{
            ans += cost
        }
    }
    (0 until n).forEach{
        find(parent, it)
    }
    print(if(parent.all{it == 0}) ans else -1)
}
