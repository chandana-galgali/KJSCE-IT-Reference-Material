class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    def _lsb(self, i):
        return i & -i
    def update(self, i, delta):
        i += 1  
        while i <= self.size:
            self.tree[i] += delta
            i += self._lsb(i)
    def prefix_sum(self, i):
        i += 1  
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= self._lsb(i)
        return result
    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    fenwick_tree = FenwickTree(len(arr))
    for i, val in enumerate(arr):
        fenwick_tree.update(i, val)
    q = int(input("Enter number of queries: "))
    for _ in range(q):
        query_type = input("Enter query type (sum/update): ").lower()
        if query_type == "update":
            idx, value = map(int, input("Enter index and value separated by space: ").split())
            fenwick_tree.update(idx, value - arr[idx])
            arr[idx] = value
        elif query_type == "sum":
            left, right = map(int, input("Enter left and right indices for sum query (separated by hyphen): ").split("-"))
            print(f"Sum of range [{left}, {right}]: {fenwick_tree.range_sum(left, right)}")
        else:
            print("Invalid query type. Please enter 'sum' or 'update'.")