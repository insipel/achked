# Randomized Quickselect: Worst-Case & Probability Analysis

## 1. What Happens to the Worst Case ($O(N^2)$)?

* Theoretically, the worst-case time complexity for Quickselect remains **$O(N^2)$**. This occurs if the random pivot selection accidentally picks the extreme minimum or maximum remaining element at every single partitioning step.
* However, with randomized pivot selection, encountering the worst case is **not dictated by the input structure**, but purely by random chance.
* The probability of picking such an extreme pivot repeatedly decreases exponentially with array size $N$. For any practical array size, this probability is negligible.

---

## 2. Worst-Case Probability & Napkin Math Analysis ($N = 100$)

### 2.1 The Probability Formula

When choosing pivots uniformly at random from the remaining sub-array, the probability of selecting an extreme element (either minimum or maximum) at every step for an array of size $N = 100$ is given by:

$$
P = \frac{2^{N-1}}{N!} = \frac{2^{99}}{100!}
$$

To find the order of magnitude ($10^x$), we take the base-10 logarithm ($\log_{10}$) of $P$:

$$
\log_{10}(P) = \log_{10}(2^{99}) - \log_{10}(100!)
$$

---

### 2.2 Step-by-Step Napkin Math Derivation

#### Step 1: Estimating the Numerator ($2^{99}$)
Using the standard computer science rule of thumb $2^{10} \approx 10^3$ (so $\log_{10}(2) \approx 0.3$):

$$
\log_{10}(2^{99}) = 99 \times \log_{10}(2) \approx 99 \times 0.3 = \mathbf{29.7}
$$

*(Thus, $2^{99} \approx 10^{29.7} \approx 5 \times 10^{29}$)*

#### Step 2: Estimating the Denominator ($100!$)
Using **Stirling's Approximation** for $\log_{10}(N!)$:
$$
\log_{10}(N!) \approx N \log_{10}(N) - N \log_{10}(e)
$$

Since $\log_{10}(e) \approx 0.434$:

$$
\log_{10}(100!) \approx 100 \log_{10}(100) - 100(0.434)
$$

$$
\log_{10}(100!) \approx 100(2) - 43.4 = 200 - 43.4 = \mathbf{156.6}
$$

*(Thus, $100! \approx 10^{156.6}$)*

#### Step 3: Combining Both Parts
Subtracting the exponent of the denominator from the numerator:

$$
\log_{10}(P) = \log_{10}(2^{99}) - \log_{10}(100!)
$$

$$
\log_{10}(P) \approx 29.7 - 156.6 = \mathbf{-126.9}
$$

$$
P \approx 10^{-127}
$$

---

### 2.3 Strict vs. Bi-directional Worst-Case Scenarios

* **Bi-directional Worst Case ($P \approx 10^{-127}$):** Allows picking *either* the minimum or maximum element at each step.
* **Strict One-Sided Worst Case ($P \approx 10^{-157}$):** Requires picking exclusively the maximum (or exclusively the minimum) element at every step:
  $$
  P = \frac{1}{100!} \approx \frac{1}{10^{157}} = \mathbf{10^{-157}}
  $$

---

### Key Takeaway
Whether the exact probability bound is **$10^{-127}$** or **$10^{-157}$**, napkin math demonstrates that the probability of hitting the worst-case runtime in randomized Quickselect is astronomically smaller than the number of atoms in the observable universe ($\approx 10^{80}$). This makes randomized Quickselect a universally optimal $O(N)$ expected-time algorithm in practice.