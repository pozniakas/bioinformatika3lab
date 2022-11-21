# Bioinformatika 3 laboratorinis darbas

### Apibūdinkite fastq formatą. Kokia papildoma informacija pateikiam lyginant su FASTA formatu?

FASTQ yra tekstiniu pagrindu veikiantis formatas, kuris naudojamas saugoti sekai (paprastai - nukleotidų sekai) ir ją atitinkantiems kokybiniams įverčiams. 

Na, o papildomai šis formatas turi sekos identifikacinį numerį bei kokybės įverčius. Jie leidžia pavaizduoti kaip tiksliai buvo atrasta seka (šie duomenys pateikiami ASCII simboliais).

### Kurią mėnesio dieną Jūs gimėte? Prie dienos pridėkite 33. Koks ASCII simbolis atitinka šį skaičių?

Gimiau 23 dieną, tad gauname 23 + 33 = 56. Šis skaičius ASCII lentelėje atitinka '5' simbolį.

### Kodėl pirmi 32 ASCII kodai negali būti naudojami sekos kokybei koduoti?

Negali, nes jie yra naudojami kompiuterių ir yra rezervuoti. Pvz.: 2 ASCII skaičiaus simbolio negalim naudot, nes tai atitinka 'Teksto pradžios' simbolį, šis simbolis suprantamas tik kompiuteriams.

### Parašykite, kokią koduotę nustatėte ir kuo remiantis?

Rašant skriptą bei jo logiką, kur tikriname kokia koduotė yra naudojama, buvo naudojamasi šia lentele: 

<pre>  <span style="color: purple">SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS</span>.....................................................
  ..........................<span style="color: green">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</span>......................
  ...............................<span style="color: blue">IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII</span>......................
  .................................<span style="color: orange"><b>J</b>JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ</span>.....................
  <span style="color: brown">LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL</span>....................................................
  <span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPPPP</span><span style="color: red">PPPP</span>
 &nbsp;!"#$%&amp;'()*+,-./0123456789:;&lt;=&gt;?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
  |                         |    |        |                              |                     |
 33                        59   64       73                            104                   126
<span style="color: purple">  0........................26...31.......40                                </span>
<span style="color: green">                           -5....0........9.............................40 </span>
<span style="color: blue">                                 0........9.............................40 </span>
<span style="color: orange">                                    3.....9..............................41 </span>
<span style="color: brown">  0.2......................26...31........41                              </span>
<span style="color: red">  0..................20........30........40........50..........................................93</span>
</pre>

<pre> <span style="color: purple">S - Sanger        Phred+33,  raw reads typically (0, 40)</span>
 <span style="color: green">X - Solexa        Solexa+64, raw reads typically (-5, 40)</span>
 <span style="color: blue">I - Illumina 1.3+ Phred+64,  raw reads typically (0, 40)</span>
 <span style="color: orange">J - Illumina 1.5+ Phred+64,  raw reads typically (3, 41)
     with 0=unused, 1=unused, 2=Read Segment Quality Control Indicator (bold) 
     (Note: See discussion above).</span>
 <span style="color: brown">L - Illumina 1.8+ Phred+33,  raw reads typically (0, 41)</span>
 <span style="color: red">P - PacBio        Phred+33,  HiFi reads typically (0, 93)</span>
</pre>

Ir nustatėme, kad visi simboliai naudojami fastq faile yra iki 73-iojo simbolio, kas reišikia, kad galimi yra du variantai:

* Sanger Phred+33
* Illumina 1.8+ Phred+33

Tuomet rankiniu būdu patikrinau ar yra kažkur naudojamas 'J' simbolis, nes jis yra vienintelis, kuris galimas Illumina koduotėje, bet negalimas Sanger. Tokio simbolio nėra, tad galime teigti, kad naudojama yra Sanger Phred+33 koduotė.

### Pateikite grafiką, kurio y ašyje būtų read’ų skaičius, x ašyje - C/G nukletidų dalis read’o sekoje. Parašykite, koks „stambių“ pikų skaičius yra gautame grafike?

<img width="1439" alt="image" src="https://user-images.githubusercontent.com/50362698/202936984-2fac51dc-a794-4db7-bc6b-624139de7785.png">

„Stambių“ pikų skaičius yra 3:

* Kai C/G nukleotidų dalis buvo 0.34
* Kai C/G nukleotidų dalis buvo 0.54
* Kai C/G nukleotidų dalis buvo 0.70

### Pateikite lentelę, kurioje būtų read’o id ir rasto mikroorganizmo rūšis

<img width="1439" alt="image" src="https://user-images.githubusercontent.com/50362698/202937192-389e47d9-0933-4daf-9029-e20ecce6bb87.png">


### Kokių rūšių bakterijų buvo mėginyje?

Escherichia coli, Thermus thermophilus, Staphylococcus aureus
