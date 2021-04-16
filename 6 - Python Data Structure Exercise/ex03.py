# Given a list slice it into 3 equal chunks and reverse each chunk
# sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Solution: https://github.com/JhonesBR

def divChunks(L):
    chunkSize = int(len(L)/3)
    for i in range(0, len(L), chunkSize):
        chunk = []
        for j in range(chunkSize):
            chunk.append(L[i+j])
        print(f"Original chunk: {chunk}")
        print(f"Reversed chunk: {chunk[::-1]}\n")


sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
divChunks(sampleList)