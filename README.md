# pylift

![](https://github.com/df-foundation/pylift/raw/master/docs/img/pylift_logo.png?raw=true)

[![GitHub version](https://badge.fury.io/gh/pylift%2Fpylift.svg)](https://badge.fury.io/gh/pylift%2Fpylift)

[Read our documentation!](https://pylift.readthedocs.io/en/latest/)

**pylift** is an uplift library that provides, primarily:

1. Fast uplift modeling implementations. 
2. Evaluation tools \(`UpliftEval` class\).

While other packages and more exact methods exist to model uplift, **pylift** is designed to be quick, flexible, and effective. **pylift** heavily leverages the optimizations of other packages -- namely, `xgboost`, `sklearn`, `pandas`, `matplotlib`, `numpy`, and `scipy`. The primary method currently implemented is the Transformed Outcome proxy method \(Athey 2015\).

This branch is a fork from [github.com/wayfair/pylift](https://github.com/wayfair/pylift), and is actively being maintained.

## Installation

The latest version of pylift can be installed through pypi:

```text
pip install pylift
```

## License

Licensed under the BSD-2-Clause by the authors.

## Reference

Yi, R. & Frost, W. \(2018\). [Pylift: A Fast Python Package for Uplift Modeling](https://tech.wayfair.com/data-science/2018/10/pylift-a-fast-python-package-for-uplift-modeling/). Wayfair Tech Blog.

Athey, S., & Imbens, G. W. \(2015\). Machine learning methods for estimating heterogeneous causal effects. stat, 1050\(5\).

Gutierrez, P., & Gérardy, J. Y. \(2017\). Causal Inference and Uplift Modelling: A Review of the Literature. In International Conference on Predictive Applications and APIs \(pp. 1-13\).

Hitsch, G., & Misra, S. \(2018\). Heterogeneous Treatment Effects and Optimal Targeting Policy Evaluation. Preprint

