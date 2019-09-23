
#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
using namespace  std;
struct password {
	char name;
	string unit;
	char Pointer;
	char Start;
};
struct Pointer {
	string turntable;
	char First_Pointer;
	char Position;
	string ETW;
};
password a = { 'A',"BDFHJLCPRTXVZNYEIWGAKMUSQO",'W','X' };
password b = { 'B',"AJDKSIRUXBLHWTMCQGZNPYFVOE",'F','D' };
password c = { 'C',"EKMFLGDQVZNTOWYHXUSPAIBRCJ",'R','H' };
password d = { 'D',"ESOVPZJAYQUIRHXLNFTGKDCMWB",'J','E' };
password e = { 'E',"HEJXQOTZBVFDASCILWPGYNMURK",'Z','H' };
string react = "YRUHQSLDPXNGOKMIEBFZCWVJAT", medi1,medi2, abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
void change_first(string &a, string &b, char t) {
	int i;
	for (i = 0; i < 26; i++) {
		if (b[i] == t) {
			medi1 = a.substr(0, i);
			medi2 = b.substr(0, i);
			break;
		}
	}
	a = a.substr(i, 26 - i);
	a = a + medi1;
	b = b.substr(i, 26 - i);
	b = b + medi2;
}
void change1(int &middle, string a, string b) {
	char t = a[middle];
	int i;
	for (i = 0; i < 26; i++) {
		if (b[i] == t) {
			middle = i;
			break;
		}
	}
}
void change2(char &re_middle, string a, string b, string c, bool Rec) {
	int i;
	if (Rec == true)
	{
		for (i = 0; i < 26; i++) {
			if (abc[i] == re_middle) {
				break;
			}
		}
		re_middle = b[i];
		for (i = 0; i < 26; i++) {
			if (a[i] == re_middle) {
				break;
			}
		}
		re_middle = abc[i];
	}
	else
	{
		for (i = 0; i < 26; i++) {
			if (c[i] == re_middle) {
				break;
			}
		}
		re_middle = b[i];
		for (i = 0; i < 26; i++) {
			if (a[i] == re_middle) {
				break;
			}
		}
		re_middle = abc[i];
	}
	
}
void add1(string &a,string &b) {
	medi1 = a.substr(0, 1);
	a = a.substr(1, 25);
	a = a + medi1;
	medi2 = b.substr(0, 1);
	b = b.substr(1, 25);
	b = b + medi2;
}
int main() {
	int i, j, k, n;
	string t;
	
	cin >> n;
	while (n--) {
		password sel[5];
		sel[0] = a, sel[1] = b, sel[2] = c, sel[3] = d, sel[4] = e;
		Pointer zhuanzi[3];
		Pointer turntableStart[3];
		cin >> t;
		for (i = 0; i < 3; i++) {
			for (j = 0; j < 5; j++) {
				if (sel[j].name == t[i]) {
					zhuanzi[i].turntable = sel[j].unit;
					zhuanzi[i].First_Pointer = sel[j].Pointer;
					zhuanzi[i].ETW = abc;
					turntableStart[i].turntable = sel[j].unit;
					turntableStart[i].First_Pointer = sel[j].Pointer;
					turntableStart[i].ETW = abc;
					break;
				}
			}
		}
		for (i = 0; i < 3; i++) {
			zhuanzi[i].Position = t[3 + i];
			change_first(zhuanzi[i].turntable, zhuanzi[i].ETW, t[3 + i]);
		}
		cin >> t;
		
		k = 0;
		while (t[k] != '\0') {
			add1(zhuanzi[0].turntable, zhuanzi[0].ETW);
			zhuanzi[0].Position = zhuanzi[0].ETW[0];
			//近絃锣笵ㄨ勃近絃锣
			if (zhuanzi[0].Position == zhuanzi[0].First_Pointer && k != 0) {
				add1(zhuanzi[1].turntable, zhuanzi[1].ETW);
				zhuanzi[1].Position = zhuanzi[1].ETW[0];
			}
			// DOUBLE STEP 惠耞近絃竚
			if ((zhuanzi[1].Position+1) == zhuanzi[1].First_Pointer  && zhuanzi[0].Position==a.Start && k != 0) {
				add1(zhuanzi[2].turntable, zhuanzi[2].ETW);
				zhuanzi[2].Position = zhuanzi[2].ETW[0];
				add1(zhuanzi[1].turntable, zhuanzi[1].ETW);
				zhuanzi[1].Position = zhuanzi[1].ETW[0];
			}
			int middle;
			for (i = 0; i < 26; i++) {
				if (abc[i] == t[k]) {
					middle = i;
					break;
				}
			}
			for (i = 0; i < 3; i++) {
				change1(middle, zhuanzi[i].turntable, zhuanzi[i].ETW);
			}

			char re_middle = react[middle];
			for (i = 2; i >= 0; i--) {
				bool Rec = false;
				//は甮
				if (i == 2)
				{
					Rec = true;
					change2(re_middle, turntableStart[i].turntable, zhuanzi[i].ETW, abc, Rec);
				}
				else
					//癴近絃
				{
					change2(re_middle, turntableStart[i].turntable, zhuanzi[i].ETW, zhuanzi[i+1].ETW, Rec);
				}
			}
			for (i = 0; i < 26; i++) {
				if (zhuanzi[0].ETW[i] == re_middle) {
					break;
				}
			}
			re_middle = abc[i];

			cout << re_middle;

			k++;
			
		}
		cout << endl;

	}
	system("pause");
	return 0;
}


