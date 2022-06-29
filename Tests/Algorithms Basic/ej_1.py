'''
Road Repair
A number of points along the highway are in need of repair. An equal number of crews are available, stationed at various points along the highway. 
They must move along the highway to reach an assigned point. Given that one crew must be assigned to each job, what is the minimum total amount of 
distance traveled by all crews before they can begin work?

For example, given crews at points {1,3,5} and required repairs at {3,5,7}, one possible minimum assignment would be {1→ 3, 3 → 5, 5 → 7} for a
total of 6 units traveled.


Function Description

Complete the function getMinCost in the editor below. The function should return the minimum possible total distance traveled as an integer.
 
getMinCost has the following parameter(s):
    crewId[crewId[0],...crewId[n-1]] : a vector of integers
    jobId[jobId[0],...jobId[n-1]] : a vector of integers


Constraints

1 < n < 105
crewId[i] : 1 < crewId[i] < 109
jobId[i] : 1 < jobId[i] < 109

 
Input Format For Custom Testing

The first line contains an integer, n, denoting the number of elements in crew_id and job_id.
Each line i of the n subsequent lines (where 0 < i < n) contains an integer describing crew_id[i].
The next line again contains the integer n as above.
Each line i of the n subsequent lines (where 0 < i < n) contains an integer describing job_id[i].


Sample Case 0

Sample Input For Custom Testing
5
5
3
1
4
6
5
9
8
3
15
1
 

Sample Output
17

Explanation

By index, crewId[i] → jobId[i], { (0 → 0) , (1 → 2) , (2 → 4) , (3 → 3) , (4 → 1) } is one possible assignment for a minimum cost of 17. 
Showing element values, this is { (5 → 9) , (3 → 3) , (1 → 1) , (4 → 15) , (6 → 8) } yielding a total travel distance of 4 + 0 + 0 + 11 + 2 = 17.


Sample Case 1

Sample Input For Custom Testing
4
5
1
4
2
4
4
7
9
10

Sample Output
18

Explanation

By index, { (1 → 0) , (0 → 1) , (2 → 2) , (3 → 3) } is one possible assignment for a minimum cost of 18.
'''


def getMinCost(crew_id, job_id):
    n = len(crew_id)
    m = len(job_id)

    crew_id.sort()
    job_id.sort()

    cost = 0

    if n == m:
        for i in range(n):
            cost += abs(crew_id[i] - job_id[i])

    return cost


if __name__ == '__main__':
    crew_id = [5, 3, 1, 4, 6]
    job_id = [9, 8, 3, 15, 1]

    print(getMinCost(crew_id, job_id))
