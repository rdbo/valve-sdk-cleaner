'''
<< SDK Cleaner by rdbo >>
https://github.com/rdbo/valve-sdk-cleaner
'''

import os
import platform

def get_file_list(path):
	path_separator = "/"
	if(platform.system() == "Windows"):
		path_separator = "\\"
	file_list = []
	for path, names, filenames in os.walk(path):
		for file in filenames:
			abs_file = f"{path}{path_separator}{file}"
			file_list.append(abs_file)
	return file_list

def main():
	hlsdk_folder = "halflife-master"
	srcsdk_folder = "source-sdk-2013-master"
	sdk_folder = os.path.dirname(os.path.realpath(__file__))
	if not (sdk_folder.endswith(hlsdk_folder) or sdk_folder.endswith(srcsdk_folder)):
		print(f"[!] Invalid SDK Folder: {sdk_folder}")
		print(f"[+] The SDK folder ends with '{hlsdk_folder}' or '{srcsdk_folder}'")
		return 0

	file_list = get_file_list(sdk_folder)
	print("[*] Cleaning SDK up ...")
	for file in file_list:
		if not (file.endswith(__file__) or file.endswith(".h") or file.endswith(".hpp")):
			os.remove(file)

	print("[*] The SDK has been successfully cleaned up")

	return 1

if __name__ == "__main__":
	main()
