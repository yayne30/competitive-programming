class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        number_seat=[0]*n
        for i in range(len(bookings)):
            number_seat[bookings[i][0]-1]+=bookings[i][2]
            if(bookings[i][1]<n):
                number_seat[bookings[i][1]]-=bookings[i][2]
        for j in range(1,n):
            number_seat[j]+=number_seat[j-1]
        return number_seat




        