# Import
import re
import Bio.SeqIO

# Function to get the k-mers from a list of sequences
def getKmers(k, D): 
	# Initialize an empty dictionary for the k-mers
	K = {}
	# Iterate through the data
	for d in D:
		# Go through the sequence 
		for i in range(0, len(d[1]) - k + 1, 1):
			# If the current k-mer contains only the characters A, C, G or T, it will be saved
			if bool(re.match('^[ACGT]+$', d[1][i:i + k])) == True: K[d[1][i:i + k]] = 0
	# Return the dictionary of k-mers
	return K

# Function to save the extracted k-mers
def saveExtractedKmers(K, solutions, path):
	# Iterate through the solutions
	for i, solution in enumerate(solutions):
		# Open a fasta file
		file = open(path + "/" + str(i + 1) + ".fasta", "w")
		# Save the k-mers of the actual solution
		[file.write(">solution_" + str(i + 1) + "_k_mer_" + str(j + 1) + "\n" + list(K.keys())[s] + "\n") for j, s in enumerate(solution)]
		# Close the fasta file
		file.close()

# Function to load the set of k-mers from a fasta file
def loadKmers(k_mers_path):
	# Initialize an empty dictionary for the k-mers
	K = {}
	# Iterate through the k-mers
	for record in Bio.SeqIO.parse(k_mers_path, "fasta"):
		# Save the current k-mer
		K[str(record.seq.upper())] = 0
	# Return the dictionary of k-mers
	return K
