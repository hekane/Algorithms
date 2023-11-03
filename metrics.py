
class statistics:
    def __init__(self, swaps, comparisons):
        self.swaps=swaps
        self.comparisons=comparisons
    def print_mertrics(self):
        print("Total operations:",self.swaps, self.comparisons)
        print("Swaps:",self.swaps)
        print("Comparisons:",self.comparisons)