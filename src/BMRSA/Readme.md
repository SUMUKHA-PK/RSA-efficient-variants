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
 and E = E<sub>L</sub>*E<sub>R</sub>
 
 ### 4. Exponentiation
* Calculate C<sub>p<sub>i</sub></sub> by the C<sub>p<sub>i</sub></sub> = V mod(P<sub>i</sub>)

* Compute M<sub>p<sub>i</sub></sub> by the M<sub>p<sub>i</sub></sub> =C<sub>p<sub>i</sub></sub><sup>d<sub>p<sub>i</sub></sub></sup>mod(P<sub>i</sub>)

* Compute y<sub>p</sub> = N / P<sub>i</sub> = P<sub>1</sub>P<sub>2</sub>....P<sub>b</sub> and
n<sub>i</sub> = y<sub>i</sub> * y<sub>i</sub><sup>-1</sup> (mod P<sub>i</sub>)

* Using the CRT to combine the M<sub>i</sub> 's to obtain
r = V<sup>d</sup> = M<sub>p<sub>l</sub></sub>*n<sub>1</sub> + .... + M<sub>p<sub>b</sub></sub>*n<sub>b</sub> (mod N)


### 5. Percolate Down
* Use r as the root of the tree

* Find t = 0 mod E<sub>L</sub> and t = 1 mod E<sub>R</sub>.<br />
  t<sub>L</sub> = t / E<sub>L</sub> and  t<sub>R</sub> = (t-1)/<sub>R</sub><br />
  Find r<sub>R</sub> = r<sup>t</sup>/(V<sub>L</sub><sup>t<sub>L</sub></sup>*V<sub>R</sub><sup>t<sub>R</sub></sup>) and 
  r<sub>L</sub> = r / r<sub>R</sub>
  
* What is present in the leaves will be messages

***

## File structure
* main.py : driver function
* mainBMRSA : here is where BMRSA is implemented
* mainBRSA : here is where BRSA is implemented
* useful/ funcs : useful functions like CRT, MMI are implemented here

***

## Results

* BMRSA is faster than BRSA which is evident from the graph below. <br />
The reason is due to *exponentiation step and tree making* which reduces the time needed for exponentiation

<b>Batch size is 1</b>
![](1.PNG)


<b>Batch size is 2</b>
![](2.PNG)

<b>Batch size is 3</b>
![](3.PNG)