Usage: EDA
===============

Once a ``TransformedOutcome()`` object has been instantiated, **pylift** offers a couple methods for simple feature EDA: ``up.NIV()`` (Net Information Value) and ``up.NWOE()`` (Net Weight of Evidence). See `Data Exploration with Weight of Evidence and Information Value in R <https://multithreaded.stitchfix.com/blog/2015/08/13/weight-of-evidence/>`_ for more details.

Net Weight of Evidence
----------------------
*Weight of Evidence* comes from a simple Bayesian decomposition of lift as a function of features:

.. math:: \log \frac{P(Y = 1|X_j}{P(Y = 0|X_j} = \log \frac{P(Y=1)}{P(Y=0)} + \underbrace{\log \frac{P(X_j | Y=1)}{P(X_j | Y =0)}}_{\text{Weight of Evidence}}

Net Weight of Evidence (NWOE) is the difference in Weight of Evidence (WOE) between the treatment and control groups.

.. math:: \text{NWOE} = \text{WOE}_t - \text{WOE}_c

Where Weight of Evidence is defined as:

.. math:: \text{WOE_{ij} = \log \frac{P(X_j \subset B_i | Y = 1}{P(X_j \subset B_i | Y = 0}

where :math:`B_i` indicates a bin :math:`i`, and the subscript :math:`j` indicates a particular feature.

This can be accessed in **pylift** as follows:

::

    up = TransformedOutcome(df)
    up.NWOE()

``up.NWOE()`` can take two arguments: ``n_bins`` (the number of bins) and ``feats_to_use`` (a subset of features over which to calculate NWOE).

The base routine can be accessed from the ``pylift.explore`` module (``from pylift.explore.base import _NWOE``).

Net Information Value
---------------------
*Information Value* is the sum of all WOE values, weighted by the absolute difference in the numerator and denominator.

.. math:: \text{IV}_j = \int \log \frac{P(X_j | Y = 1)}{P(X_j | Y=0)} (P(X_j | Y = 1) - P(X_j | Y = 0)) \ dx

For the *net* weight of evidence, the numerator and denominator can be rewritten as:

.. math:: \text{NWOE_j} = \log \frac{P(x_j | Y = 1, W = 1) P(x_j | Y = 0, W= 0)}{P(x_j | Y =1, W=0) P(x_j | Y = 0, W = 1)}

Net information value, then, sums the NWOE values, weighted by the difference between the above numerator and denominator.

This can be accessed in **pylift** as follows:

::

   up = TransformedOutcome(df)
   up.NIV()

``up.NIV()`` accepts ``feats_to_use`` and ``n_bins``, as it requires NWOE to be calculated as a pre-requisite. But ``up.NIV()`` also accepts ``n_iter`` -- ``up.NIV()`` will bootstrap the training set to obtain error bars, and ``n_iter`` specifies the number of iterations to use.

The base routine can be accessed from the ``pylift.explore`` module (``from pylift.explore.base import _NIV``).

