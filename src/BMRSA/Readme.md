# The Batch Multi Prime RSA

***

## Algorithm

### 1. Set Up

* Compute b distinct primes P<sub>1</sub>....P<sub>b</sub> which are (n/b) bits long

* Calculate phi and N. <br />
phi = (P<sub>1</sub> - 1)*...(P<sub>b</sub> - 1) <br />
N = P<sub>1</sub>*...P<sub>b</sub>

* Taken l distinct and pairwise relatively prime public
keys e<sub>1</sub>,....,e<sub>l</sub> as input. For each ei get di = ei<sup>-1</sup>mod(N).<br /> 
Computed = d<sub>1</sub>....d<sub>l</sub>mod(N)


### 2. Encryption
* For each message mi compute v<sub>i</sub> = m<sub>i</sub><sup>e<sub>i</sub></sup> mod(N).


### 3. Percolate Up
* Create a tree with leaves (V, E), where V = v<sub>i</sub> and E = e<sub>i</sub> and pass upwards.
* V = V<sub>R</sub><sup>E<sub>L</sub></sup> * V<sub>L</sub><sup>E<sub>R</sub></sup>
 and E = 