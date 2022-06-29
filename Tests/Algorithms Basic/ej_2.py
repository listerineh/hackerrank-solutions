'''
Algorithms/Data Structures
An Institutional Broker wants to Review their Book of Customers to see which are Most Active. Given a List of Trades By "Customer Name, 
Determine which Customers Account for At Least 5% of the Total Number of Trades. Order the List Alphabetically Ascending By Name."


Example
n = 23
"customers = {"Bigcorp", "Bigcorp", "Acme", "Bigcorp", "Zork", "Zork", "Abe", "Bigcorp", "Acme", "Bigcorp", "Bigcorp", "Zork", "Bigcorp", 
"Zork", "Zork", "Bigcorp", "Acme", "Bigcorp", "Acme", "Bigcorp", "Acme", "Littlecorp", "Nadircorp"}."

"Bigcorp had 10 Trades out of 23, which is 43.48% of the Total Trades."
"Both Acme and Zork had 5 trades, which is 21.74% of the Total Trades."
"The Littlecorp, Nadircorp, and Abe had 1 Trade Each, which is 4.35%..."
"So the Answer is ["Acme","Bigcorp","Zork"] (In Alphabetical Order) Because only These Three Companies Placed at least 5% of the Trades.


Function Description
Complete the Function mostActive in the Editor Below.

mostActive has the following parameter:
String customers[n]: An Array Customer Names
(Actual Question Says String Array, But Signature is List of Strings)

Returns String[]: An Alphabetically Ascending Array


Constraints
1 < n < 10^5
1 < Length of customers[] < 20
The First Character of customers[i] is a Capital English letter.
All Characters of customers[i] except for the First One are Lowercase.
Guaranteed that At least One Customer makes at least 5% of Trades.


Input Format
"The First Line contains an integer, n, The Number of Elements in customers."
"Each Line i of the n Subsequent Lines (where 0 s i< n) contains a string, customers[i]."


Sample Case 0 Input For Custom Testing
20
Omega Alpha Omega Alpha Omega Alpha Omega Alpha Omega Alpha Omega Alpha Omega Alpha Omega Alpha Omega Alpha Omega Beta


Function mostActive       
customers[] size n = 20
customers[] = [As Provided Above]


Sample Output
Alpha
Beta
Omega


Explanation
Alpha made 10 Trades out of 20 (50% of the Total), Omega made 9 Trades (45% of the Total). and Beta made 1 Trade (5% of the Total). All of them 
have met the 5% Threshold, so all the Strings are Returned in an Alphabetically Ordered Array."
'''


def mostActive(customers):
    appeared = [] 
    counting = []
    percents = []

    total = len(customers)

    for customer in customers:
        if not customer in appeared:
            appeared.append(customer)

    for customer in appeared:
        count = 0
        for item in customers:
            if customer == item:
                count += 1
        counting.append(count)

    for customer in counting:
        percents.append(customer*100/total)

    to_delete = []
    final = []

    for i in range(len(percents)):
        if percents[i] < 5:
            to_delete.append(i)

    for j in range(len(appeared)):
        if not j in to_delete:
            final.append(appeared[j])

    final.sort()

    return final


if __name__ == '__main__':
    list = ["Alpha",
            "Beta",
            "Zeta",
            "Beta",
            "Zeta",
            "Zeta",
            "Epsilon",
            "Beta",
            "Zeta",
            "Beta",
            "Zeta",
            "Beta",
            "Delta",
            "Zeta",
            "Beta",
            "Zeta",
            "Beta",
            "Zeta",
            "Beta",
            "Zeta",
            "Beta"]
    print(mostActive(list))
