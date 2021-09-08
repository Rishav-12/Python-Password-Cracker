import hashlib

# generator function to read each password in our wordlist
def file_reader(filename):
	for row in open(filename, 'r'):
		yield row

# function to convert text to a SHA256 hash
def text_to_sha256(text):
	sha256_hashed_text = hashlib.sha256(text.encode()).hexdigest()
	return sha256_hashed_text

def main():
	target_sha256 = input("Enter the SHA256 hash to crack: ").strip().lower()
	passwords_file = input("Enter the wordlist to look in: ")

	reader = file_reader(passwords_file)

	while True:
		try:
			# obtain the next password from the wordlist by calling next() on the file_reader object
			cleaned_password = next(reader).strip()
			password_sha256 = text_to_sha256(cleaned_password)

			# if the SHA256 hash of our current password matches the hash we are looking to crack
			# we have found the password!
			if password_sha256 == target_sha256:
				print("Password found")
				print(f"Password: {cleaned_password}")
				return
		# if there the no more passwords in the wordlist, the generator object raises StopIteration
		# and we stop the script and tell the user that the hash was not found in the provided wordlist
		except StopIteration:
			break
	print("Password not found in given file")

if __name__ == '__main__':
	main()
