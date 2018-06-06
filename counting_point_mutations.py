dnaOne = "CGCTGCAATGCAAGTTAACGGAACTGGGCTGGTAGCGGAATCGAGTCTACAAACACCTTCAAGCAAGGACCTATTGTATCGGCTTAAGTGGGACCCGAAATAATAGTCGTCCATGTGGTGTAAGATATGCTGCATGAGCTAGTTCCATCCCTTTATAGCAGTTCCCTAACTATAGTAGGTGTTCTGCGTGTGGTGCCTTATGACAAACGCCATGAAAGCTCCTGTGTGCACATCCTACCCCACTGTGCCCTAAGTAGATATGGTGATCGTAATTATCGATCATCCCCGCCGGGGCACAGTACGCAGCGTCAGCCACAATTCATGTCAACGCTATGGCGTTCGGGGGACAAAGTACTTAGGTAGAATAAATGTTAACGCGTTCCGTCTGACGAGGATAATCTGGACGCCGACAAGTATGTCCCGAGGGCCACATTCACTGAAAGCTTGTTCTAGATGTGGCCGCCCGCGTTTAGCGTCGGACGCTGACCAACGCCTAGTGGATGTGGGAGCTGTGCCAAGTTGGCTTATTTTGCCAATCAGACCCCTGATAGCCGATCAACCGGGGAGTGATGTACTACTTAGCGGTATCTTAGAAGCACACCATCTACCAAATACGGCGATGGGTATATGCTACTATTATGTGTGGCGAATCACTCACTACCAGGAACAGCTTAAATCTACACGATGATATGTTGGAGACAGCCGGCGCGTTGGCTAGCTCCTGTCACTACCGACGAGATGTGCGCATATTTTAACTCCGCGGTTGTCCAAGGTTGAAGTCACTAGCTCACAGTGTAGCTGCATGACACACGATGCTCTCCCCGTTCCAAGGCTTGAAGCGATCCTTGCCTCCTTAATGTCCTAGGCCGCCTTTCTTTGGAGTCGGACGGTTCAGACCTCCTCACGCTGGCCAAGTTCCGAGCCCTACTGTGTTGGAACCGGAACGCTAATGTTCTGCTGT"
dnaTwo = "CCCGGCCGCCTAAGTTACAGGCCCATGGAGAACTCCGTAGTTGACTATATAACGTGGCTCAATCAAAAAAACACTGTATGTGGTTAATGTACGCGTGATTTAGTCGTCGTGAATGTAAGTTAAAAGTTCTGGCTTAAGCCTGACCCCGGCCTGCATACCCACACCGTAAGCTTGTTTACTTTTCTGTGTGGTGTACATCTTCCGCCAGCGCATTCAACCACCCGTTCTCACAGACTAATGGACGGCACCAAGGCGATTTATACTTCCACAGATCCTGTAGGAGCCGCGTCTTCCCACATTCTGCCCCGACCTGGATCGGGTAAATAAGCTCAATGGCTTTAGCCTCTCCAATTACTCGCGCAGTATTAGTGCTAGAGCGGTCGGGAGTCATCATAAGACATGGTCACCCTCCTCTACGATCCGGGGACATCTTTCTATTGAGGCTTGTCCTGCAGGTGTGATCCAGCGATGGGGCGCGAAACATGGGCAAGGGCTGTGCCAGTTGGGAGCGGGCTGTGAAGGTTGGGTTTTGCTAAACACCCCCCAGATAGTGTCGCAGCAGGGCAGTGAGGTTGAAGTTAGAGATACTTTAGAAGTGCATTCTTTTCTACCAACGACAAAAGAGGGATGAACGTATTGGCAAATCTGAAGGTCAAGCCTGTCGAACCTAAGCATCTTCTTCACTGGATTTCTTCGAGATCGCCAGTTCGTTGCTTTGAGCCAGCCTCGTCCACAAAGACATGTGAATGGTTTCAAATGGTGTTTTTCCAATGTGGAACTCCACAGTCGAACGGGTCGTTTCGTAACCTGGTCCGATCAGTGCGCTACGATGCTTATGGTGGCTCTAGCCTCCTAAAATACATAAGTGCTCATTCGTTTAGATCGATCTCCTCATACTAGTACGAGGAAGCGCGGTTCAGATCCCCATACAGGAGAAAAAACAACTGTTCAATCGTGCTCT"
mutCount = count = sum(1 for a, b in zip(dnaOne, dnaTwo) if a != b)
print(mutCount)