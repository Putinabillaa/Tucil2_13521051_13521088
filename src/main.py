import time
import Helper
import ClosestPoint_BruteForce
import ClosestPoint_DnQ

def main(): 
    Quit = False
    Helper.SplashScreen()
    while(not Quit):
        # Input
        # Input banyaknya dimensi
        nDim = int(input("Enter dimensions: "))
        while(nDim < 2):
            print("Dimensions must larger than 1")
            nDim = int(input("Enter dimensions: "))

        # set range koordinat titik
        if(nDim == 2 or nDim == 3): 
            maxRange = 1000000.00
            minRange = -1000000.00
        else:
            maxRange = 1000.00
            minRange = -1000.00
        
        # Input banyaknya titik
        n = int(input("Enter number of points: "))
        while(n < 2):
            print("Number of points must larger than 1")
            n = int(input("Enter number of points: "))
        # Menu input koordinat titik
        print("How do you want to input the points' coordinates?")
        print("1. Randomize")
        print("2. Input File")
        choice = input(">>> ")
        while(choice != '1' and choice != '2'):
            print("You've inputed wrong choice, please choose 1 or 2!")
            choice = input(">>> ")

        # Pemanggilan method randomizer
        if(choice == '1'):
            points = Helper.ListRandomizer(nDim, n, maxRange, minRange)

        # Pemanggilan method read file
        else:
            points = Helper.ReadFile(nDim, n, maxRange, minRange)
            while (points == -1):
                points = Helper.ReadFile(nDim, n, maxRange, minRange)

        # Pemanggilan method bruteforce
        start_time = time.process_time()
        BF_minDist, BF_pair, BF_totalOps = ClosestPoint_BruteForce.ClosestPoint_Bf(nDim, points)
        BF_execTime = '%.5f'%(time.process_time() - start_time)
        # Pemangginan method DnC
        sorted_points= Helper.sortAxis(points, 0)
        start_time = time.process_time()
        DnC_minDist, DnC_pair, DnC_totalOps = ClosestPoint_DnQ.closestPair(nDim, sorted_points, n, 0)
        DnC_execTime = '%.5f'%(time.process_time() - start_time)
        # Pemanggilan method visualiser & Output
        print("The Minimum Distance is: " + str(DnC_minDist) + str(BF_minDist))
        print("Between points: ")
        for x in DnC_pair:
            print(x[0])
            print(x[1])
            print('\n')
        if(nDim == 3):
            print("Pair(s) of closest points indicated by different color")
            Helper.Visualizer3D(n, points,  DnC_pair)
        elif(nDim == 2):
            print("Pair(s) of closest points indicated by different color")
            Helper.Visualizer2D(n, points,  DnC_pair)      
        tableHead = ["No", "Metrics", "Brute Force", "Divide and Conquer"]
        print('---------------------------------------------------------------------------------')
        print('| {:2} | {:^26} | {:^20} | {:^20} |'.format(*tableHead))
        print('---------------------------------------------------------------------------------')
        table = [["1.", "Execution Time", str(BF_execTime) + " sec", str(DnC_execTime) + " sec"], ["2.", "Total Euclidean Operations", BF_totalOps, DnC_totalOps]]
        for row in table:
            print('| {:2} | {:<26} | {:^20} | {:^20} |'.format(*row))
        print('---------------------------------------------------------------------------------')
        print("Do you want to do another calculation? (y/n)")
        choice = input(">>> ")
        while(choice != 'y' and choice != 'n'):
            print("You've inputed wrong choice, please choose y or n!")
            choice = input(">>> ")
        if(choice == 'n'): Quit = True

main()