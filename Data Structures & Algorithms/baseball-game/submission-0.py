class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []
        result = 0 

        for x in range(len(operations)):
            if operations[x] == '+':
                record.append(int(record[-1]) + int(record[-2]))

            elif operations[x] == 'D':
                record.append(int(record[-1])*2)

            elif operations[x] == 'C':
                record.pop()

            else:
                record.append(operations[x])

        for x in range(len(record)):
            result += int(record[x])

        return result 
            