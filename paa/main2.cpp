#include <iostream>
#include <string>
using namespace std;
string sort (string s)
{
	if (s.length ()%2==1) return s;
	string a, b;
	int len = s.length ()/2;
	a = sort(s.substr (0,len));
	b = sort(s.substr (len,len));
	if (a>b) return a+b;
	else return b+a;
}
int main ()
{
	string s1,s2;
	cin >> s1 >> s2;
	if (sort (s1) ==sort (s2)) cout<< "yes\n";
	else cout<< "no\n";
	return 0;
}