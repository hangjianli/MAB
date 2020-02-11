def __init__(self, k=10, exp_rate=.3, lr=0.1, ucb=False, seed=None, c=2):
        self.k = k
        self.actions = range(self.k)
        self.exp_rate = exp_rate
        self.lr = lr
        self.total_reward = 0
        self.avg_reward = []

        self.TrueValue = []
        np.random.seed(seed)
        for i in range(self.k):
            self.TrueValue.append(np.random.randn() + 2)  # normal distribution
