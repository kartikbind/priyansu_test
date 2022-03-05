import sys


def minCost(N, K, X):
    diff = sys.maxsize
    if K == 2:
        for i in range(0,N):
            for j in range(0, N):
                if X[j] - X[i] <= 0:
                    pass
                else:
                    diff = min(diff, X[j] - X[i])
        return diff
    else:
        Y = []

        for i in range(0, N):
            cost = 0
            for j in range(0, N):
                if X[i] > X[j]:
                    cost = cost + X[i] - X[j]
                else:
                    cost = cost + X[j] - X[i]
            Y.append(cost)
        Y.sort()
        return Y[0]


def main():
    """N = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())
    X = []
    for i in range(N):
        X.append(int(sys.stdin.readline().strip()))"""
    N = 5
    K = 5
    X = [-2185, 2309, -5600, 2776, 2788]
    # N = 4
    # K = 2
    # X = [5851, -553, 704, -2652]
    # N = 5
    # K = 2
    # X = [5449, -2589, -1611, 8923, -5074]
    result = minCost(N, K, X)
    print(result)


if __name__ == "__main__":
    main()
