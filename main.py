import matplotlib.pyplot as plt
from bioinfokit.analys import fastq
from Bio.Blast import NCBIXML, NCBIWWW

fastqToAnalyze = "reads_for_analysis.fastq";

# Šaltinis: https://en.wikipedia.org/wiki/FASTQ_format#Encoding
encodingsDictionary = dict({
    'Sanger Phred+33': (33, 73),
    'Solexa Solexa+64': (59, 104),
    'Illumina 1.3+ Phred+64': (64, 104),
    'Illumina 1.5+ Phred+64': (67, 105),
    'Illumina 1.8+ Phred+33': (33, 74)
})

def blastSearch(seq):
    resultHandle = NCBIWWW.qblast("blastn", "nt", seq, alignments=1, hitlist_size=1)
    records = NCBIXML.parse(resultHandle)
    for rec in records:
        for alignment in rec.alignments:
            return alignment.hit_def

def bootstrap():
    fastqIterator = fastq.fastq_reader(file=fastqToAnalyze)

    qualityScoreConcatenation = ""
    gcRatios = []

    ids = []
    sequences = []

    for entry in fastqIterator:
        seqId, sequence, _, quality_score = entry
        qualityScoreConcatenation = qualityScoreConcatenation + quality_score
        gcRatios.append(round((sequence.count('G') + sequence.count('C')) / len(sequence), 2))
        ids.append(seqId)
        sequences.append(sequence)
    uniqueCharacters = set(qualityScoreConcatenation)

    for encoding in encodingsDictionary:
        charactersAreInEncodingRange = True
        for character in uniqueCharacters:
            if ord(character) < encodingsDictionary[encoding][0] or ord(character) > encodingsDictionary[encoding][1]:
                charactersAreInEncodingRange = False
        if charactersAreInEncodingRange:
            print(encoding)

    xAxis = []
    yAxis = []
    for i in range(0, 100):
        xAxis.append(i / 100)
    for x in xAxis:
        yAxis.append(gcRatios.count(x))
    plt.plot(xAxis, yAxis, color="black")
    plt.xlabel('C/G nukleotidai')
    plt.ylabel('Nuskaitymų kiekis')
    plt.show()

    peak1Ids = []
    peak1Seq = []
    peak2Ids = []
    peak2Seq = []
    peak3Ids = []
    peak3Seq = []
    peak1Pos = [j for j, x in enumerate(gcRatios) if x == 0.34][:5]
    peak2Pos = [j for j, x in enumerate(gcRatios) if x == 0.54][:5]
    peak3Pos = [j for j, x in enumerate(gcRatios) if x == 0.7][:5]
    for pos in peak1Pos:
        peak1Ids.append(ids[pos])
        peak1Seq.append(sequences[pos])
    for pos in peak2Pos:
        peak2Ids.append(ids[pos])
        peak2Seq.append(sequences[pos])
    for pos in peak3Pos:
        peak3Ids.append(ids[pos])
        peak3Seq.append(sequences[pos])
    print(peak1Seq)
    print(peak2Seq)
    print(peak3Seq)

    idsColumn = []
    bacteriaColumn = []
    for seqId in peak1Ids:
        idsColumn.append(seqId)
    for seqId in peak2Ids:
        idsColumn.append(seqId)
    for seqId in peak3Ids:
        idsColumn.append(seqId)

    for s in peak1Seq:
        bacteriaColumn.append(blastSearch(s))
    for s in peak2Seq:
        bacteriaColumn.append(blastSearch(s))
    for s in peak3Seq:
        bacteriaColumn.append(blastSearch(s))

    print(idsColumn)
    print(bacteriaColumn)

bootstrap()