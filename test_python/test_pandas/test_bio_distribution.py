# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


def test():
    n = 10
    p = 0.3
    k = np.arange(0, 21)
    bio = stats.binom.pmf(k, n, p)
    plt.plot(k, bio, 'o-')
    plt.title('Bio: n={}, p={}'.format(n, p), fontsize=15)
    plt.xlabel('Nums of successes')
    plt.ylabel('prob of successes', fontsize=15)
    plt.show()

if __name__ == '__main__':
    test()
