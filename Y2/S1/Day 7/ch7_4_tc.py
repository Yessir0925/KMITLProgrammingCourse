"""
Enter Input : i 3,i 5,i 2,d 3
insert 3
 3
insert 5
      5
 3
insert 2
      5
 3
      2
delete 3
 5
      2

Enter Input : d 1,i 1,d 1,i 0,i 2,i 4,i 1,i 5,i 3,d 2
delete 1
Error! Not Found DATA
insert 1
 1
delete 1
insert 0
 0
insert 2
      2
 0
insert 4
           4
      2
 0
insert 1
           4
      2
           1
 0
insert 5
                5
           4
      2
           1
 0
insert 3
                5
           4
                3
      2
           1
 0
delete 2
                5
           4
      3
           1
 0

Enter Input : i 8,i 7,d 1,i 3,i 1,i 2,i 6,i 9,d 8,d 9,d 7,d 1,d 6,d 3,d 2
insert 8
 8
insert 7
 8
      7
delete 1
Error! Not Found DATA
 8
      7
insert 3
 8
      7
           3
insert 1
 8
      7
           3
                1
insert 2
 8
      7
           3
                     2
                1
insert 6
 8
      7
                6
           3
                     2
                1
insert 9
      9
 8
      7
                6
           3
                     2
                1
delete 8
 9
      7
                6
           3
                     2
                1
delete 9
 7
           6
      3
                2
           1
delete 7
      6
 3
           2
      1
delete 1
      6
 3
      2
delete 6
 3
      2
delete 3
 2
delete 2

"""