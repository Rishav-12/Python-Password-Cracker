import hashlib

def file_reader(filename):
	for row in open(filename, 'r'):
		yield row

def text_to_sha256(text):
	sha256_hashed_text = hashlib.sha256(text.encode()).hexdigest()
	return sha256_hashed_text

def main():
	target_sha256 = input("Enter the SHA256 hash to crack: ").strip().lower()
	passwords_file = input("Enter the wordlist to look in: ")

	reader = file_reader(passwords_file)

	while True:
		try:
			cleaned_password = next(reader).strip()
			password_sha256 = text_to_sha256(cleaned_password)

			if password_sha256 == target_sha256:
				print("Password found")
				print(f"Password: {cleaned_password}")
				return
		except StopIteration:
			break
	print("Password not found in given file")

if __name__ == '__main__':
	main()
