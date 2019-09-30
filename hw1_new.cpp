#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
using namespace  std;

struct  Rotors{ //storing the five roters which are original
	char name;
	string unit;
	char notch;
	char Start;
};
struct Position {
	string turntable;
	char First_Position;
	char now;
	string ETW;
};
struct Plugboard {
	string input;
	string output;
};
Rotors I = { 'C',"EKMFLGDQVZNTOWYHXUSPAIBRCJ",'Y','H' };
Rotors II = { 'B',"AJDKSIRUXBLHWTMCQGZNPYFVOE",'M','D' };
Rotors III = { 'A',"BDFHJLCPRTXVZNYEIWGAKMUSQO",'D','X' };
Rotors IV = { 'D',"ESOVPZJAYQUIRHXLNFTGKDCMWB",'R','D' };
Rotors V = { 'E',"VZBRGITYUPSDNHLXAWMJQOFECK",'H','E' };
string reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT";
string ETW = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
string buffer1, buffer2;

Plugboard SetPlugboard(Plugboard plugboard,string setPlugboard) {

	for (int i = 0; i < 6; i++)
	{
		int position = i * 2;
			for (int j = 0; j < 26; j++)
			{
				if (plugboard.output[j] == setPlugboard[position])
				{
					plugboard.output[j] = setPlugboard[position + 1];
				}
				
				else if (plugboard.output[j] == setPlugboard[position + 1]) 
				{
					plugboard.output[j] = setPlugboard[position];
				}	
			}
	}

	return plugboard;
}
void first_position_changed(string &turntable, string &ETW, char first_position) {
	int i;
	for (i = 0; i < 26; i++) {
		if (ETW[i] == first_position) {
			buffer1 = turntable.substr(0, i);
			buffer2 = ETW.substr(0, i);
			break;
		}
	}
	turntable = turntable.substr(i, 26 - i);
	turntable = turntable + buffer1;
	ETW = ETW.substr(i, 26 - i);				
	ETW = ETW + buffer2;
}
void Encoding_before_reflector(int &encrypt_letter_position, string turntable, string ETW) {
	char t = turntable[encrypt_letter_position];
	int i;
	for (i = 0; i < 26; i++) {
		if (ETW[i] == t) {
			encrypt_letter_position = i;
			break;
		}
	}
}
void Encoding_after_reflector(char &encrypt_letter, string turntable, string ETW_now, string last_wheel_ETW, bool reflet) {
	int i;
	if (reflet == true)
	{
		for (i = 0; i < 26; i++) {
			if (last_wheel_ETW[i] == encrypt_letter) {
				break;
			}
		}
		encrypt_letter = ETW_now[i];
		for (i = 0; i < 26; i++) {
			if (turntable[i] == encrypt_letter) {
				break;
			}
		}
		encrypt_letter = last_wheel_ETW[i];
	}
	else
	{
		for (i = 0; i < 26; i++) {
			if (last_wheel_ETW[i] == encrypt_letter) {
				break;
			}
		}
		encrypt_letter = ETW_now[i];
		for (i = 0; i < 26; i++) {
			if (turntable[i] == encrypt_letter) {
				break;
			}
		}
		encrypt_letter = ETW[i];
	}
	
}
void rote_1(string &turntable,string &ETW) {
	buffer1 = turntable.substr(0, 1);
	turntable = turntable.substr(1, 25);
	turntable = turntable + buffer1;
	buffer2 = ETW.substr(0, 1);
	ETW = ETW.substr(1, 25);
	ETW = ETW + buffer2;
}

