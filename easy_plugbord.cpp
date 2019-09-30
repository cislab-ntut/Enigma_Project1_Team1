#include <iostream>

using namespace std;

int main()
{
	char input_char[3]{};
	char exchange_char[3]{};
	bool output = false;
	bool lock = false;
	bool ex_time = true;
	int start_station = 0;
	char alphabet[26] = { 'A','B', 'C', 'D', 'E', 'F','G','H', 'I', 'J', 'K', 'L' ,'M', 'N','O', 'P', 'Q', 'R' ,'S' ,'T','U', 'V', 'W', 'X', 'Y', 'Z' };
	cout << "Input 3 char to switch" << endl;
	cin >> input_char;
	for (int first_number = 0; first_number<26; first_number++) {
		if (input_char[0] != alphabet[first_number]) {//the first char can't exchange with itself
			exchange_char[0] = alphabet[first_number];
			for (int second_number = start_station; second_number<26; second_number++) {
				if (input_char[1] != alphabet[second_number]) {
					if (alphabet[second_number] == input_char[0]&&ex_time) {
						exchange_char[0] = input_char[1];//force the first alphabet to exchange
						exchange_char[1] = input_char[0];
						lock = true;
					}
					else {
						exchange_char[1] = alphabet[second_number];
					}
					for (int third_number = 0; third_number<26; third_number++) {
						if (input_char[2] != alphabet[third_number]) {
							if (alphabet[third_number] == input_char[0] && exchange_char[0] != input_char[1]) {
								exchange_char[0] = input_char[2];//force the first alphabet to exchange
								exchange_char[2] = input_char[0];
							}
							else if (alphabet[third_number] == input_char[1] && exchange_char[0] != input_char[1]) {
								exchange_char[1] = input_char[2];//force the first alphabet to exchange
								exchange_char[2] = input_char[1];
							}
							else if(alphabet[third_number]!= input_char[0]&& alphabet[third_number] != input_char[1]&& alphabet[third_number] != exchange_char[0] && alphabet[third_number] != exchange_char[1]&& alphabet[third_number] != input_char[2]){
								exchange_char[2] = alphabet[third_number]; \
									output = true;
							}
						}
						if (output) {
							for (int i = 0; i < 3; i++) {
								cout << exchange_char[i];
							}
							cout << endl;
							output = false;
						}
					}
				}
				if (lock) {
					for (int i = 0; i < 3; i++) {
						exchange_char[i] = ' ';
					}
					ex_time = false;
					lock = false;
					start_station++;
					break;
				}
			}
		}
	}
	return 0;
}