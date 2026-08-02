# Randomized Quickselect: Worst-Case & Probability Analysis

## 1. What Happens to the Worst Case ($O(N^2)$)?

* [cite_start]Theoretically, the worst-case time complexity for Quickselect remains **$O(N^2)$**. This occurs if the random pivot selection accidentally picks the extreme minimum or maximum remaining element at every single partitioning step[cite: 1].
* [cite_start]However, with randomized pivot selection, encountering the worst case is **not dictated by the input structure**, but purely by random chance[cite: 1].
* The probability of picking such an extreme pivot repeatedly decreases exponentially with array size $N$. [cite_start]For any practical array size, this probability is negligible[cite: 1].

---

## 2. Worst-Case Probability & Napkin Math Analysis ($N = 100$)

### 2.1 The Probability Formula

When choosing pivots uniformly at random from the remaining sub-array, the probability of selecting an extreme element (either minimum or maximum) at every step for an array of size $N = 100$ is given by:

[cite_start]$$P = \frac{2^{N-1}}{N!} = \frac{2^{99}}{100!}$$ [cite: 1]

To find the order of magnitude ($10^x$), we take the base-10 logarithm ($\log_{10}$) of $P$:

[cite_start]$$\log_{10}(P) = \log_{10}(2^{99}) - \log_{10}(100!)$$ [cite: 1]

---

### 2.2 Step-by-Step Napkin Math Derivation

#### Step 1: Estimating the Numerator ($2^{99}$)
[cite_start]Using the standard computer science rule of thumb $2^{10} \approx 10^3$ (so $\log_{10}(2) \approx 0.3$)[cite: 1]:

[cite_start]$$\log_{10}(2^{99}) = 99 \times \log_{10}(2) \approx 99 \times 0.3 = \mathbf{29.7}$$ [cite: 1]

[cite_start]*(Thus, $2^{99} \approx 10^{29.7} \approx 5 \times 10^{29}$)* [cite: 1]

#### Step 2: Estimating the Denominator ($100!$)
[cite_start]Using **Stirling's Approximation** for $\log_{10}(N!)$[cite: 1]:
[cite_start]$$\log_{10}(N!) \approx N \log_{10}(N) - N \log_{10}(e)$$ [cite: 1]

[cite_start]Since $\log_{10}(e) \approx 0.434$[cite: 1]:

[cite_start]$$\log_{10}(100!) \approx 100 \log_{10}(100) - 100(0.434)$$ [cite: 1]
[cite_start]$$\log_{10}(100!) \approx 100(2) - 43.4 = 200 - 43.4 = \mathbf{156.6}$$ [cite: 1]

[cite_start]*(Thus, $100! \approx 10^{156.6}$)* [cite: 1]

#### Step 3: Combining Both Parts
Subtracting the exponent of the denominator from the numerator:

[cite_start]$$\log_{10}(P) = \log_{10}(2^{99}) - \log_{10}(100!)$$ [cite: 1]
[cite_start]$$\log_{10}(P) \approx 29.7 - 156.6 = \mathbf{-126.9}$$ [cite: 1]

[cite_start]$$P \approx 10^{-127}$$ [cite: 1]

---

### 2.3 Strict vs. Bi-directional Worst-Case Scenarios

* [cite_start]**Bi-directional Worst Case ($P \approx 10^{-127}$):** Allows picking *either* the minimum or maximum element at each step[cite: 1].
* [cite_start]**Strict One-Sided Worst Case ($P \approx 10^{-157}$):** Requires picking exclusively the maximum (or exclusively the minimum) element at every step[cite: 1]:
  [cite_start]$$P = \frac{1}{100!} \approx \frac{1}{10^{157}} = \mathbf{10^{-157}}$$ [cite: 1]

---

### Key Takeaway
[cite_start]Whether the exact probability bound is **$10^{-127}$** or **$10^{-157}$**, napkin math demonstrates that the probability of hitting the worst-case runtime in randomized Quickselect is astronomically smaller than the number of atoms in the observable universe ($\approx 10^{80}$)[cite: 1]. [cite_start]This makes randomized Quickselect a universally optimal $\mathcal{O}(N)$ expected-time algorithm in practice[cite: 1].