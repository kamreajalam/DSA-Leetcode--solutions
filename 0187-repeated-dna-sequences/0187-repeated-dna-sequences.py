class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        seen = set()
        repeated = set()

        for i in range(len(s)-9):

            dna = s[i:i+10]

            if dna in seen:

                repeated.add(dna)

            else:

                seen.add(dna)

        return list(repeated)

# T: 0(n-d), S: 0(n-d).d