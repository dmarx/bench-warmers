# Spectral Scheduling

labels: experimental

1. learn a singular basis over the data
2. treat the eigenvalues as relative sampling weight, sample a basis dimension/component each batch
3. sample a batch of data, using that datum's value in the sampled component as their relative likelihood (threshold this)
4. incorporate a temperature term so we can sample disproportionately from the important components in early training, progressively increasing the weight of the tail probabilities.

can we learn this online?
