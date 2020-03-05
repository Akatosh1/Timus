class Main:
    def __init__(self, data):
        self.peaks = int(data[0])
        self.chains = 0
        self.visited = [False] * self.peaks
        self.in_chain = [False] * self.peaks
        self.dictionary = []
        self.components = []
        for i in range(1, self.peaks+1):
            self.dictionary.append([])
            for j in range(self.peaks):
                if int(data[i][j]):
                    self.dictionary[i-1].append(j)
                else:
                    pass

    def calculate(self):
        for i in range(self.peaks):
            if not self.visited[i]:
                self.find_chain(i)
                self.chains += 1
                self.components.append([])
                for i in range(self.peaks):
                    if self.visited[i] and not self.in_chain[i]:
                        self.components[self.chains-1].append(i+1)
                        self.in_chain[i] = True

    def find_chain(self, peak):
        self.visited[peak] = True
        for i in self.dictionary[peak]:
            if not self.visited[i]:
                self.find_chain(i)

if __name__ == "__main__":
    file = open("test1.txt", "r")
    data = file.read().split()
    main = Main(data)
    answer = main.calculate()
    answer = ""
    print(main.chains)
    for i in main.components:
        for j in i:
            answer += (str(j) + " ")
        print(answer + "0")
        answer = ""
