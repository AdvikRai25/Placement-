class Solution(object):
    def maximumTime(self, time):
        time = list(time)


        if time[0] == '?':
            if time[1] == '?' or time[1] <= '3':
                time[0] = '2'
            else:
                time[0] = '1'


        if time[1] == '?':
            if time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'


        if time[3] == '?':
            time[3] = '5'


        if time[4] == '?':
            time[4] = '9'

        return ''.join(time) 

if __name__ == "__main__":
    s = Solution()
    print(s.maximumTime("2?:?0"))  # Output: "23:50"
    print(s.maximumTime("0?:3?"))  # Output: "09:39"
    print(s.maximumTime("1?:22"))  # Output: "19:22"
    print(s.maximumTime("??:??"))  # Output: "23:59"
