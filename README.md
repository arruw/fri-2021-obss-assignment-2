# OBSS Assignment 2 - Analysis of electromyogram of the uterus (EHG)
Estimating time course of peak frequency and median frequency along the spectrograms of uterine EMG records

Report is available [here](./report.pdf).

## Requirements
 - WFDB Software Package

## Tools
**Download the Term-Preterm EHG Database [1] and Sample Entropy Estimation Toolkit [3] from PhysioNet [3]**

```bash
$ cd data
$ wget -r -N -c -np https://physionet.org/files/tpehgdb/1.0.1/
$ wget -r -N -c -np wget -r -N -c -np https://physionet.org/files/sampen/1.0.0/
```

**Convert database to MATLAB format**
```bash
$ ./convert2mat.sh
```

## Literature
[1] [Gašper Fele-Žorž, Gorazd Kavšek, Živa Novak-Antolič and Franc Jager. A comparison of various linear and non-linear signal processing techniques to separate uterine EMG records of term and pre-term delivery groups. Medical & Biological Engineering & Computing, 46(9):911-922 (2008).](https://www.researchgate.net/profile/Franc_Jager/publication/5416350_A_comparison_of_various_linear_and_non-linear_signal_processing_techniques_to_separate_uterine_EMG_records_of_term_and_pre-term_delivery_groups/links/5459fdac0cf26d5090ad3cd6.pdf)

[2] [Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.](https://physionet.org/content/tpehgdb/1.0.1/)

[3] [Lake, D. E., J. S. Richman, M. P. Griffin, and J. R. Moorman. Sample entropy analysis of neonatal heart rate variability. Am J Physiol 2002; 283(3):R789-R797;](http://ajpregu.physiology.org/content/283/3/R789.abstract)