void encryption(Plugboard plugboard, Position rotor[], Position turntableStart[]) {
	string input;
	cin >> input;
	for (int i = 0; i < input.length(); i++)
	{

		for (int j = 0; j < 26; j++)
		{
			if (input[i] == plugboard.input[j])
			{
				input[i] = plugboard.output[j];
				break;
			}
			
		}
		
	}
			int i, k;
	k = 0;
	while (input[k] != '\0') {
		rote_1(rotor[0].turntable, rotor[0].ETW);
		rotor[0].now = rotor[0].ETW[0];
		//近絃锣笵ㄨ勃近絃锣
		if (rotor[0].now == rotor[0].First_Position && k != 0) {
			rote_1(rotor[1].turntable, rotor[1].ETW);
			rotor[1].now = rotor[1].ETW[0];
		}
		// DOUBLE STEP 惠耞近絃竚
		if ((rotor[1].now + 1) == rotor[1].First_Position  && rotor[0].now == I.Start && k != 0) {
			rote_1(rotor[2].turntable, rotor[2].ETW);
			rotor[2].now = rotor[2].ETW[0];
			rote_1(rotor[1].turntable, rotor[1].ETW);
			rotor[1].now = rotor[1].ETW[0];
		}
		int encrypt_letter_position;
		for (i = 0; i < 26; i++) {
			if (ETW[i] == input[k]) {
				encrypt_letter_position = i;
				break;
			}
		}
		for (i = 0; i < 3; i++) {
			Encoding_before_reflector(encrypt_letter_position, rotor[i].turntable, rotor[i].ETW);
		}

		char encrypt_letter = reflector[encrypt_letter_position];
		for (i = 2; i >= 0; i--) {
			bool reflet = false;2
			//は甮
			if (i == 2)
			{
				reflet = true;
				Encoding_after_reflector(encrypt_letter, turntableStart[i].turntable, rotor[i].ETW, ETW, reflet);
			}
			else
				//癴近絃
			{
				Encoding_after_reflector(encrypt_letter, turntableStart[i].turntable, rotor[i].ETW, rotor[i + 1].ETW, reflet);
			}
		}
		for (i = 0; i < 26; i++) {
			if (rotor[0].ETW[i] == encrypt_letter) {
				break;
			}
		}
		encrypt_letter = ETW[i];

		cout << encrypt_letter;

		k++;

	}
	cout << endl;
		
	
}
int main() {
	int i, j, n;
	string keyset, input;

	cin >> n;
	while (n--) {
		Rotors sel[5];
		sel[0] = I, sel[1] = II, sel[2] = III, sel[3] = IV, sel[4] = V;
		Position rotor[3];
		Position turntableStart[3];

		Plugboard plugboard = { "ABCDEFGHIJKLMNOPQRSTUVWXYZ","ABCDEFGHIJKLMNOPQRSTUVWXYZ" };
		cin >> keyset;
		for (i = 0; i < 3; i++) {
			for (j = 0; j < 5; j++) {
				if (sel[j].name == keyset[i]) {
					rotor[i].turntable = sel[j].unit;
					rotor[i].First_Position = sel[j].notch;
					rotor[i].ETW = ETW;
					turntableStart[i].turntable = sel[j].unit;
					turntableStart[i].First_Position = sel[j].notch;
					turntableStart[i].ETW = ETW;
					break;
				}
			}
		}
		string setPlugboard;
		cin >> setPlugboard;
		plugboard = SetPlugboard(plugboard, setPlugboard);

		for (int i = 0; i < 26; i++) {
			for (int j = 0; j < 26; j++) {
				for (int k = 26; k < 26; k++) {
					
				

					//for (i = 0; i < 3; i++) {
					//	rotor[i].now = keyset[3 + i];
					//	first_position_changed(rotor[i].turntable, rotor[i].ETW, keyset[3 + i]);
					//}
					rotor[0].now = ETW[i];
					first_position_changed(rotor[0].turntable, rotor[0].ETW, keyset[3];
					rotor[1].now = ETW[j];
					first_position_changed(rotor[1].turntable, rotor[1].ETW, keyset[4];
					rotor[2].now = ETW[k];
					first_position_changed(rotor[2].turntable, rotor[2].ETW, keyset[5];

					
					encryption(plugboard, rotor, turntableStart);
				}
			}
		}

						
	
						//

	

	}
	system("pause");
	return 0;
}


