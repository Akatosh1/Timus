class Main():
    def __init__(self, data):
        self.peaks = int(data[0])
        self.merge_list = []
        self.half_one = [1]
        self.half_two = []
        counter = 0
        self.current_peak = 1
        self.previous_peak = 1
        self.merge_list.append([])
        for i in range(1, len(data)):
            if int(data[i]):
                self.merge_list[counter].append(int(data[i]))
            elif i == len(data)-1:
                pass
            else:
                counter += 1
                self.merge_list.append([])

    def calculate(self):
        visited = []
        queue = [1]
        is_finding = True
        while (len(visited) < self.peaks) and is_finding:
            current_peak = queue[0]
            merge = self.merge_list[current_peak-1]
            for peak in merge:
                if (peak not in self.half_one and peak not in self.half_two):
                    if current_peak in self.half_one:
                        self.half_two.append(peak)
                    else:
                        self.half_one.append(peak)
                if current_peak in self.half_one and peak in self.half_one:
                    print("No")
                    is_finding = False
                if current_peak in self.half_two and peak in self.half_two:
                    print("No")
                    is_finding = False
                    break
                if peak not in visited and peak not in queue:
                    queue.append(peak)
            queue.pop(0)
            visited.append(current_peak)
        if (len(self.half_two) + len(self.half_one)) == self.peaks:
            print("Yes")
            print(sorted(self.half_one))
            print(sorted(self.half_two))

if __name__ == "__main__":
    file = open("test2.txt", "r")
    data = file.read().split()
    main = Main(data)
    main.calculate()
