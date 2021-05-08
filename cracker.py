import hashlib

def text_to_sha256(text):
	sha256_hashed_text = hashlib.sha256(text.encode()).hexdigest()
	return sha256_hashed_text

def main():
	target_sha256 = input("Enter the SHA256 hash to crack: ").strip().lower()
	passwords_file = input("Enter the wordlist to look in: ")

	with open(passwords_file, 'r') as f:
		passwords = f.readlines()

	for password in passwords:
		cleaned_password = password.strip()
		password_sha256 = text_to_sha256(cleaned_password)

		if password_sha256 == target_sha256:
			print("Password found")
			print(f"Password: {cleaned_password}")
			return
	print("Password not found in given file")

if __name__ == '__main__':
	main()
