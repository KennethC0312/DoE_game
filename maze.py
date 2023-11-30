maze = [
        [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,0,1,1,0,1,1,0,0,3,1,1,1,1,1,1,0,0,0,0,1],
         [1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,0,1],
         [1,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1],
         [1,0,1,0,0,1,1,0,1,0,0,1,0,1,1,0,1,0,1,1,1],
         [1,0,0,1,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1],
         [1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1],
         [1,1,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,1],
         [1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1],
         [1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
         [1,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1],
         [1,1,3,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,1],
         [1,1,0,0,0,1,0,0,0,3,1,1,1,1,1,0,1,1,1,1,1],
         [1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1],
         [1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1],
         [1,1,1,1,0,0,0,2,1,0,0,1,1,0,0,1,1,0,0,1,1],
         [1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1],
         [1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1],
         [1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
        [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
         [1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,3,1,1,1],
         [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1],
         [1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1],
         [1,1,1,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1],
         [1,1,1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1],
         [1,1,1,1,0,1,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1],
         [1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1],
         [1,1,1,0,1,0,0,3,1,0,0,0,0,0,1,1,1,1,1,1,1],
         [1,1,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1],
         [1,1,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1],
         [1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1],
         [1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,3,1,0,1],
         [1,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,1,0,2,1,1],
         [1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
        [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
         [1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
         [1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,1,0,1,1],
         [1,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1],
         [1,1,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1],
         [1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,0,1,1,1,0,1],
         [1,2,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,1],
         [1,0,1,0,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1],
         [1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1],
         [1,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1],
         [1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1],
         [1,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1],
         [1,1,0,3,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,0,1],
         [1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1],
         [1,1,1,0,1,1,1,1,1,1,1,1,3,0,0,0,0,0,1,0,1],
         [1,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,0,0,0,1],
         [1,1,0,1,1,0,0,3,0,0,1,1,0,1,1,1,1,1,1,0,1],
         [1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,1,0,1],
         [1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1],
         [1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1],
         [1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
]
