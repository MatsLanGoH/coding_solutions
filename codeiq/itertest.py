hey = dict()

hey = { 0: [2]}

print(hey)

hey.setdefault(0, []).append(1)
hey.setdefault(1, []).append(1)

print(hey)





H 1 2 8
V 4 1 6
H 1 7 5
V 7 7 2

H 2 / 1 2 3 4 5 6 7 8 (or for Y=2 all X between 1 and 8)
V X=4 all Y between 1 and 6.
   If there is a Y(H) that is bigger than 1 or smaller than 6, we might have a collision.
   If the Xvals for that Y(1..8) contain our Vx(=4), reduce total by one.
Just get the sum for now


    0  1  2  3  4  5  6  7  8  9 10
10
 9
 8
 7
 6
 5
 4
 3
 2
 1
 0


<n0 n1> <c0 c1> if n1 < c0
<c0 c1> <n0 n1> or if n0 > c1 => append, remove no tiles

<c0 <n0 n1> c1> if c0 < n0 and n1 < c1 => ignore (completely inside) and add all tiles to collision


<c0 <n0 == c1> == n1> add n1-c1 tiles to total, and update c1 to n1
<n0 == < c0 == n1> c1> add c0-n0 tiles to total, and update c0 to n0

<n0 <c0 c1> n1> if n0 < c0 and c1 < n1 => add c0-n0+n1-c0 tiles, then update c0=n0 and c1=n1
