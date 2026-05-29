class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed= zip(*sorted(zip(position, speed)))
        speed = list(speed)
        position = list(position) 

        time_to_dest = [(target-position[i])/speed[i] for i in range(len(position))]
        print(speed, position, time_to_dest)

        num_of_fleets = 0
        i = len(time_to_dest)-1
        while i >= 0:
            curr_car = i-1
            num_of_fleets+=1
            while curr_car >= 0 and time_to_dest[i] >= time_to_dest[curr_car]:
                curr_car-=1
            i = curr_car
                

        return num_of_fleets 
            
        
        
        