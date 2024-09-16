# re-emit probability

labels: experimental

population based training thing

consider some particular node X_0 which transmits a message to its neighbor X_1. X_1 compares the signal against its local information to measure a "discrepancy" score. 
If the message surpasses some discrepancy threshold, X_1 re-broadcasts it to its neighbors. 
This behavior should be analogous to bees transmitting messages through their neighbors during "shimmering" colony defense. - https://journals.biologists.com/jeb/article/225/17/jeb244716/276503/Defensive-shimmering-responses-in-Apis-dorsata-are

once the threshold is surpassed, a "re-emit" probability parameter is referenced. This parameter should be a function of the discrepancy score and the message age. 
We want to amplify messages proportional to their discrepancy, and also we want to make sure we don't get caught in a chain reaction sending the same message 
back and forth repeatedly.

actually, with this re-emit probability, it could just be a continuous function of the discrepancy and then we don't even need to define a threshold. It'll be functionally 
given by the low-probability region of the re-emit probability distribution (over discrepancy).
